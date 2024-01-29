# Import required libraries
import pandas as pd
import dash 
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
wget = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
spacex_df = pd.read_csv(wget)
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)
#create the options for Launch Sites
launch_sites = []
launch_sites.append({'label':'All Sites','value':'All'})
for site in spacex_df['Launch Site'].unique().tolist():
    launch_sites.append({'label': site, 'value': site})

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                  dcc.Dropdown(id='site-dropdown', options=launch_sites, value='All', placeholder="Place holder here", searchable=True),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider', min=0, max=10000, step=1000,
                                                marks={0: '0',1000:'1000',2000:'2000',3000:'3000',4000:'4000',5000:'5000',6000:'6000',7000:'7000',8000:'8000',9000:'9000',10000:'10000'},
                                                value=[min_payload, max_payload]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'All':
        fig = px.pie(spacex_df, values='class',
                     names='Launch Site',
                     title='Total Success Launches by Site')
        return fig
    else:
        # return the outcomes piechart for a selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        site_df = filtered_df.groupby(['Launch Site', 'class']).size().reset_index(name='class count')
        fig = px.pie(site_df, values='class count', names='class',
                     title=f'Total Success Launches for site {entered_site}')
        return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='payload-slider', component_property='value'),
               Input(component_id='site-dropdown', component_property='value')])
def get_scatter_chart(payload_slider,entered_site):
    low, high = payload_slider
    slide = (spacex_df['Payload Mass (kg)'] > low) & (spacex_df['Payload Mass (kg)'] < high)
    df_slide = spacex_df[slide]
    if entered_site == 'All':
       fig1 = px.scatter(df_slide, x='Payload Mass (kg)', y='class', color="Booster Version Category",
                   title='Correlation between Payload and Success for all Sites')
       return fig1
    else:
        filtered_df1 = df_slide[df_slide['Launch Site'] == entered_site]
        fig1 = px.scatter(filtered_df1, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                    title=f'Correlation between Payload and Success for site {entered_site}')
        return fig1

# Run the app
if __name__ == '__main__':
    app.run_server()
