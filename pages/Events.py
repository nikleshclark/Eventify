import dash
import plotly.express as px
import pandas as pd
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import datetime
from plotly_calplot import calplot
import plotly.graph_objects as go
import numpy as np
import pymongo



mongodb_url = "mongodb://localhost:27017/"  # MongoDB connection URL
database_name = "Events"  # Name of your database
collection_name = "Attended_events"  # Name of your collection


client = pymongo.MongoClient(mongodb_url)
database = client[database_name]
collection = database[collection_name]


def All_events(name):
    mongodb_url = "mongodb://localhost:27017/"  # MongoDB connection URL
    database_name = "Events"  # Name of your database
    collection_name = name  # Name of your collection

    
    client = pymongo.MongoClient(mongodb_url)
    database = client[database_name]
    collection = database[collection_name]

# Fetch all documents with "Event Name"
    events = collection.find({"Event Name": {"$exists": True}})
    categories = collection.find({"Category": {"$exists": True}})
    dates = collection.find({"Date": {"$exists": True}})
    rewards = collection.find({"Rewards": {"$exists": True}})
    result = []
    # Loop through the results and print the event names
    for event,cat,dat,re in zip(events,categories,dates,rewards):
        #event_name = event["Event Name"]
        result.append((event['Event Name'],cat['Category'],dat['Date'],re['Rewards']))
    client.close()
    return result

# def Regi_events(name='Registered_events'):
#     mongodb_url = "mongodb://localhost:27017/"  # MongoDB connection URL
#     database_name = "Events"  # Name of your database
#     collection_name = name  # Name of your collection

    
#     client = pymongo.MongoClient(mongodb_url)
#     database = client[database_name]
#     collection = database[collection_name]

# # Fetch all documents with "Event Name"
#     events = collection.find({"Event Name": {"$exists": True}})
#     categories = collection.find({"Category": {"$exists": True}})
#     dates = collection.find({"Date": {"$exists": True}})
#     rewards = collection.find({"Rewards": {"$exists": True}})
#     result = []
#     # Loop through the results and print the event names
#     for event,cat,dat,re in zip(events,categories,dates,rewards):
#         #event_name = event["Event Name"]
#         result.append((event['Event Name'],cat['Category'],dat['Date'],re['Rewards']))
#     client.close()
#     return result

# def Atte_events():
#     pass



dash.register_page(__name__, path='/events')

CONTENT_STYLE = {
    "margin-left": "6rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

df = px.data.tips()
#fig = px.pie(df, values='tip', names='day',title='Events attended',template="plotly_dark",hole=0.8)

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 15,
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {
        'bar': {'color':'#0096FF'}
    }
    ))
fig.update_layout(
    margin=dict(
        l=20,
        r=25,
        b=10,
        t=5,
     
    ),
    title_text='Events attended', title_x=0.5,title_y=0.05
   # paper_bgcolor = "grey"
 )


def Display_gauge(value):
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = value,
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {
        'axis': {'range': [None, 15]},
        'bar': {'color':'#0096FF'}
    }
    ))
    fig.update_layout(
        margin=dict(
            l=20,
            r=25,
            b=10,
            t=15,
        
        ),
        title_text='Events attended', title_x=0.5,title_y=0.05
    # paper_bgcolor = "grey"
    )
    return fig




# list_group = dbc.ListGroup(
#     [
        
        
#         dbc.ListGroupItem([html.P("Event A"),
#                            html.Small(
#                                 ["24 October 2023 Category: ",dcc.Link("Science",href='/')],
#                                 className="card-text text-muted",
#                             ),]),
#         dbc.ListGroupItem([html.P("Event B"),
#                            html.Small(
#                                 ["24 October 2023 Category: ",dcc.Link("Community",href='/')],
#                                 className="card-text text-muted",
#                             ),]),
#         dbc.ListGroupItem("Event A"),
#         dbc.ListGroupItem("Event B"),
#         dbc.ListGroupItem("Event A"),
#         dbc.ListGroupItem("Event B"),
#     ]
# )


