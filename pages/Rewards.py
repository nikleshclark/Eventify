import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/rewards')

CONTENT_STYLE = {
    "margin-left": "6rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

layout = html.Div(
    [
        dbc.Breadcrumb(
                items=[
                    {"label": "Home", "href": "/", "external_link": True},
                    {"label": "Explore", "href": "/explore","external_link":True},
                    {"label": "Events", "href": "/events","external_link":True},
                    {"label": "Claim Rewards", "href": "/rewards", "active": True},
                    
    ],
),
        
    ], style=CONTENT_STYLE
)