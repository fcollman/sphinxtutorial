Basic Sphinx Tutorial
---------------------

Some nice tutorials online
https://eikonomega.medium.com/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365

official docs https://www.sphinx-doc.org/en/master/usage/quickstart.html

Install sphinx dependancies
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a doc\_requirements.txt files in your repository. Add sphinx, and
sphinx plugins you want to use to list. (see
`doc\_requirements.txt <doc_requirements.txt>`__ in this repo).

1. sphinxcontrib-napoleon: allows use of doc strings that are in numpy
   or google format
2. sphinxcontrib-apidoc: helps generate documentation pages for your
   python modules

Install those requirements with pip or conda, best practice to do this
in a conda or virtual environment.

Run sphinx-quickstart
~~~~~~~~~~~~~~~~~~~~~

run sphinx-quickstart docs

from root of your repo. Will put all documentation related files in
docs/ subdirectory.

Answer questions as prompted. Will fill in values in various places. Can
replace those values in the files later if neeed.

In `docs/conf.py <docs/conf.py>`__ you will find configuration for your
docs. One immediate change is to uncomment these lines and modify them
to point up one directory to your repository root.

::

    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))

Next add extensions you want to use.

::

    extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.napoleon', 'sphinx_rtd_theme']

Change theme if you want... i've installed the read the docs theme,
added the extension and specified it. You can find more themes and
previews here https://sphinx-themes.org/.

::

    html_theme = 'sphinx_rtd_theme'

Create apidoc
~~~~~~~~~~~~~

Running this command will auto-generate rst pages for each of your
modules. If you add new modules you need to rerun this command to have
those pages captures.

::

    sphinx-apidoc -o docs/api sphinxparty

This placed all these files in the api subdirectory of your docs.

Now add a reference to this subdirectory to you index.rst table of
contents.

::

    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       api/modules

make a first version of documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

in doc subdirectory run

::

    make html

should produce a file in docs/\_build/html/index.html with your docs.

Write human readable documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create pages for key steps, such as installation, getting started, and
advanced topics that need explanation.

When writing pages you might want to create links, both inside
documentation and outside documentation. There is a large amount to
learn about how to write resturctured text. An overview can be found
here
https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

One extension to know about is sphinx-intersphinx
https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
This lets you create links to docs for other modules. You have to
specify for each module where that docs can be found. For example in
meshparty here are the relevant lines of conf.py

::

    intersphinx_mapping = {'trimesh':('https://trimsh.org/', None),
                       'networkx':('https://networkx.github.io/documentation/stable', None),
                       'scipy':('https://docs.scipy.org/doc/scipy/reference/', None)}

Now when writing documentation you can uses lines like this

::

    This module in scipy helps you do computations on sparse graphs :mod:`scipy.sparse.csgraph`

to reference external documentation. You should do the same thing when
referencing components of your own api within the documentation.

If you use the same rst format in docstrings, those will work as well
within the apidoc.

for example.. from
(render-python)[https://render-python.readthedocs.io/en/latest/api/renderapi.html#renderapi.tilespec.get\_tile\_spec]

Readme
~~~~~~

If you want to include your readme file in your documentation you have
to use the rst format, then you can reference and insert it dynamically
into your documentation like so.

::

    README
    ------
    .. include:: ../README.rst  

other extensions of note
~~~~~~~~~~~~~~~~~~~~~~~~

sphinx.ext.viewcode - Will create links to source code with autodoc.

sphinxcontrib.yt -  Plugin for inserting youtube videos into docs

`argschema <https://argschema.readthedocs.io/en/master/user/intro.html#sphinx-documentation>`__ - plugin for autodocumenting schemas from argschema

sphinx.ext.githubpages – Publish HTML docs in GitHub Pages

Publishing docs
~~~~~~~~~~~~~~~
readthedocs: https://docs.readthedocs.io/en/stable/intro/import-guide.html
This is my preferred method as it builds them for you as you check in new code.

githubpages: https://executableopinions.readthedocs.io/en/latest/labs/gh-pages/gh-pages.html
This is also an option but the config is complex and you have to maintain the builds yourself.

Example to look at
~~~~~~~~~~~~~~~~~~
render-python: https://github.com/AllenInstitute/render-python 
docs online at: https://render-python.readthedocs.io/en/latest/

render-modules: https://github.com/AllenInstitute/render-modules
docs online at: https://render-modules.readthedocs.io/en/latest/

MeshParty: https://github.com/sdorkenw/MeshParty
docs online at: https://github.com/sdorkenw/MeshParty

argschema: https://github.com/AllenInstitute/argschema
docs: https://argschema.readthedocs.io/en/master/