import os
import sys

# THIS IS THE MAGIC LINE FOR SPHINX TO FIND YOUR CODE
sys.path.insert(0, os.path.abspath('..')) 

project = 'News Capstone Consolidation'
copyright = '2026, Faadhil Khan'
author = 'Faadhil Khan'

extensions = [
    'sphinx.ext.autodoc', # Reads your docstrings automatically
    'sphinx.ext.viewcode', # Adds clickable source code links
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster' # Clean default theme
html_static_path = ['_static']