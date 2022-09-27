import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px




app = dash.Dash()
server = app.server
df = pd.read_csv('C:\\Users\\tombr\\Documents\\stockdata2.csv',  index_col=0, parse_dates=True)
df.index = pd.to_datetime(df['Date'])

fig = px.line(x =df["Date"], y= df["value"], color =df['stock'], template='none')
fig.update_layout(
    plot_bgcolor='#2f323A',
    paper_bgcolor='#2f323A',
    font_color="#1CA8DD"
)
data1 = dict(
    number=[39, 27.4, 20.6, 11, 2],
    stage=["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"])
fig1 = px.funnel(data1, x='number', y='stage')
fig1.update_layout(
    plot_bgcolor='#2f323A',
    paper_bgcolor='#2f323A',
    font_color="#1CA8DD"
)

app.layout = html.Div(
    html.Div(style={'backgroundColor': '#2f323A'},
             children=[
        html.Div(style={'backgroundColor': '#2f323A'},
            children=[
                html.P(children="🥑", className="header-emoji"),
                html.H1(
                    children="Avocado Analytics",
                        style ={"color": "#1CA8DD",
                       "margin": "4px auto",
                       "font": "roag",
                       "text-align": "center",
                       "max-width": "384px",
                       'backgroundColor':'#2f323A'
                            },
                ),
                html.P(
                    children="Analyze data moment"
                    " im still working this out",
                    style ={
                       "color": "#1CA8DD",
                       "font":  "roag",
                       "margin": "4px auto",
                       "text-align": "center",
                       "max-width": "384px",
                       'backgroundColor':'#2f323A'
                            },
                ),
            ],
            className="header",
        ),
        dcc.Graph(
           id='whats a going on',
           figure=fig
        ),
    html.Div(style={'backgroundColor': '#2f323A'},
             children=[
            dcc.Graph(
                id =  {"title": "This is ugly"},
             figure=fig1

        ),
       ]
      )
     ]
    ),
)

if __name__ == '__main__':
    app.run_server()

#2f323A background
#1CA8DD