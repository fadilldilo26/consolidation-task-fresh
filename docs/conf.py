# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django

# THIS IS THE MAGIC LINE FOR SPHINX TO FIND YOUR CODE
# It tells Sphinx to look in the folder above 'docs' (your main project folder)
sys.path.insert(0, os.path.abspath('..'))

# Set the Django settings module so Sphinx can understand your models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_project.settings')

# Initialize Django
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'News Capstone Consolidation'
copyright = '2026, Faadhil Khan'
author = 'Faadhil Khan'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc', # Automatically generate docs from docstrings
    'sphinx.ext.viewcode', # Add links to source code
    'sphinx.ext.napoleon', # Support for Google style docstrings
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']