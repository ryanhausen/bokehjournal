from journal import Journal
from bokeh.plotting import figure
import chartify

journal = Journal('Example File')

journal.append_h1('Bokeh Journal')

journal.append_paragraph('Bokeh Journal is a tool to create HTML documents' +
                         'using python and bokeh. It currently supports:')

journal.append_list('h1', 
                    'h2', 
                    'h3', 
                    'ul (this for example)', 
                    'p',
                    'a',
                    'br',
                    'and Bokeh plots')

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title="simple line example", 
           x_axis_label='x', 
           y_axis_label='y')
p.line(x, y, legend="Temp.", line_width=2)
journal.append_bokeh(p)

journal.append_paragraph('It also supports Spotify\'s Chartify library')

# From https://github.com/spotify/chartify/blob/master/examples/Examples.ipynb
data = chartify.examples.example_data()

ch  = chartify.Chart(blank_labels=True, x_axis_type='datetime')
ch.plot.scatter(
        data_frame=data,
        x_column='date',
        y_column='unit_price')
ch.set_title("Scatterplot")
ch.set_subtitle("Plot two numeric values.")

journal.append_chartify(ch)

journal.show()