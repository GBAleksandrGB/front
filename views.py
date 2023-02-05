from jinja2 import Environment, FileSystemLoader


def render(template_name, folder='templates', static_url='/static/', **kwargs):
    env = Environment()
    env.loader = FileSystemLoader(folder)
    env.globals['static'] = static_url
    template = env.get_template(template_name)
    return template.render(**kwargs)


class Index:
    def __call__(self):
        return '200 OK', render('index.html')


class Contacts:
    def __call__(self):
        return '200 OK', render('contacts.html')
