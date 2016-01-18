#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# complexity documentation build configuration file, created by
# sphinx-quickstart on Tue Jul  9 22:26:36 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# Get the project root dir, which is the parent dir of this
cwd = os.getcwd()
project_root = os.path.dirname(cwd)

# Insert the project root dir as the first element in the PYTHONPATH.
# This lets us ensure that the source package is imported, and that its
# version is used.
sys.path.insert(0, project_root)

# add the _ext/ dir for local extensions
sys.path.insert(1, os.path.abspath('_ext'))

# configure paths and names once
project_name = "wiki"
project_name_slug = "wiki"
project_orgname = "westurner"
project_twitter_user = project_orgname
project_author = u"Wes Turner"
project_copyright = u'@westurner 2014-2016, {}'.format(project_author)
project_github_path = "{}/{}".format(project_orgname, project_name)
project_github_url = "https://github.com/{}".format(project_github_path)
project_src_url = project_github_url
project_src_path = project_github_path
project_url = project_github_url
project_title = u'{}'.format(project_src_path)
project_description_oneline = (
    u'Documentation for the {} project'.format(project_name))
project_og_site_name = project_src_path  # e.g. westurner/dotfiles

srclink_project = project_github_url
srclink_src_path = ''
srclink_branch = 'master'

# current_git_branch=subprocess.check_output("git b") && parse

# import dotfiles

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings.
# They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    #'sphinxcontrib.napoleon',
    #'sphinxcontrib.ansi',
    #'sphinxcontrib.programoutput',
    #'sphinxcontrib.issuetracker',
    'sphinxcontrib.srclinks'
]

autodoc_member_order = 'bysource'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rest'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = project_name
copyright = project_copyright

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = None # dotfiles.__version__
# The full version, including alpha/beta/rc tags.
release = None # dotfiles.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ---------------------------------------------

# see: http://git.io/Pk7SGA
# on_rtd is whether we are on readthedocs.org, this line of code grabbed
# from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'basicstrap'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'lang': 'en',
    'nosidebar': False,
    'rightsidebar': False,
    'sidebar_span': 3,
    'nav_fixed_top': False,
    'nav_fixed': False,
    'nav_width': '900px',
    'content_fixed': False,
    'content_width': '768px',
    'row_fixed': False,
    'noresponsive': False,
    'noresponsiverelbar': True,
    'googlewebfont': False,
    'googlewebfont_url': 'http://fonts.googleapis.com/css?family=Lily+Script+One',
    'googlewebfont_style': u"font-family: 'Lily Script One' cursive;",
    'header_inverse': False,
    'relbar_inverse': False,
    'inner_theme': False,
    'inner_theme_name': 'bootswatch-readable',
#    'h1_size': '3.0em',
#    'h2_size': '2.6em',
#    'h3_size': '2.2em',
#    'h4_size': '1.8em',
#    'h5_size': '1.4em',
#    'h6_size': '1.1em',
}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project_title

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': [
        'localtoc.html',
        'relations.html',
        'searchbox.html',
        'srclinks.html',
        'links.html',
        ],
    'index': [
        'globaltoc.html',
        'relations.html',
        'searchbox.html',
        'srclinks.html',
        'links.html',
        ],
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Suffix for generated links to HTML files.
# The default is whatever html_file_suffix is set to;
# it can be set differently (e.g. to support different web server setups).
html_link_suffix = ''

# Filename affix
filename_affix = "{}".format(project_name_slug)

# Output file base name for HTML help builder.
htmlhelp_basename = '{}-doc'.format(filename_affix)



# -- Options for LaTeX output --------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index',
     '{}.tex'.format(filename_affix),
     project_title,
     project_author,
     'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index',
     project_name_slug,
     project_title,
     [project_author],
     1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index',
     project_name_slug,
     project_title,
     project_author,
     project_name,
     project_description_oneline,
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


def configure_meta_tags(app, pagename, templatename, context, doctree):
    metatags = context.get('metatags', '')
    metatags += """
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- OpenGraph metadata: ogp.me -->
    <meta property="og:title" content="{title}" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="{og_site_name}" />
    <!--
    <meta property="og:description" content="{description}" />
    -->
    <meta property="og:image" content="{og_image_url}" />
    <meta property="og:image:width" content="{og_image_width}" />
    <meta property="og:image:height" content="{og_image_height}" />
    <!--
    <meta property="og:image:secure_url" content="./_static/img/logo.png" />
    -->
    <!-- Twitter metadata -->
    <meta property="twitter:card" content="summary" />
    <meta property="twitter:title" content="{title}" />
    <meta property="twitter:description" content="{description}" />
    <meta property="twitter:site" content="{twitter_user}" />
    <meta property="twitter:creator" content="{twitter_user}" />
    """.format(
        title=context.get('title',''),
        description=context.get('description', project_description_oneline),
        og_site_name=project_og_site_name,
        og_image_url="",  # 470x242.png
        og_image_width="470",
        og_image_height="242",
        twitter_user=project_twitter_user)
    context['metatags'] = metatags

def setup(app):
    app.add_javascript('js/local.js')
    app.add_stylesheet('css/local.css')
    app.connect('html-page-context', configure_meta_tags)


if __name__ == "__main__":
    context = {}
    output = configure_meta_tags(None, None, None, context, None)
    print(context.get('metatags'))