list_group_items = []
x = All_events("All_events")
y = All_events("Registered_events")
z = All_events("Attended_events")
# Loop through the results and create dbc.ListGroupItems
def Generate_all(x):
    list_group_items=[]
    for event in x:
        event_name = event[0]

        category = event[1]
        date = event[2]
        rewards = event[3]
        
        list_group_items.append(
            dbc.ListGroupItem([
                html.P(event_name),
                html.Small(["Category : ",dcc.Link(category, href='/')]),
                html.Br(),
                html.Small(
                    [date + " Rewards: "+rewards],
                    className="card-text text-muted",
                ),
            ])
        )
    return list_group_items

def Generate_registered(x):
    list_group_items=[]
    for event in x:
        event_name = event[0]

        category = event[1]
        date = event[2]
        rewards = event[3]
        
        list_group_items.append(
            dbc.ListGroupItem([
                html.P(event_name),
                html.Small(["Category : ",dcc.Link(category, href='/')]),
                html.Br(),
                html.Small(
                    [date + " Rewards: "+rewards],
                    className="card-text text-muted",
                ),
            ])
        )
    return list_group_items

def Generate_attended(x):
    list_group_items=[]
    for event in x:
        event_name = event[0]

        category = event[1]
        date = event[2]
        rewards = event[3]
        
        list_group_items.append(
            dbc.ListGroupItem([
                html.P(event_name),
                html.Small(["Category : ",dcc.Link(category, href='/')]),
                html.Br(),
                html.Small(
                    [date + " Rewards: "+rewards],
                    className="card-text text-muted",
                ),
               
            ])
        )
    return list_group_items



for event in x:
    event_name = event[0]

    category = event[1]
    date = event[2]
    rewards = event[3]
    
    list_group_items.append(
        dbc.ListGroupItem([
            html.P(event_name),
            html.Small(["Category : ",dcc.Link(category, href='/')]),
            html.Br(),
            html.Small(
                [date + " Rewards: "+rewards],
                className="card-text text-muted",
            ),
        ])
    )

# Create the dbc.ListGroup with the list of items
All_eve = dbc.ListGroup(list_group_items)
y1 = []
for event in y:
    event_name = event[0]

    category = event[1]
    date = event[2]
    rewards = event[3]
    
    y1.append(
        dbc.ListGroupItem([
            html.P(event_name),
            html.Small(["Category : ",dcc.Link(category, href='/')]),
            html.Br(),
            html.Small(
                [date + " Rewards: "+rewards],
                className="card-text text-muted",
            ),
        ])
    )

# Create the dbc.ListGroup with the list of items
Reg_eve = dbc.ListGroup(y1)
z1 = []
for event in z:
    event_name = event[0]

    category = event[1]
    date = event[2]
    rewards = event[3]
    
    z1.append(
        dbc.ListGroupItem([
            html.P(event_name),
            html.Small(["Category : ",dcc.Link(category, href='/')]),
            html.Br(),
            html.Small(
                [date + " Rewards: "+rewards],
                className="card-text text-muted",
            ),
        ])
    )

# Create the dbc.ListGroup with the list of items
Att_eve = dbc.ListGroup(z1)



dummy_start_date = "2023-01-01"
dummy_end_date = "2023-12-31"
dummy_df = pd.DataFrame(
    {
        "ds": pd.date_range(dummy_start_date, dummy_end_date),
        "value": 3,
    }
)
dummy_df.loc[dummy_df["ds"] == "10/21/23", "value"] = 10
cal = calplot(dummy_df, x="ds", y="value",
              name="Events",
              dark_theme=False,
              gap = 4,
    month_lines_width=3,     
    month_lines_color="#fff")

def Display_Cal(dummy_df):
    cal = calplot(dummy_df, x="ds", y="value",
              name="Events",
              dark_theme=False,
              gap = 4,
    month_lines_width=3, 
    colorscale="blues",    
    month_lines_color="#fff")
    return cal




card = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src="/static/images/profile.png",
                        className="img-fluid rounded-start",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Profile Name", className="card-title"),
                            html.Hr(),
                            html.P(
                                "Coins ",
                                className="card-text",
                            ),
                            dbc.NavLink([" 30 ",html.I(className='bi bi-coin')], href="/page-1", active="exact",id="coins"),
                            html.Br(),
                            dbc.Button("Edit Profile",className="rounded-pill"),
                            
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    style={"maxWidth": "540px"},
)



