import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/explore')

CONTENT_STYLE = {
    "margin-left": "6rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
bcard = dbc.Card(
    [
        dbc.CardImg(src="/static/images/lostandfound.jpg", top=True,style={"height":"180px"}),
        dbc.CardBody(
            [
                html.H4("Lost & Found Items", className="card-title"),
                html.P(
                    "Redirect to Lost & Found site",
                    className="card-text",
                ),
                dbc.Button("Open Site", color="primary",className="btn btn-danger",href = "/lost_found" ),
            ]
        ),
    ]
    
)



card1= dbc.Card(
    [
        dbc.CardImg(src="/static/images/events.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Events Profile", className="card-title"),
                html.P(
                    "Find your Event Participation",
                    className="card-text",
                ),
                dbc.Button("Open Site", color="primary",className="btn btn-danger",href = "/events" ),
            ]
        ),
    ],
    
)

layout = html.Div(
    [
        dbc.Breadcrumb(
                items=[
                    {"label": "Home", "href": "/", "external_link": True},
                    {"label": "Explore", "href": "/explore", "active": True},
                    
    ],
),
 dbc.Container(
                [
                dbc.Row(
                        [
                            dbc.Col(html.Div(card1),width=3),
                            dbc.Col(html.Div(bcard),width=3),
                            
                            
                        ],
                    justify="start",align="center",style ={"height":"300px"} )  ,
                    
                ]
            ),
    ], style=CONTENT_STYLE
)