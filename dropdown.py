from dash import Dash, Input, Output, dcc, html, callback


app = Dash()

app.layout = html.Div(children = [
    dcc.Dropdown(value=[], id='dropdown1'),
    html.Button(children: '按鈕', id='button', n_clicks=0)
])


@app.callback(
    Output('doropdown1', 'value'),
    Input('button', 'n_clicks'),
)
def on_click(n_clicks):
    return ['物件1', '物件2', '物件3']



app.run(debug=False)