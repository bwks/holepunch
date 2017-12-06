from jinja2 import Environment, PackageLoader, FileSystemLoader


def template_loader(package_dir, template_dir,  trim_blocks=True, lstrip_blocks=True):
    """
    Define environment template loader.
    http://jinja.pocoo.org/docs/dev/api/
    :param package_dir: package directory
    :param template_dir: template directory
    :param trim_blocks: remove newlines caused by template tags
    :param lstrip_blocks: remove leading spaces and tabs caused by template tags
    :return: environment package loader
    """
    return Environment(loader=PackageLoader(package_dir, template_dir),
        trim_blocks=trim_blocks, lstrip_blocks=lstrip_blocks)


def file_system_loader(search_paths, trim_blocks=True, lstrip_blocks=True):
    """
    File system template loader
    :param search_paths: List of paths to search for templates
    :param trim_blocks: remove newlines caused by template tags
    :param lstrip_blocks: remove leading spaces and tabs caused by template tags
    :return: file system loader
    """
    return Environment(loader=FileSystemLoader(searchpath=search_paths),
        trim_blocks=trim_blocks, lstrip_blocks=lstrip_blocks)

def render_from_template(directory, template_name, **kwargs):
    """
    from: https://www.pydanny.com/jinja2-quick-load-function.html. Thanks pydanny
    >>> from simple_script import render_from_template
    >>> data = {
    ...     "date": "June 12, 2014",
    ...     "items": ["oranges", "bananas", "steak", "milk"]
    ... }
    >>> render_from_template(".", "shopping_list.html", **data)

    """
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(**kwargs)

