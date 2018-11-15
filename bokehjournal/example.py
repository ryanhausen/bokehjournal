from journal import Journal
from bokeh.plotting import figure

journal = Journal('Example File')

journal.append_h1('Bokeh Journal')

journal.append_paragraph('Bokeh Journal is a tool to create HTML documents' +
                         'using python and bokeh. It currently supports:')

journal.append_list('h1', 
                    'h2', 
                    'h3', 
                    'ul (this for example)', 
                    'p', 
                    'br',
                    'and Bokeh plots')

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
p.line(x, y, legend="Temp.", line_width=2)
journal.append_bokeh(p)

journal.show()