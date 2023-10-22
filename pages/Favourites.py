import dash
from dash import dcc, html, Output, Input, State,  callback
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/favourites')


CONTENT_STYLE = {
    "margin-left": "6rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

layout = html.Div(
    [
        dcc.Location(id="lurl", refresh=False),
        dbc.Breadcrumb(
                items=[
                    {"label": "Home", "href": "/", "external_link": True},
                    {"label": "Favourites", "href": "/favourites", "active": True},
                    
    ], id = "fav-path"
),
           
    ], style=CONTENT_STYLE
)

