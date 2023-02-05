import os
from wsgiref.simple_server import make_server

from ulrs import routes
import settings


class PageNotFound404:
    def __call__(self):
        return '404 WHAT', '404 PAGE Not Found'


class Framework:
    def __init__(self, routes_dct, params):
        self.routes_dct = routes_dct
        self.params = params

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.routes_dct:
            view = self.routes_dct[path]
            content_type = self.get_content_type(path)
            code, body = view()
            body = body.encode('UTF-8')
        elif path.startswith(self.params.STATIC_URL):
            file_path = path[len(self.params.STATIC_URL):len(path) - 1]
            content_type = self.get_content_type(file_path)
            code, body = self.get_static(self.params.STATIC_FILES_DIR, file_path)
        else:
            view = PageNotFound404()
            content_type = self.get_content_type(path)
            code, body = view()
            body = body.encode('utf-8')

        start_response(code, [('Content-Type', content_type)])
        return [body]

    @staticmethod
    def get_content_type(file_path, content_types_map=settings.CONTENT_TYPES_MAP):
        file_name = os.path.basename(file_path).lower()
        extension = os.path.splitext(file_name)[1]
        return content_types_map.get(extension, "text/html")

    @staticmethod
    def get_static(static_dir, file_path):
        path_to_file = os.path.join(static_dir, file_path)
        with open(path_to_file, 'rb') as f:
            file_content = f.read()
        status_code = '200 OK'
        return status_code, file_content


app = Framework(routes, settings)

with make_server('', 8080, app) as httpd:
    print("Запуск на порту 8080...")
    httpd.serve_forever()
