import os

from jinja2 import FileSystemLoader, Environment, Template
from jinja2.ext import with_


__all__ = ('get_template', )


def get_template():
    """Loads project-bound schematic template.

    Returns `jinja2.Template`.
    """

    template_base = os.path.join(os.path.dirname(__file__), 'templates')

    # read template
    jinja_env = Environment(extensions=[with_],
                            loader=FileSystemLoader(template_base))
    template = jinja_env.get_template('schematic.tpl')

    return template
