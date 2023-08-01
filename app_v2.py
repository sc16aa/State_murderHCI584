
# Import packages
from dash import Dash, dash_table, dcc, callback, Output, Input, html
import pandas as pd
import plotly.express as px


# Incorporate data
df = pd.read_csv('StateAggregates.csv') #for chloro map
table_df = pd.read_csv('filtered.csv') #for table data
# print(df)

# Initialize the app
app = Dash(__name__)

# App layout

app.layout = html.Div([
    
    html.H1("Exonerated from Prison: Names and Data", style={'text-align': 'center'}),
    html.Br(),
    
    dcc.RadioItems(options=['AvgAge', 'AvgDurationYrs', 'DNAprob', 'NumInmates', 'MajRace'], value = 'AvgAge',
                   inline=True, 
                   id='radio-buttons',
                   style={'color': 'Black', 'font-size': 20}),
    
    html.Br(),
    
    dcc.Graph(figure={}, id = 'graph-output'), #getting weird error figure is an array not object
    html.Br(),
    
    html.H2('Full List of those Convicted but Later Found Innocent', style = {'text-align':'center'}),
   
    dash_table.DataTable(data = table_df.to_dict('records'), 
                                        page_size=99999,
                                        #virtualization=True,   
                                        style_table={'overflowy': 'auto', 
                                                     'height':500,
                                                     }
    )
])    


# Combining Plotly graphs with the Dash html components

@callback(
    Output(component_id='graph-output', component_property='figure'),
    [Input(component_id='radio-buttons', component_property='value'),
     Input(component_id="radio-buttons-Table",component_property='children')]
)



def update_graph(value):   #value to return differnt maps
    fig = px.choropleth(
        data_frame= df,
        locations= 'ST',
        locationmode='USA-states',
        scope="usa",
        color = value,
        hover_data=['ST', value],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        template='plotly_dark'
    )    
    
    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
