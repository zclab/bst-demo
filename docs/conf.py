import datetime

project = "An example of bulma sphinx theme"
author = "zclab"
year = str(datetime.date.today().year)
copyright = year + " " + author
master_doc = "content"
language = "en"  #'zh_CN'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "sphinx_subfigure",
    "ablog",
    # "myst_parser",
    # "jupyter_sphinx",
    "myst_nb",
    "matplotlib.sphinxext.plot_directive",
]


myst_enable_extensions = ["colon_fence", "deflist"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.9", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "markdown_it": ("https://markdown-it-py.readthedocs.io/en/latest", None),
}

templates_path = ["_templates"]
html_additional_pages = {
    "index": "index.html"
}

html_static_path = ["_static"]
html_theme = "bulma_sphinx_theme"
html_title = "An example of bulma sphinx theme"
html_favicon = "_static/favicon.png"
html_last_updated_fmt = ""
html_logo = "_static/logo.svg"
html_show_sourcelink = True

todo_include_todos = True

# https://github.com/hung1001/font-awesome-pro-v6
# html_css_files = [
#     "https://cdn.jsdelivr.net/gh/duyplus/fontawesome-pro/css/all.min.css",
# ]
# fontawesome_included = True

html_theme_options = {
    "header_links_before_dropdown": 3,
    "navbar_color_style": "is-white",  # see styles: https://bulma.io/documentation/components/navbar/#colors
    "logo": {"text": "BST Demo", "logo": "_static/logo.svg"},
    "icon_links": [
        {
            "name": "Github",
            "url": "https://github.com/zclab/bulma-sphinx-theme",
            "svg": "github",
        },
        {
            "name": "Pypi",
            "url": "https://pypi.org/project/bulma-sphinx-theme/",
            "svg": "package",
        },
    ],
    "external_links": [
        {
            "name": "Pydata",
            "url": "https://pydata-sphinx-theme.readthedocs.io/en/latest/",
        },
        {"name": "Furo", "url": "https://pradyunsg.me/furo/quickstart/"},
        {
            "name": "Sphinx book theme",
            "url": "https://sphinx-book-theme.readthedocs.io/en/latest/",
        },
        {
            "name": "Hugging Face community",
            "url": "https://huggingface.co/docs/transformers/index",
        },
        {
            "name": " Docusaurus",
            "url": "https://docusaurus.io/",
        },
    ],
    "source_repository": "https://github.com/zclab/bst-demo",
    "source_branch": "main",
    "source_directory": "docs/",
    "use_edit_page_button": True,
    "have_top_navbar": True,
    "fix_navbar": False,
    "navbar_start": [],
    "navbar_end": ["navbar-nav.html", "theme-swither.html", "icon-links.html"],
    "light_colors":{
        "bst-color-background-sidenav":"rgb(255, 255, 255)",
    },
}

html_context = {"default_mode": "auto"}

blog_path = "blog"
blog_post_pattern = "examples/blog/*/*"
blog_authors = {
    "zclab": ("子川", "https://github.com/zclab"),
}
html_sidebars = {
    "examples/blog/*": [
        "sidenav-panel.html",
        "ablog/postcard.html",
        "ablog/recentposts.html",
        "ablog/tagcloud.html",
        "ablog/categories.html",
        "ablog/authors.html",
        "ablog/languages.html",
        "ablog/locations.html",
        "ablog/archives.html",
    ],
}
