from pprint import pprint as pp
import csv
from simba_framework.templator import render
from db.record_in_db import record

class Index:

    # def __init__(self, request, *args, **kwargs):
    #     self.request = request

    def __call__(self, request, *args, **kwargs):
        return '200 ok', render(
            template_name='index1.html',
            folder='templates',
            context={'variable': 'IMPORTANT DATA', },
            # context={},
        ),


class About:
    # def __init__(self, request, *args, **kwargs):
    #     self.request = request

    def __call__(self, request, *args, **kwargs):
        return '200 ok', 'about',


class Feedback:
    def __call__(self, request, *args, **kwargs):
        if request['method'] == 'POST':
            record(request['data'])
            return '302 ok', 'File was recorded'
        else:
            return '200 ok', render(
                template_name='feedback.html',
                folder='templates'
            )
