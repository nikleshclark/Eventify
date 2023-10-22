import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/server_count')

CONTENT_STYLE = {
    "margin-left": "6rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

pcard = dbc.Card(
    [
        dbc.CardImg(src="/static/images/pie.png", top=True),
        dbc.CardBody(
            [
                html.H4("Pie Chart", className="card-title"),
                html.P(
                    "Redirect to the Pie Chart",
                    className="card-text",
                ),
                dbc.Button("Open Chart", color="primary",className="btn btn-secondary",href = "/pie_chart" ),
            ]
        ),
    ],
    
)
bcard = dbc.Card(
    [
        dbc.CardImg(src="/static/images/bar.png", top=True),
        dbc.CardBody(
            [
                html.H4("Bar Chart", className="card-title"),
                html.P(
                    "Redirect to the Bar Chart",
                    className="card-text",
                ),
                dbc.Button("Open Chart", color="primary",className="btn btn-secondary",href = "/bar_chart" ),
            ]
        ),
    ],
    
)
layout = html.Div(
    [
        dbc.Breadcrumb(
                items=[
                    {"label": "Home", "href": "/", "external_link": True},
                    {"label": "Explore", "href": "/explore",},
                    {"label": "Server Count",  "active": True},
                    
    ],
),
            dbc.Container(
                [
                dbc.Row(
                        [
                            dbc.Col(html.Div(pcard),width=4),
                            dbc.Col(html.Div(bcard),width=4),
                            
                            
                        ],
                    justify="start",align="center" )  ,
                    
                ]
            ),
    ], style=CONTENT_STYLE
)