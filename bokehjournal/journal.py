import webbrowser

import dominate
import bokeh_utils as bu
from dominate.tags import link, script, p, h1, h2, h3, ul, li, style, br, a
from dominate.util import raw
from bokeh.embed import components

class Journal:
    def __init__(self, title, css='splendor'):
        self.doc = dominate.document(title=title)
        self.has_widgets = False
        self.has_tables = False

        with self.doc.head:
            link(rel='stylesheet', href=Journal.css[css], type='text/css')

            # bokeh css/js
            link_href, js_src = bu.get_bokeh_src()
            link(rel='stylesheet', href=link_href, type="text/css")
            script(type='text/javascript', src=js_src)

            # css to center the bokeh plots
            style("""
            div.bk-grid {
                margin: auto;
                width: 50%;
            }

            div.bk-plot-layout {
                margin: auto;
                width: 50%;
            }

            div.bk-root {
                margin: auto;
                width: 50%;
            }

            div.bk-canvas-wrapper {
                margin: auto;
                width: 50%;
            }
            """)




    def append_paragraph(self, text):
        with self.doc.body:
            p(text)

    def append_h1(self, text):
        with self.doc.body:
            h1(text)

    def append_h2(self, text):
        with self.doc.body:
            h2(text)

    def append_h3(self, text):
        with self.doc.body:
            h3(text)

    def append_a(self, text, href):
        with self.doc.body:
            a(text, href=href)

    def append_list(self, *items):
        with self.doc.body:
            with ul() as unorderedList:
                for item in items:
                    if type(item) is list:
                        self.append_list(*item)
                    else:
                        li(item)

    def append_br(self, num=1):
        with self.doc.body:
            for _ in range(num):
                br()

    def append_bokeh(self, figure):
        js, div = components(figure)

        with self.doc.head:
            raw(js)

        with self.doc.body:
            raw(div)

    def append_chartify(self, chart):
        self.append_bokeh(chart.figure)

    def save(self, file_path):
        with open(file_path, 'w') as f:
            print(self.doc.render(), file=f)

    def show(self, where='new_window'):
        self.save('output.html')
        new_settings = ['current_window', 'new_tab', 'new_window']

        if where not in new_settings:
            raise ValueError('Invalid "where" value. Should be {}'.format(new_settings))

        webbrowser.open('./output.html', new=new_settings.index(where))


    css = {
        'splendor': "https://cdn.jsdelivr.net/gh/markdowncss/splendor/css/splendor.min.css",
        'retro': "https://cdn.jsdelivr.net/gh/markdowncss/retro/css/retro.css",
        'modest': "https://cdn.jsdelivr.net/gh/markdowncss/air/css/splendor.min.css",
    }



