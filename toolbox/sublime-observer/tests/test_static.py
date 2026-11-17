"""Source-level guarantees that do not need an editor."""
import ast
import json
import os
import re
import unittest

import fakes

PKG = os.path.join(fakes.IMPL, 'SublimeObserver')
SOURCES = ('publisher.py', 'contract.py')
FORBIDDEN_IMPORTS = {'socket', 'socketserver', 'subprocess', 'multiprocessing', 'signal', 'select',
                     'selectors', 'asyncio', 'http', 'urllib', 'ctypes', 'dbus', 'xmlrpc'}
# Calls that would change a view, focus, selection or scroll, list views, or act on another process.
FORBIDDEN_ATTRS = {'run_command', 'focus_view', 'focus_sheet', 'focus_group', 'set_viewport_position',
                   'show', 'show_at_center', 'set_clipboard', 'open_file', 'insert', 'erase', 'add',
                   'subtract', 'add_regions', 'views', 'sheets', 'windows', 'active_window',
                   'kill', 'killpg', 'popen', 'system'}
CONTRACT_ALLOWED = {'add'}          # set.add on in-memory bookkeeping only


def tree(name):
    with open(os.path.join(PKG, name), encoding='utf-8') as handle:
        return ast.parse(handle.read(), filename=name, feature_version=(3, 8))


class StaticTests(unittest.TestCase):
    def test_python_38_grammar(self):
        for name in SOURCES:
            tree(name)       # raises SyntaxError on post-3.8 syntax

    def test_no_transport_or_process_imports(self):
        for name in SOURCES:
            for node in ast.walk(tree(name)):
                names = []
                if isinstance(node, ast.Import):
                    names = [a.name for a in node.names]
                elif isinstance(node, ast.ImportFrom) and node.module:
                    names = [node.module]
                for imported in names:
                    self.assertNotIn(imported.split('.')[0], FORBIDDEN_IMPORTS, (name, imported))

    def test_no_view_changing_listing_or_signalling_calls(self):
        for name in SOURCES:
            allowed = CONTRACT_ALLOWED if name == 'contract.py' else set()
            used = {n.attr for n in ast.walk(tree(name)) if isinstance(n, ast.Attribute)}
            self.assertEqual(sorted((used & FORBIDDEN_ATTRS) - allowed), [], name)

    def test_contract_module_has_no_sublime_import(self):
        imports = [n for n in ast.walk(tree('contract.py')) if isinstance(n, (ast.Import, ast.ImportFrom))]
        for node in imports:
            mods = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module or '']
            for mod in mods:
                self.assertFalse(mod.startswith('sublime'), mod)

    def test_package_layout(self):
        names = set(os.listdir(PKG)) - {'__pycache__'}
        self.assertEqual(names, {'publisher.py', 'contract.py', '.python-version',
                                 'SublimeObserver.sublime-settings', 'SublimeObserver.sublime-commands'})
        with open(os.path.join(PKG, '.python-version')) as handle:
            self.assertEqual(handle.read().strip(), '3.8')

    def test_one_palette_entry(self):
        with open(os.path.join(PKG, 'SublimeObserver.sublime-commands'), encoding='utf-8') as handle:
            raw = re.sub(r',\s*([\]}])', r'\1', handle.read())     # Sublime JSON allows trailing commas
        entries = json.loads(raw)
        self.assertEqual(entries, [{'caption': 'Sublime Observer: Share This View (toggle)',
                                    'command': 'sublime_observer_toggle_share'}])

    def test_settings_defaults_match_contract(self):
        with open(os.path.join(PKG, 'SublimeObserver.sublime-settings'), encoding='utf-8') as handle:
            text = handle.read()
        raw = re.sub(r'^\s*//.*$', '', text, flags=re.M)
        values = json.loads(re.sub(r',\s*([\]}])', r'\1', raw))
        self.assertEqual(values, {'root': None, 'cap_chars': 200000, 'debounce_ms': 150, 'max_delay_ms': 1000,
                                  'viewport_poll_ms': 500, 'heartbeat_s': 1})


if __name__ == '__main__':
    unittest.main()
