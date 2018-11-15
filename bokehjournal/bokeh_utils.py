import bokeh

BOKEH_URL = 'https://cdn.pydata.org/bokeh/release/bokeh-{}.min.{}'

def get_bokeh_src():
    ver = bokeh.__version__
    link = BOKEH_URL.format(ver,'css')
    js = BOKEH_URL.format(ver, 'js')

    return link, js