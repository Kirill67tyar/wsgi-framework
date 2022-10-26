from simba_framework.templator import render


class Index:

    # def __init__(self, request, *args, **kwargs):
    #     self.request = request

    def __call__(self, request, *args, **kwargs):
        return '200 ok', render(
            template_name='index.html',
            folder='templates',
            context={}
        ),


"""
template_name, folder='templates', context={}
"""


class About:
    # def __init__(self, request, *args, **kwargs):
    #     self.request = request

    def __call__(self, request, *args, **kwargs):
        return '200 ok', 'about',
