# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Roguelike'
copyright = '2024, Nikita Stepanov <nistepanovme@gmail.com> && Mihail Frolov <m@mail.ru> && Arseniy Brothers <arseniys@gmail.com>'
author = (
    'Nikita Stepanov <nistepanovme@gmail.com> && Mihail Frolov <m@mail.ru> && Arseniy Brothers <arseniys@gmail.com>'
)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
