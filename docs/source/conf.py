# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('../../src/'))

project = 'The Instructed Glacier Model (IGM)'
copyright = '2023, Guillaume Jouvet'
author = 'Guillaume Jouvet'
release = 'v1.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc','sphinx.ext.napoleon','sphinx.ext.mathjax',
    'sphinx.ext.autosummary','sphinx.ext.mathjax','sphinx.ext.doctest',
    'numpydoc', 'sphinx_mdinclude', 'sphinx_rtd_theme'
]

napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

templates_path = ['_templates']
exclude_patterns = ['setup*', 'versioneer*']

numpydoc_show_class_members = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme_options = {
    'display_version': False,
    'navigation_depth': 2,
    'collapse_navigation': False,
    "sticky_navigation": False,
    "titles_only": True
}

html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------
autodoc_mock_imports = ['matplotlib', 'tensorflow', 'netCDF4', 'scipy', 'numpy']
