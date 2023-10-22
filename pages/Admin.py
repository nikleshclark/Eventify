import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

dash.register_page(__name__, path='/admin')

CONTENT_STYLE = {
    "margin-left": "6rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
df = pd.read_csv("lost_data.csv")
fig = px.line(df,x="Date",y="Lost items")

card1 = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Found Item Inventory", className="card-title",style = {"font-size":"23px"}),
            html.P(
                "View Found Item Inventory"
                
            ),
        ]
    ),
    style={"width": "18rem"},
)
card2 = dbc.Card(
    dbc.CardBody(
        [
            html.H5("All Entries", className="card-title",style = {"font-size":"23px"}),
            html.P(
                "View all entries"
                
            ),
        ]
    ),
    style={"width": "18rem"},
)
card3 = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Lost Item Inquiry", className="card-title",style = {"font-size":"23px"}),
            html.P(
                "Show Inquires here"
                
            ),
        ]
    ),
    style={"width": "18rem"},
)

card4 = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Matching", className="card-title",style = {"font-size":"23px"}),
            html.P(
                "Show all Possible Matches"
                
            ),
        ]
    ),
    style={"width": "18rem"},
)


layout = html.Div(
    [
        dbc.Breadcrumb(
                items=[
                    {"label": "Home", "href": "/", "external_link": True},
                    {"label": "Admin", "href": "/admin", "active": True},
                    
    ],
),
 dbc.Container(
                [
                dbc.Row(
                        [
                            dbc.Col(html.Div(card1),width=3),
                            dbc.Col(html.Div(card2),width=3),
                            dbc.Col(html.Div(card3),width=3),
                            dbc.Col(html.Div(card4),width=3),
                            
                            
                        ],
                    justify="start",align="center")  ,

                dbc.Row(
                        [
                            dbc.Col(html.Div(
                                dcc.Graph(figure=fig),

                            ),width=8),
                            dbc.Col(html.Div(card2),width=4),
                            
                            
                            
                        ],
                    justify="start",align="center")
                    
                ]
            ),
    ], style=CONTENT_STYLE
)