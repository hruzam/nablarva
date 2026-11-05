export async function api(path, options = {}) {
  const method = options.method || 'GET';
  const headers = {...options.headers};
  if (!['GET','HEAD'].includes(method)) headers['X-Console-Action'] = '1';
  let body = options.body;
  if (body !== undefined && !(body instanceof Blob) && !(body instanceof ArrayBuffer)) {
    body = JSON.stringify(body); headers['Content-Type'] = 'application/json';
  }
  const response = await fetch(path, {...options, method, headers, body, credentials:'same-origin', cache:'no-store'});
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    const error = new Error(data.error?.message || data.message || `Request failed (${response.status})`);
    error.status = response.status; error.detail = data; throw error;
  }
  return data;
}
