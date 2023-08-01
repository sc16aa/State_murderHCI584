#Table Dashboard

# Import packages
from dash import Dash, dash_table, dcc, callback, Output, Input, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Incorporate data
df = pd.read_csv('filtered_with_latlong.csv')
print(df)


#map code
#Pretty sure I need to create an index to count the amount of people in each state 
fig = px.choropleth(
    data_frame = df,
    locationmode='USA-states',
    locations='ST',
    color= '#',
    hover_name='Name',
    hover_data=['Name', 'Crime', 'Sentence','County','Exonerated'],
    scope='usa',
    template='plotly_dark'
)

# Initialize the app
app = Dash(__name__)

# App layout
#This is the part I accidentally broke when I combined it with my map needs to be fixed
app.layout = html.Div([
    html.H1("Exonerated from Prison: Names and Data", style={'text-align': 'center'}),
    html.Br(),
    dcc.Graph(figure = fig),
    #space for table working on combinging them tomorrow (6/10)
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
    dcc.Graph(figure={}, id='controls-and-graph'),
    html.Div(id='output', children=[]),
    html.Br(),
    dcc.Graph(id='controls-and-graph', figure={})
])

# # Combining Plotly graphs with the Dash html components
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
