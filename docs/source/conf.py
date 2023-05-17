# Configuration file for the Sphinx documentation builder.
import pathlib
import sys
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

# -- Project information

project = 'slskd-python-api'
copyright = '2023, bigoulours'
author = 'bigoulours'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

add_module_names = False

# autodoc_typehints="none"
# typehints_document_rtype = False
typehints_use_rtype = False
typehints_use_signature = True
#typehints_use_signature_return = True

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

