"""
Опиши класс ошибки с методос __call__, где он просто вернёт
return '404 what', '404 PAGE Not Found',

И так:
1) пишем класс Framework
2) __init__ принимает список путей (словарь с путями скорее всего)
3) __call__ как wsgi функция
4) принимает start_response и environ
5) environ у нас словарь с переменными окружения как от CGI
    там есть переменная PTH_INFO
    именно благодаря этой переменной мы и можем узнать
    абсолютный url на который пользователь отправил HTTP-запрос
    Обязательно проверь, что url заканчивается на /
6) проверяем что url есть в списке с путями
7) если есть, то созаём переменную view, если нет, и присваиваем значение
в словаре в списке путей
если нет, view = PageNotFound404()

создаём две переменные:
status_code и body от нашей функции
вызываем функцию start_response со статус кодом и заголовком
возвращаем тело, преращая его из str в байты
body.encode('utf-8')

"""


class PageNotFond404:  # (Exception)
    def __call__(self, *args, **kwargs):
        return '404 увы', '404 PAGE Not Found',


class Framework:
    """
        Класс Framework - основа WSGI-фреймворка
    """

    def __init__(self, routes_obj):
        self.routes_dict = routes_obj

    def __call__(self, environ, start_response):
        # получаем адрес по которому пользователь выполнил переход
        path = environ['PATH_INFO']
        if not path.endwith('/'):
            path = path + '/'

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
        # nginx или apache передаст само тело ответа клиенту
        return [body.encode('utf-8'), ]
