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
        status_code, body = view()

        # start_response - отправляет код ответа и заголовки
        start_response(status_code, [('Content-Type', 'text/html',), ])

        # передаём через WSGI коннектор на сторону web-сервера байты
        # преращая str в байты
        # nginx или apache передаст само тело ответа клиенту
        return [body.encode('utf-8'), ]
