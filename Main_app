
# Import packages
from dash import Dash, dash_table, dcc, callback, Output, Input, html
import pandas as pd
import plotly.express as px


# Incorporate data
df = pd.read_csv('StateAggregates.csv') #for choro map
table_df = pd.read_csv('filtered.csv') #for table data
# print(df)

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    
    html.H1("Exonerated from Prison:", style={'text-align': 'center'}),
    html.Br(),
    
    dcc.RadioItems(options=['AvgAge', 'AvgDurationYrs', 'DNAprob', 'NumInmates', 'MajRace'], value='AvgAge',
                   inline=True, 
                   id='map_buttons',
                   style={'color': 'Black', 'font-size': 20}),
    dcc.Graph(figure={}, id='map_graph'),  

    html.Br(),

    dcc.RadioItems(options=['Race', 'Crime', 'ST', 'Age', 'Duration', 'DNA' ], value='Race', inline=True, id='bar_graph_buttons'),
    dcc.Graph(figure={}, id='bar_graph'),

    html.Br(),

    dash_table.DataTable(data = table_df.to_dict('records'), 
                                        page_size=99999,
                                        #virtualization=True,   
                                        style_table={'overflowy': 'auto', 
                                                     'height':500,},
                                        sort_action="native",
    )
])    

#https://community.plotly.com/t/dash-how-to-return-two-figures/70715/2

@callback(
    Output(component_id='map_graph', component_property='figure'),
    Output(component_id='bar_graph', component_property='figure'),
    
    # has to be in a list so we transmit both input values to update_graph!
    [Input(component_id='map_buttons', component_property='value'),
    Input(component_id='bar_graph_buttons', component_property='value')], # must use value here despite the arg called bar_graph_value later
)


 
def update_graph(map_value, bar_graph_value):    
    
    # use different color scale for each input
    color_dict = {'AvgAge':px.colors.sequential.YlOrRd,
                  'AvgDurationYrs':px.colors.sequential.YlGnBu,
                  'DNAprob': px.colors.sequential.YlGn,
                  'NumInmates': px.colors.sequential.RdPu, 
                  'MajRace': px.colors.qualitative.Set1}

    fig1 = px.choropleth(
        data_frame= df,
        locations= 'ST',
        locationmode='USA-states',
        scope="usa",
        color = map_value,
        hover_data=['ST', map_value],
        color_continuous_scale=color_dict[map_value],
        template='plotly_dark'
    )    

    fig2 = px.histogram(table_df, x=bar_graph_value)
    
    return fig1, fig2
 

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
