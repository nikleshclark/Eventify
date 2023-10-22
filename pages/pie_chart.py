import dash
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px


dash.register_page(__name__, path='/pie_chart')

df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries

CONTENT_STYLE = {
    "margin-left": "6rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

datasource = dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Datasource")),
                dbc.ModalBody("Database: MySQL"),
            ],
            id="pie_datasource",
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
                        "label": "Pie Chart",
                        "active":True,
                    },
    ],
),

            html.H1('Sample Pie Chart',
                        style={'textAlign':'center'}),
            
                dbc.Container(
                [
                dbc.Row(
                        [
                            dbc.Col(dbc.Button("Download",id="pbtn_csv"),width=2),
                            dbc.Col(dbc.Button("FullScreen",id="fullscreen_pie"),width=2),
                            dbc.Col(dbc.Button("Data Source",id="datasource_pie"),width=2),
                            
                            
                        ],
                    justify="center" )  ,
                    
                ]
            ),

                dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Fullscreen modal")),
                dbc.ModalBody(dcc.Graph(id='piechart',
                         figure=px.pie(df, values='pop', names='country', title='Population of European continent'))),
            ],
            id="modal-pfs",
            fullscreen=True,
        ),
                datasource,


                # dbc.Button("Download",id = "btn_csv"),
                dcc.Download(id="download-dataframe-pie"),
                dcc.Graph(id='piechart',
                         figure=px.pie(df, values='pop', names='country', title='Population of European continent'))

    ], style=CONTENT_STYLE
)

@callback(
    Output("download-dataframe-pie", "data"),
    Input("pbtn_csv", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df.to_csv, "Server_count.csv")


@callback(
    Output("modal-pfs", "is_open"),
    Input("fullscreen_pie", "n_clicks"),
    State("modal-pfs", "is_open"),
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open

@callback(
    Output("pie_datasource", "is_open"),
    Input("datasource_pie", "n_clicks"),
    State("pie_datasource", "is_open"),
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open