import sys
from wsgiref.simple_server import make_server

from urls import urlpatterns
from simba_framework.main import (
    Framework,
    ForExit,
    output_in_console,
)
from common.analyzetools import delimiter

"""
    def make_server(
        host, port, app, server_class=WSGIServer, handler_class=WSGIRequestHandler
    ):
"""

application = Framework(routes_obj=urlpatterns)

host = ''
port = 8080

if len(sys.argv) > 1:
    for a in sys.argv:
        if '--host' in a:
            host = a.split('=')[-1]
        elif '--port' in a:
            port = int(a.split('=')[-1])


# создаём wsgi-сервер, который будет прослушивать указанный хост и порт
# with make_server(host, port, app=application) as server:
#     print('Запуск с нашего фреймворка')
#     running_host = server.server_address[0]
#     running_port = server.server_address[-1]
#     print(f'http://{running_host}:{running_port}')
#     print(f'http://127.0.0.1:{running_port}')
#     print()
#     print('For exit press "ctrl+c"')
#     try:
#         server.serve_forever()
#     except KeyboardInterrupt:
#         print('\n', '- ' * 20)
#         raise SystemExit('Server finished working')


def runserver():
    with ForExit() as for_exit:
        with make_server(host, port, app=application) as server:
            output_in_console(server)
            server.serve_forever()


def main():
    commands = sys.argv.copy()
    commands = list(map(lambda x: x.lower(), commands))
    if 'runserver' in commands:
        runserver()
    else:
        delimiter()
        print('ERROR')
        print('May be you want use command "runserver"')


if __name__ == '__main__':
    main()
