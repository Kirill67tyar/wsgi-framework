from os.path import join
from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment


# jinja2 - шаблонизатор
# jinja2.Template - обспечивает открытие и считывание содержимого шаблона в строку

# def render(template_name, folder='templates', context={}):  # **context):
#     """
#         :param template_name: имя шаблона
#         :param folder: папка где находится шаблон
#         :param context: контекст передаваемый в шаблон
#         :return:
#     """
#     file = join(folder, template_name)
#     with open(file, mode='r', encoding='utf-8') as f:
#         template = Template(f.read())
#     # рендерим шаблон конекстом
#     return template.render(**context)

def render(template_name, folder='templates', context={}):  # **context):
    """
        :param template_name: имя шаблона
        :param folder: папка где находится шаблон
        :param context: контекст передаваемый в шаблон
        :return:
    """
    # создаём окружение для загрузки шаблонов
    env = Environment()

    # в окружении указываем путь, по которму нужно искать наши шаблоны
    env.loader = FileSystemLoader(folder)

    # загружает конкретный шаблон, который мы будем передовать
    template = env.get_template(template_name)

    # рендерим контекст
    return template.render(**context)
