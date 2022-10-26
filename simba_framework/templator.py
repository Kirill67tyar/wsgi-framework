from os.path import join
from jinja2 import Template


# jinja2 - шаблонизатор
# jinja2.Template - обспечивает открытие и считывание содержимого шаблона в строку

def render(template_name, folder='templates', context={}):  # **context):
    """

    :param template_name: имя шаблона
    :param folder: папка где находится шаблон
    :param context: контекст передаваемый в шаблон
    :return:
    """
    file = join(folder, template_name)
    with open(file, mode='r', encoding='utf-8') as f:
        template = Template(f.read())
    # рендерим шаблон конекстом
    return template.render(**context)
