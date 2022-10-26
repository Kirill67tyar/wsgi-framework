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

    def get_data(self, environ: dict):
        print(environ['QUERY_STRING'])
        return self.pars_data(environ['QUERY_STRING'])


class PostRequests(BaseRequest):

    @staticmethod
    def get_wsgi_input_data(environ: dict) -> bytes:
        data = b''
        if environ.get('CONTENT_LENGTH'):
            content_length = int(environ['CONTENT_LENGTH'])
            if content_length:
                data = environ['wsgi.input'].read(content_length)
        return data

    def get_data(self, environ: dict):
        result = {}
        data_bytes = self.get_wsgi_input_data(environ)
        if data_bytes:
            data_str = data_bytes.decode('utf-8')
            result = self.pars_data(data_str)
        return result


"""
Чтобы получить тело post запроса, его нужно декодировать из байтов в str
variable.decode(encoding='utf-8')

Но перед этим нужно проверить что, в теле запроса вообще что-то пришло
environ['CONTENT_LENGTH']
И если при post запросе приходит что-то в теле, 
это хранится в ключе wsgi.input


"""
