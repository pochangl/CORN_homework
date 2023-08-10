from dash import Dash, Input, Output, dcc, html, callback, State


app = Dash()

app.layout = html.Div(children = [
    dcc.Dropdown(options=[], id='dropdown1'),
    html.Button(children='初始化按鈕', id='button', n_clicks=0),
    html.Button(children='讀取資料', id='button2', n_clicks=0),
    html.H1(id='output'),
])


@app.callback(
    Output('dropdown1', 'options'),
    Input('button', 'n_clicks'),
    prevent_initial_call=True,
)
def on_click(n_clicks):
    return ['物件1', '物件2', '物件3']


@app.callback(
    Output('output', 'children'),
    Input('button2', 'n_clicks'),
    State('dropdown1', 'value'),
)
def on_load(n_clicks, dropdown_value):
    return f'選擇了 {dropdown_value}'


app.run(debug=True)