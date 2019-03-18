import codecs
import os
import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

html = '''
    <html lang="zh-cn">
    <head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type" />
    <link href="/static/default.css" rel="stylesheet">
    <link href="/static/github.css" rel="stylesheet">
    </head>
    <body>
    %s
    </body>
    </html>
    '''


def markdown_to_html(file):
    with codecs.open(file, mode='r', encoding='utf-8', errors='ignore') as f:
        # with codecs.open(os.path.join(os.getcwd(), "app/static/friendly.css"), mode='r', encoding='utf-8') as cssfile:
        body = f.read()

        # md = Markdown(extensions=['fenced_code',
        #                           'codehilite(css_class=highlight,linenums=None)',
        #                           'meta', 'admonition', 'tables'])
        # content = md.convert(body)
        # meta = md.Meta if hasattr(md, 'Meta') else {}
        content = markdown.markdown(body, output_format='html5', \
                                    extensions=['markdown.extensions.toc', \
                                                'markdown.extensions.sane_lists', \
                                                'markdown.extensions.codehilite', \
                                                'markdown.extensions.abbr', \
                                                'markdown.extensions.attr_list', \
                                                'markdown.extensions.def_list', \
                                                'markdown.extensions.fenced_code', \
                                                'markdown.extensions.footnotes', \
                                                'markdown.extensions.smart_strong', \
                                                'markdown.extensions.meta', \
                                                'markdown.extensions.nl2br', \
                                                'markdown.extensions.tables'])

    return html % content
