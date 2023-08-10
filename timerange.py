from dash import Dash, Input, Output, dcc, html, callback, State
import datetime

app = Dash()

app.layout = html.Div(children = [
    dcc.DatePickerRange(
        id='picker',
        min_date_allowed=datetime.date(year=2023,month=7, day=1),
        max_date_allowed=datetime.date(year=2023, month=8, day=1),
    ),
])


@app.callback(
    Output('picker', 'max_date_allowed'),
    Input('picker', 'min_date_allowed'),
)
def init_end_date(_):
    return datetime.datetime.now().date()

@app.callback(
    Input('picker', 'start_date'),
    Input('picker', 'end_date'),
)
def on_event(start_date, end_date):
    pass


app.run(debug=True)