rewards = dbc.Card(
    [
        dbc.Row(
            [
               
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Badges", className="card-title"),
                            html.Hr(),
                            html.H5(
                                "Novice",
                                className="card-text",
                            ),
                            html.Br(),
                            dbc.Button("Claim Rewards",className="rounded-pill",href = "https://store.clarku.edu/cap-relaxed-twill-clark"),
                            
                            html.Br(),
                           
                            
                        ]
                    ),
                    className="col-md-8",
                ),
                 dbc.Col(
                    dbc.CardImg(
                        src="/static/images/rewards.png",
                        className="img-fluid rounded-start",
                    ),
                    className="col-md-4",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    style={"maxWidth": "540px"},
)


# df = pd.DataFrame(
#     {
#         "Name": ["Arthur", "Ford", "Zaphod", "Trillian"],
#         "Date": ["Dent", "Prefect", "Beeblebrox", "Astra"],
#         "Category": ["Dent", "Prefect", "Beeblebrox", "Astra"],
#     }
# )

#table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)


layout = html.Div([
    dbc.Breadcrumb(
                items=[
                    {"label": "Home", "href": "/", "external_link": True},
                    {"label": "Explore", "href": "/explore","external_link":True},
                    {"label": "Events", "href": "/events", "active": True},
                    
    ],
),


    dbc.Row([
        dbc.Col(


            card,

            # dbc.Card(
            #     dbc.CardBody([
            #         dbc.Col(dash.html.Img(src="https://images.plot.ly/logo/new-branding/plotly-logomark.png",height = "30px")),
            #         dbc.Col([dash.html.H3("Name"),
            #                  dash.html.P("Coins: 100"),
            #         dbc.Button("Edit Profile")]),
            #         ]),
            #     className="mt-2 mb-3"
            # ),
            width=3, className="mt-2"
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dcc.Graph(id="graph",figure=fig,style = {'height':'200px'}),


                ]),
                className="mb-3 mt-2", 
            ),
             width=4 
        ),
        dbc.Col(
           rewards,
            width=5, className="mt-2"
        ),
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H5("All Events"),
                    html.Div(All_eve,id="all-list"),


                ]),
                className="mb-3"
            ),
        ]),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H5("Registered Events"),
                    html.Div(Reg_eve,id="registered-list"),


                ]),
                className="mb-3"
            ),
        ]),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H5("Attended Events"),
                    html.Div(Att_eve,id="attended-list"),


                ]),
                className="mb-3"
            ),
        ])

    ]),
    
    
    
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("15 Events Attended in this Year",id="events-count"),
                    dcc.Graph(figure=cal,id="calendar-c")]),
                
                className="mb-3"
            ),
        ),
    ]),
    
],  style=CONTENT_STYLE)

@callback([Output('graph', 'figure'),Output('coins','children'),Output('calendar-c','figure'),Output('events-count','children'),
           Output('all-list','children'),Output('registered-list','children'),Output('attended-list','children')
           
           ],
              [Input('url', 'pathname')])
def display_page(pathname):
    attended_events = All_events('Attended_events')
    all_events = All_events('All_events')
    registered_events = All_events('Registered_events')
    z = dbc.ListGroup(Generate_attended(attended_events))
    x = dbc.ListGroup(Generate_all(all_events))
    y = dbc.ListGroup(Generate_registered(registered_events))

    count = 0
    dummy_start_date = "2023-01-01"
    dummy_end_date = "2023-12-31"
    dummy_df = pd.DataFrame(
    {
        "ds": pd.date_range(dummy_start_date, dummy_end_date),
        "value": 3,
    }
        )
    
    for i in attended_events:
        count += int(i[3])
        dummy_df.loc[dummy_df["ds"] == i[2], "value"] = 20
    calendar = Display_Cal(dummy_df)
    coins = [str(count)+" ",html.I(className='bi bi-coin')]
    events_count = [str(len(attended_events))+" Events attended in this Year"]
    



    return [Display_gauge(len(attended_events)),coins,calendar,events_count,x,y,z]
    # if pathname == '/apps/app1':
    #      return app1.layout
    # elif pathname == '/apps/app2':
    #      return app2.layout
    # else:
    #     return '404'



# if __name__ == '__main__':
#     app.run_server(debug=True)
