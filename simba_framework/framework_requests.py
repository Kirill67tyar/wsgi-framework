import quopri
from pprint import pprint as pp

from common.analyzetools import (
    p_type, p_dir, p_mro,
)


class BaseRequest:

    @staticmethod
    def pars_data(data: str) -> dict:
        if data:
            data = data.split('&')
            output = {
                part.split('=')[0]: part.split('=')[-1]
                for part in data
            }
            output.pop('', None)
        else:
            output = {}
        return output


class GetRequests(BaseRequest):

    def get_data(self, environ: dict) -> dict:
        # --------- console ----------
        # print(environ['QUERY_STRING'])
        # --------- console ----------

        return self.pars_data(environ['QUERY_STRING'])


class PostRequests(BaseRequest):

    @staticmethod
    def get_wsgi_input_data(environ: dict) -> str:
        data = b''
        if environ.get('CONTENT_LENGTH'):
            content_length = int(environ['CONTENT_LENGTH'])
            if content_length:
                data = environ['wsgi.input'].read(content_length)

                # # --------- console ----------
                # p_type(environ['wsgi.input'])  # <class '_io.BufferedReader'>
                # p_type(data)  # <class 'bytes'>
                # # --------- console ----------

        data = data.decode('utf-8')  # декодируем из байтов в str
        return data

    @staticmethod
    def decode_value(data: dict) -> dict:
        """
            Это нужно для кириллицы
        """
        # # --------- console ----------
        # # кириллица до преобразования
        # pp(data)
        # # --------- console ----------

        print('\n')
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace('+', ' '), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str

        # # --------- console ----------
        # # кириллица после преобразования
        # pp(new_data)
        # # --------- console ----------

        return new_data

    def get_data(self, environ: dict) -> dict:
        # получаем данные из словаря окружения, преобразовывая байты в str
        data = self.get_wsgi_input_data(environ)  # some_key=hello-from-data&another-key=Кириллица
        # преобразуем данные из str в dict
        data = self.pars_data(data)  # {'some_key': 'hello-from-data', ...
        # для обработки кириллицы
        data = self.decode_value(data)  # {'some_key': 'hello-from-data', ...
        return data


"""
Чтобы получить тело post запроса, его нужно декодировать из байтов в str
variable.decode(encoding='utf-8')

Но перед этим нужно проверить что, в теле запроса вообще что-то пришло
environ['CONTENT_LENGTH']
И если при post запросе приходит что-то в теле, 
это хранится в ключе wsgi.input


"""
