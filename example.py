import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_ENVIRONMENT = Environment(loader=FileSystemLoader(os.path.join(PATH, 'templates')))


def render_template(template_filename, context_data):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context_data)


def create_config(input_filename, output_filename, context_data):

    with open(output_filename, 'w') as f:
        buf = render_template(input_filename, context_data)
        f.write(buf)


if __name__ == "__main__":

    context = {
        'AUTH_BACKEND': 'micronodes.io',
        'AUTH_PORT': 8080
    }

    create_config(input_filename="example.j2", output_filename="example.conf", context_data=context)
