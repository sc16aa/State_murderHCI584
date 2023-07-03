#Table Dashboard

# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('filtered.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data, Graph, and Controls'),
    html.Hr(),

    # CH: value must be an existing column, you had lifeExp which is not a valid column name
    dcc.RadioItems(options=['Race', 'Crime', 'ST', 'Age', 'Duration', 'DNA' ], value='Race', inline=True, id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), 
                                        page_size=99999,
                                        #virtualization=True, 
                                        fixed_rows={'headers': True},  
                                        style_table={'overflowY': 'auto', 
                                                     'height':500,
                                                     'overflow': 'hidden',
                                                     'textOverflow': 'ellipsis',
                                                     #'maxWidth': 0,
                                                     }
                        ),
    dcc.Graph(figure={}, id='controls-and-graph')
])

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)


def update_graph(col_chosen):
    fig = px.histogram(df, x=col_chosen)
    return fig

def updateTable(n):
     pass

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
