from dash import Dash, Input, Output, dcc, html, callback


app = Dash()

app.layout = html.Div(children = [
    dcc.DropDown(value=[], id='dropdown1'),
    html.Button(id='button', n_click=0)
])
@callback(
    Output('doropdown1', 'value'),
    Input('button', 'n_click'),
)

def on_click(n_click):
    return ['a', 'b', 'c']



app.run(debug=False)