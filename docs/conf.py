# -*- coding: utf-8 -*-

import sys
import os
import re
import datetime

# If we are building locally, or the build on Read the Docs looks like a PR
# build, prefer to use the version of the theme in this repo, not the installed
# version of the theme.


def is_development_build():
    # PR builds have an interger version
    re_version = re.compile(r'^[\d]+$')
    if 'READTHEDOCS' in os.environ:
        version = os.environ.get('READTHEDOCS_VERSION', '')
        if re_version.match(version):
            return True
        return False
    return True


sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('..') + '/fuzzycorr')
sys.path.append(os.path.abspath('..') + '/examples')

# the following modules will be mocked (i.e. bogus imports - required for C-dependent packages)
autodoc_mock_imports = ['earthpy', 'numpy', 'gdal', 'matplotlib', 'geopandas', 'rasterio', 'scipy',
                        'ogr', 'pandas', 'alphashape', 'mapclassify', 'pyproj', 'interpolate']

import sphinx_rtd_theme
from sphinx.locale import _

project = u'FuzzyCorr'
slug = re.sub(r'\W+', '-', project.lower())
version = '0.0.1'
release = '0.0.1'
author = u'Beatriz Negreiros'
copyright = author
language = 'en'

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'sphinx_thebe',
    'sphinx_rtd_theme'
]

templates_path = ['_templates']
source_suffix = '.rst'
exclude_patterns = []
locale_dirs = ['locale/', 'docs/']
gettext_compact = False

master_doc = 'index'
suppress_warnings = ['image.nonlocal_uri']
pygments_style = 'default'

intersphinx_mapping = {
    'rtd': ('https://docs.readthedocs.io/en/latest/', None),
    'sphinx': ('http://www.sphinx-doc.org/en/stable/', None),
}

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'navigation_depth': 5,
    'canonical_url': '',
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': 'White',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': False,
    'includehidden': -1,
    'titles_only': False
}

html_context = {
    'author': 'Beatriz Negreiros',
    'date': datetime.date.today().strftime('%Y-%m-%d'),
    'display_github': True,
    'github_user': 'beatriznegreiros',
    'github_repo': 'fuzzycorr',
    'github_version': 'master/',
}

if not 'READTHEDOCS' in os.environ:
    html_static_path = ['_static/']
    html_js_files = ['debug.js']

    # Add fake versions for local QA of the menu
    html_context['test_versions'] = list(map(
        lambda x: str(x / 10),
        range(1, 100)
    ))

html_logo = os.path.abspath('..') + '/docs/img/logo.svg'
html_show_sourcelink = True
htmlhelp_basename = slug


latex_documents = [
  ('index', '{0}.tex'.format(slug), project, author, 'manual'),
]

man_pages = [
    ('index', slug, project, [author], 1)
]

texinfo_documents = [
  ('index', slug, project, author, slug, project, 'Miscellaneous'),
]


# Extensions to theme docs
def setup(app):
    from sphinx.domains.python import PyField
    from sphinx.util.docfields import Field

    app.add_object_type(
        'confval',
        'confval',
        objname='configuration value',
        indextemplate='pair: %s; configuration value',
        doc_field_types=[
            PyField(
                'type',
                label=_('Type'),
                has_arg=False,
                names=('type',),
                bodyrolename='class'
            ),
            Field(
                'default',
                label=_('Default'),
                has_arg=False,
                names=('default',),
            ),
        ]
    )


# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True
napoleon_custom_sections = None
