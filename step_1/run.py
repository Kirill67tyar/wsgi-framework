from wsgiref.simple_server import make_server

from urls import urlpatterns
from simba_framework.main import Framework

"""def make_server(
    host, port, app, server_class=WSGIServer, handler_class=WSGIRequestHandler
):"""

application = Framework(routes_obj=urlpatterns)

# создаём wsgi-сервер, который будет прослушивать указанный хост и порт
with make_server('', 8080, app=application) as server:
    print('Запуск с нашего фреймворка')
    host = server.server_address[0]
    port = server.server_address[-1]
    print(f'http://{host}:{port}')
    print(f'http://127.0.0.1:{port}')
    server.serve_forever()
