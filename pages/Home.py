import dash
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate


dash.register_page(__name__, path='/')

CONTENT_STYLE = {
    "margin-left": "6rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

jumbotron = html.Div(
    dbc.Container(
        [
            html.H2("Clark Application", className="text-light display-3"),
            html.P(
                "Harness your data. Discover opportunities. Elevate your insights.",
                className="text-light lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                dbc.NavLink(dbc.Button("Start Exploring", color="primary",className="btn btn-secondary"),href = "/explore"), className="lead"
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-dark rounded-3",
)

layout = html.Div(
    [
        html.H2("Home"),
                jumbotron,
                html.Br(),
                html.H2("Recents"),
                html.Hr(),
                html.Div(id="recents-url",children=[]),
    ], style=CONTENT_STYLE
)

