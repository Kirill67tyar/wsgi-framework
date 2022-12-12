import sys
import quopri
from pprint import pprint as pp

from .framework_requests import GetRequests, PostRequests
from common.analyzetools import (
    p_dir, p_mro, p_glob, p_loc, p_type,
    delimiter, p_content, show_builtins,
    show_doc, console, console_compose,
)


class PageNotFond404:  # (Exception)
    def __call__(self, *args, **kwargs):
        return '404 empty', '404 Page Not Found',


class Framework:
    """
        Класс Framework - основа WSGI-фреймворка
    """

    def __init__(self, routes_obj):
        self.routes_dict = routes_obj

    def __call__(self, environ, start_response):

        # --------- console ----------
        # pp(environ)
        # --------- console ----------

        request = {
            'method': environ['REQUEST_METHOD'],
        }

        if request['method'] == 'GET':
            request['data'] = GetRequests().get_data(environ)

            # --------- console ----------
            # pp(request['data'])
            # --------- console ----------

        elif request['method'] == 'POST':
            request['data'] = PostRequests().get_data(environ)

            # # --------- console ----------
            # pp(request['data'])
            # pp(self.decode_value(request['data']))
            # # --------- console ----------

        # получаем адрес по которому пользователь выполнил переход
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path += '/'

        # находим нужный контроллер
        view = self.routes_dict.get(path)
        if not view:
            # но непонятно, как присвоить другие ошибки из client error и server error
            view = PageNotFond404()  # заглушка

        # запускаем контроллер
        status_code, body = view(request)

        # start_response - отправляет код ответа и заголовки
        start_response(status_code, [('Content-Type', 'text/html',), ])

        # передаём через WSGI коннектор на сторону web-сервера байты
        # преращая str в байты
        # nginx или apache передаст само тело ответа клиенту
        return [body.encode('utf-8'), ]  # из str в байты

    @staticmethod
    def decode_value(data: dict) -> dict:
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace('+', ' '), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data


class ForExit:

    def __enter__(self):
        return True

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('\n', '- ' * 20)
        print('Server finished working')
        if issubclass(exc_type, KeyboardInterrupt):
            sys.exit()
        # return True


def output_in_console(server):
    print('Запуск с нашего фреймворка')
    running_host = server.server_address[0]
    running_port = server.server_address[-1]
    print(f'http://{running_host}:{running_port}')
    print(f'http://127.0.0.1:{running_port}')
    print()
    print('For exit press "ctrl+c"')
