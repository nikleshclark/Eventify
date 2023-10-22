import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc


app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
    name="Home", use_pages=True,
)
# app.config.suppress_callback_exceptions=True

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "5rem",
    "padding": "1rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "6rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
      
        dbc.Nav(
            [
                dbc.NavLink("logo", href="/",id='company',style={"color":"#DA1B11"}),
                dbc.NavLink(html.I(className='bi bi-house-door'), href="/", active="exact",id="home",style={"color":"#DA1B11"}),
                dbc.NavLink(html.I(className='bi bi-star'), href="/favourites", active="exact",id="fav",style={"color":"#DA1B11"}),
                dbc.NavLink(html.I(className='bi bi-clock-history'), href="/recents",active="exact",id='his',style={"color":"#DA1B11"}),
                dbc.NavLink(html.I(className='bi bi-people-fill'), href="/page-3",active="exact",id="user",style={"color":"#DA1B11"}),
                dbc.NavLink(html.I(className='bi bi-lightbulb'), href="/page-4",active="exact",id='idea',style={"color":"#DA1B11"}),
                html.Hr(),
                dbc.NavLink(html.I(className='bi bi-person-circle'), href="/page-5",id='acc',style={"color":"#DA1B11"}),
                dbc.NavLink(html.I(className='bi bi-app-indicator'), href="/page-6",id='apps',style={"color":"#DA1B11"}),
                dbc.NavLink(html.I(className='bi bi-compass'), href="/explore",id="explore",active="exact",style={"color":"#DA1B11"}),
            ],
            vertical=True,
            # pills=True, 
        ),
        dbc.Tooltip("Home",target="home"),
        dbc.Tooltip("Explore",target="explore"),
        dbc.Tooltip("Favourites",target="fav"),
        dbc.Tooltip("History",target="his"),
        dbc.Tooltip("Users",target="user"),
        dbc.Tooltip("Idea",target="idea"),
        dbc.Tooltip("Account",target="acc"),
        dbc.Tooltip("Apps",target="apps"),
    ],
    style=SIDEBAR_STYLE,
)

#content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    dcc.Store(id="recent-pages-store"),
    sidebar,
    dash.page_container
])





if __name__ == "__main__":
    app.run(debug=True)