import hashlib
import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
import uuid

from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase

spec = importlib.util.spec_from_file_location("vault", Path(__file__).parents[1] / "host" / "vault.py")
vault = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vault)


class VaultTests(AioHTTPTestCase):
    async def get_application(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "vault"
        app = web.Application()
        vault.install_vault(app, self.root)
        return app

    async def asyncTearDown(self):
        await super().asyncTearDown()
        self.temp.cleanup()

    async def test_revision_and_immutable_kind(self):
        id = str(uuid.uuid4())
        url = '/api/vault/' + id
        body = {'kind': 'prompt', 'name': 'Czech', 'text': 'žluťoučký', 'expectedRevision': 0}
        response = await self.client.put(url, json=body)
        self.assertEqual(response.status, 200)
        created = await response.json()
        self.assertEqual((created['revision'], created['text']), (1, body['text']))
        response = await self.client.put(url, json=body)
        self.assertEqual((response.status, (await response.json())['currentRevision']), (409, 1))
        body.update(expectedRevision=1, kind='shortcut')
        self.assertEqual((await self.client.put(url, json=body)).status, 409)
        body.update(kind='prompt', text='updated')
        self.assertEqual((await (await self.client.put(url, json=body)).json())['revision'], 2)
        self.assertEqual((await self.client.delete(url, json={'expectedRevision': 1})).status, 409)
        self.assertEqual((await (await self.client.get(url)).json())['text'], 'updated')
        self.assertEqual((await self.client.delete(url, json={'expectedRevision': 2})).status, 200)
        self.assertEqual((await self.client.get(url)).status, 404)

    async def test_upload_verify_retry_and_download(self):
        data = b'\xff\xd8EXIF\x00photo\xff\xd9'
        headers = {'X-Upload-ID': str(uuid.uuid4()), 'X-File-Name': '..%2Fsecret%20%C5%BE.jpg',
                   'X-Content-SHA256': hashlib.sha256(data).hexdigest()}
        response = await self.client.post('/api/files', data=data, headers=headers)
        self.assertEqual(response.status, 200)
        item = await response.json()
        self.assertTrue(item['verified'])
        self.assertEqual(item['path'], str(self.root / item['id']))
        self.assertEqual((self.root / item['id']).read_bytes(), data)
        download = await self.client.get(item['downloadUrl'])
        self.assertEqual(await download.read(), data)
        self.assertEqual(download.headers['X-Content-Type-Options'], 'nosniff')
        retry = await self.client.post('/api/files', data=data, headers=headers)
        self.assertEqual(await retry.json(), item)
        headers['X-File-Name'] = 'other'
        self.assertEqual((await self.client.post('/api/files', data=data, headers=headers)).status, 409)
        headers['X-File-Name'] = '..%2Fsecret%20%C5%BE.jpg'
        self.assertEqual((await self.client.post('/api/files', data=b'wrong', headers=headers)).status, 422)
        listing = await (await self.client.get('/api/vault')).json()
        self.assertEqual(len(listing['items']), 1)
        self.assertEqual({p.name for p in self.root.iterdir()} - {'vault.sqlite3', item['id']}, set())

    async def test_failed_upload_leaves_no_item_or_blob(self):
        headers = {'X-Upload-ID': str(uuid.uuid4()), 'X-File-Name': 'x',
                   'X-Content-SHA256': hashlib.sha256(b'expected').hexdigest()}
        self.assertEqual((await self.client.post('/api/files', data=b'wrong', headers=headers)).status, 422)
        self.assertEqual((await (await self.client.get('/api/vault')).json())['items'], [])
        self.assertEqual({p.name for p in self.root.iterdir()}, {'vault.sqlite3'})

    async def test_symlink_blob_is_not_followed_and_invalid_ids_rejected(self):
        data = b'picture'
        headers = {'X-Upload-ID': str(uuid.uuid4()), 'X-File-Name': 'x', 'X-Content-SHA256': hashlib.sha256(data).hexdigest()}
        item = await (await self.client.post('/api/files', data=data, headers=headers)).json()
        outside = Path(self.temp.name) / 'secret'
        outside.write_bytes(b'secret')
        (self.root / item['id']).unlink()
        (self.root / item['id']).symlink_to(outside)
        self.assertEqual((await self.client.get(item['downloadUrl'])).status, 404)
        self.assertEqual((await self.client.get('/api/files/not-a-uuid')).status, 400)
        self.assertEqual(outside.read_bytes(), b'secret')
        self.assertEqual((await self.client.post('/api/files', data=data, headers=headers)).status, 500)


class RootTests(unittest.TestCase):
    def test_reject_symlink_and_nonprivate_root(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            target = base / 'target'
            target.mkdir(mode=0o700)
            (base / 'link').symlink_to(target, target_is_directory=True)
            with self.assertRaises(ValueError):
                vault.install_vault(web.Application(), base / 'link')
            target.chmod(0o755)
            with self.assertRaises(ValueError):
                vault.install_vault(web.Application(), target)


if __name__ == '__main__':
    unittest.main()
