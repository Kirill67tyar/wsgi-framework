from simba_framework.templator import render

class Index:

    def __call__(self, *args, **kwargs):
        return '200 ok', render(
            template_name='index.html',
            folder='templates',
            context={}
        ),
"""
template_name, folder='templates', context={}
"""

class About:
    def __call__(self, *args, **kwargs):
        return '200 ok', 'about',
