import dash
from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/lost_found')

CONTENT_STYLE = {
    "margin-left": "6rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

card = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src="/static/images/profile.png",
                        className="img-fluid rounded-start",
                    ),
                    className="",
                ),
            ],
            className="align-items-center",
        )
    ],
    className="mb-3",
    style={"maxWidth": "140px"},
)

carousel1 = dbc.Carousel(
    items=[
        {"key": "1", "src": "/static/images/wallet.png"},
        {"key": "2", "src": "/static/images/water.png"},
        {"key": "3", "src": "/static/images/laptop.png"},

    ],
    controls=False,
    indicators=True,
    interval=1500,
    ride="carousel",
    style = {'height':"400px"}
)


carousel2 = dbc.Carousel(
    items=[
      

        {"key": "4", "src": "/static/images/phone.png"},
        {"key": "5", "src": "/static/images/eyeglasses.png"},
        {"key": "6", "src": "/static/images/key.png"},
      
    ],
    controls=False,
    indicators=True,
    interval=1500,
    ride="carousel",
    style = {'height':"400px"}
)

carousel3 = dbc.Carousel(
    items=[
        
        {"key": "7", "src": "/static/images/school-bag.png"},
        {"key": "8", "src": "/static/images/atm-card.png"},
        {"key": "9", "src": "/static/images/idcard.png"},
    ],
    controls=False,
    indicators=True,
    interval=1500,
    ride="carousel",
    style = {'height':"400px"}
)

email_input = html.Div(
    [
        dbc.Label("Email", html_for="example-email"),
        dbc.Input(type="email", id="example-email", placeholder="Enter email"),
        html.Br(),
        dbc.Label("Contact Information", html_for="example-email"),
        dbc.Input(type="number", id="example-email", placeholder="Enter Contact Info."),
        html.Hr(),
        dbc.Label("Description", html_for="example-email"),
        dbc.Input(type="textarea", id="example-email", placeholder="Enter Description"),
        html.Br(),
        
        dbc.Button("Submit")

    ],
    className="mb-3",
)


form = dbc.Form([email_input])


upload = html.Div([
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Images')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    dbc.Button("Submit"),
    html.Div(id='output-image-upload'),
])




layout = html.Div(
    [
        dbc.Breadcrumb(
                items=[
                    {"label": "Home", "href": "/", "external_link": True},
                    {"label": "Explore", "href": "/explore","external_link":True},
                    {"label": "Lost & Found", "href": "/lost_found", "active": True},
                    
    ],
),
        
        dbc.Row([
            dbc.Col(dbc.Button("Found an Item",size="lg",style={"width":"100%","height":"250px","font-size":"40px","background-color":"#DA1B11"},id="found")),
             dbc.Col(dbc.Button("Lost an Item",size="lg",style={"width":"100%","height":"250px","font-size":"40px","background-color":"#DA1B11"},id="lost")),
             dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Found an Item")),
                dbc.ModalBody(upload),
            ],
            id="modal-found",
            size="lg",
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Lost an Item")),
                dbc.ModalBody(form),
            ],
            id="modal-lost",
            size = "lg",
        ),
            
                
                            

        ],style={"padding":"70px"}, className="g-1",),

        dbc.Row([
            dbc.Col(
            html.Div(carousel1,style={"align":"center","width":"300px"}),
            # width={"offset":4}
            ),
            dbc.Col(
            html.Div(carousel2,style={"align":"center","width":"300px"}),
            
            ),
            dbc.Col(
            html.Div(carousel3,style={"align":"center","width":"300px"}),
            
            ),
            
    ]),

#          dbc.Container(
#                 [
#                 dbc.Row(
#                         [
#                            dbc.Col([
                               
#                                     dbc.Card(
#     [
#         dbc.Row(
#             [
#                 dbc.Col(
#                     dbc.CardImg(
#                         src="/static/images/profile.png",
#                         className="img-fluid rounded-start",
#                     ),
#                     className="",
#                 ),
#             ],
#             className="align-items-center",
#         )
#     ],
#     className="mb-3",
#     style={"maxWidth": "140px"},
# ),



#                            ]), 
#                             dbc.Col([
                               
#                                     dbc.Card(
#     [
#         dbc.Row(
#             [
#                 dbc.Col(
#                     dbc.CardImg(
#                         src="/static/images/profile.png",
#                         className="img-fluid rounded-start",
#                     ),
#                     className="",
#                 ),
#             ],
#             className="align-items-center",
#         )
#     ],
#     className="mb-3",
#     style={"maxWidth": "140px"},
# ),



#                            ]), 
                        
#                             dbc.Col([
                               
#                                     dbc.Card(
#     [
#         dbc.Row(
#             [
#                 dbc.Col(
#                     dbc.CardImg(
#                         src="/static/images/profile.png",
#                         className="img-fluid rounded-start",
#                     ),
#                     className="",
#                 ),
#             ],
#             className="align-items-center",
#         )
#     ],
#     className="mb-3",
#     style={"maxWidth": "140px"},
# ),



#                            ]), 
                        
#                             dbc.Col([
                               
#                                     dbc.Card(
#     [
#         dbc.Row(
#             [
#                 dbc.Col(
#                     dbc.CardImg(
#                         src="/static/images/profile.png",
#                         className="img-fluid rounded-start",
#                     ),
#                     className="",
#                 ),
#             ],
#             className="align-items-center",
#         )
#     ],
#     className="mb-3",
#     style={"maxWidth": "140px"},
# ),



#                            ]), 
                         
                        
                        
                        
                        
#                         ],
#                     justify="start",align="center" )  ,
                    
#                 ]
#             ),

        
    ], style=CONTENT_STYLE
)

@callback(
    Output("modal-found", "is_open"),
    Input("found", "n_clicks"),
    State("modal-found", "is_open"),
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open


@callback(
    Output("modal-lost", "is_open"),
    Input("lost", "n_clicks"),
    State("modal-lost", "is_open"),
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open

def parse_contents(contents, filename, date):
    return html.Div([
         html.Hr(),
        html.H5(filename+" Uploaded Successfilly"),
        
        
        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        #html.Img(src=contents),
       
        
       
    ])

@callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'),
              State('upload-image', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
