import dash
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px


dash.register_page(__name__, path='/bar_chart')

df = px.data.gapminder()

CONTENT_STYLE = {
    "margin-left": "6rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

datasource1 = dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Datasource")),
                dbc.ModalBody("Database: MySQL"),
            ],
            id="bar_datasource",
            size="sm",
            is_open=False,
        )


layout = html.Div(
    [
        dbc.Breadcrumb(
                items=[
                    {"label": "Home", "href": "/", "external_link": True},
                    {"label": "Explore", "href": "/explore", "external_link": True},
                    {"label": "Server Count", "href": "/server_count", "external_link": True},
                    {
                        "label": "Bar Chart",
                        "active":True,
                    },
    ],
),

            html.H1('Sample Bar Chart',
                        style={'textAlign':'center'}),

                dbc.Container(
                [
                dbc.Row(
                        [
                            dbc.Col(dbc.Button("Download",id="btn_csv"),width=2),
                            dbc.Col(dbc.Button("Full Screen",id="fullscreen_bar"),width=2),
                            dbc.Col(dbc.Button("Data Source",id="datasource_bar"),width=2),
                            
                            
                        ],
                    justify="center", className="g-0" )  ,
                    
                ]
            ),

                dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Fullscreen modal")),
                dbc.ModalBody(dcc.Graph(id='line-fig',
                  figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))),
            ],
            id="modal-fs",
            fullscreen=True,
        ),
                datasource1,
                dcc.Download(id="download-dataframe-csv"),
                dcc.Graph(id='line-fig',
                  figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))

    ], style=CONTENT_STYLE
)

@callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df.to_csv, "Server_count.csv")

@callback(
    Output("modal-fs", "is_open"),
    Input("fullscreen_bar", "n_clicks"),
    State("modal-fs", "is_open"),
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open


@callback(
    Output("bar_datasource", "is_open"),
    Input("datasource_bar", "n_clicks"),
    State("bar_datasource", "is_open"),
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open