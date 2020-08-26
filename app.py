# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:45:29 2020

@author: yoges
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import dash_table
from dash.dependencies import Input, Output
import dash_daq as daq
from sim import Sim
import numpy as np

queue_size = 10000;
SToptions = [1.0, 3.0, 5.0]
IToptions = [3.0, 5.0, 7.0, 10.0]

ssq = Sim()
S, T, D = ssq.simulateSSQ(lam=3.0, b=5.0, size=queue_size)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
fig = px.line()
#print(fig)
app.layout = html.Div(children=[
    html.H1(
        children='Single Server Queue',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dbc.Card(dbc.Row([
                    dbc.Col([dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Label('Service Times (S)'),
                                        dcc.Dropdown(
                                            id='ST_select',
                                            options=[
                                                {'label': '1.0', 'value': 1.0},
                                                {'label': '3.0', 'value': 3.0},
                                                {'label': '5.0', 'value': 5.0}
                                            ],
                                            value=3.0
                                        ),
                                        html.Label('Interarrival Times (T)'),
                                        dcc.Dropdown(
                                            id='IT_select',
                                            options=[
                                                {'label': '1.0', 'value': 1.0},
                                                {'label': '3.0', 'value': 3.0},
                                                {'label': '5.0', 'value': 5.0}
                                            ],
                                            value=5.0
                                        ),
                                    ]
                                )
                        ),
                        html.Div(dash_table.DataTable(
                                id='data-table',
                                columns=(
                                    [{'id': 'type', 'name': 'Data Type'},
                                     {'id': 'mean', 'name': 'Mean'},
                                     {'id': 'std', 'name': 'Standard Deviation'}]
                                ),
                                data=[]
                            ),
                            style={'margin': '15px'}
                        )], 
                        width = 4, 
                        align = 'center'
                    ),
                    dbc.Col([daq.BooleanSwitch(
                              id='histogram_switch',
                              label="Histogram",
                              on=False
                            ),
                            dcc.Graph(
                                id='Graph1',
                                figure = fig, 
                                config = {'displayModeBar': False}
                            )], 
                            width=8
                    )
            ]), style = {'margin':'2px'}
    )
])
    
@app.callback(
    [Output(component_id='Graph1', component_property='figure'),
     Output(component_id='ST_select', component_property='options'),
     Output(component_id='IT_select', component_property='options'),
     Output(component_id='data-table', component_property='data')],
    [Input(component_id='histogram_switch', component_property='on'),
     Input(component_id='ST_select', component_property='value'),
     Input(component_id='IT_select', component_property='value')]
)
def update_graph(isHistogram, st_val, it_val):
    S, T, D = ssq.simulateSSQ(lam=st_val, b=it_val, size=queue_size)
    if isHistogram:
        fig = px.histogram(x=[i for i in range(queue_size)], y=D, nbins=100, title='Delay of a Single Server Queue', labels={'x': "N", 'y': "D<sub>n</sub>"})
    else:
        fig = px.line(x=[i for i in range(queue_size)], y=D, title='Delay of a Single Server Queue', labels={'x': "N", 'y': "D<sub>n</sub>"})
    fig.update_layout(xaxis_showgrid=False, yaxis={'gridcolor': '#dddddd'}, plot_bgcolor='white')
    return fig, getOptions(SToptions, st_val), getOptions(IToptions, it_val), getTableData(S, T, D)

def getOptions(optionsList, val):
    options=[{'label': str(option), 'value': option, 'disabled': val == option} for option in optionsList]
    return options

def getTableData(S, T, D):
    return [{'type': 'Service Time', 'mean': round(np.mean(S), 2), 'std': round(np.std(S), 2)},
            {'type': 'Interarrival Time', 'mean': round(np.mean(T), 2), 'std': round(np.std(T), 2)},
            {'type': 'Delay', 'mean': round(np.mean(D), 2), 'std': round(np.std(D), 2)}]
if __name__ == '__main__':
    app.run_server(debug=True)