from dataclasses import dataclass, asdict
from enum import Enum, auto
from dash import Dash, Input, Output, State, ctx, no_update
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],)


class ids(Enum):
    switch1 = auto()
    switch2 = auto()
    switch3 = auto()
    toggle_btn = auto()
    output1 = auto()
    output2 = auto()
    output3 = auto()
    output4 = auto()

    def id(self, index=None):
        if index is None:
            return dict(type=self.name, index=self.value)
        return dict(type=self.name, index=index)


app.layout = dbc.Container(
    [
        dbc.Row(dbc.Alert(ids.output1.name, id=ids.output1.id(), color="primary")),
        dbc.Row(dbc.Alert(ids.output2.name, id=ids.output2.id(), color="secondary")),
        dbc.Row(dbc.Alert(ids.output3.name, id=ids.output3.id(), color="warning")),
        dbc.Row(dbc.Alert(ids.output4.name, id=ids.output4.id(), color="danger")),
        dbc.Switch(id=ids.switch1.id(), label=ids.switch1.name, value=False),
        dbc.Switch(id=ids.switch2.id(), label=ids.switch1.name, value=False),
        dbc.Switch(id=ids.switch3.id(), label=ids.switch3.name, value=False),
        dbc.Button("Toggle", id=ids.toggle_btn.id()),
    ]
)


@app.callback(
    dict(
        output1=Output(ids.output1.id(), "color"),
        output2=Output(ids.output2.id(), "color"),
        output3=Output(ids.output3.id(), "color"),
        output4=Output(ids.output4.id(), "color"),
        output1_isopen=Output(ids.output1.id(), "is_open"),
        output2_isopen=Output(ids.output2.id(), "is_open"),
        output3_isopen=Output(ids.output3.id(), "is_open"),
        output4_isopen=Output(ids.output4.id(), "is_open"),
    ),
    dict(
        switch1=Input(ids.switch1.id(), "value"),
        switch2=Input(ids.switch2.id(), "value"),
        switch3=Input(ids.switch3.id(), "value"),
        toggle_btn=Input(ids.toggle_btn.id(), "n_clicks"),
        output1=State(ids.output1.id(), "color"),
        output2=State(ids.output2.id(), "color"),
        output3=State(ids.output3.id(), "color"),
        output4=State(ids.output4.id(), "color"),
        output1_isopen=State(ids.output1.id(), "is_open"),
        output2_isopen=State(ids.output2.id(), "is_open"),
        output3_isopen=State(ids.output3.id(), "is_open"),
        output4_isopen=State(ids.output4.id(), "is_open"),
    ),
)
def color_switcher(**kwargs):
    @dataclass
    class update:
        output1: ... = no_update
        output2: ... = no_update
        output3: ... = no_update
        output4: ... = no_update
        output1_isopen: ... = no_update
        output2_isopen: ... = no_update
        output3_isopen: ... = no_update
        output4_isopen: ... = no_update

    if ctx.triggered_id == ids.switch1.id():
        return asdict(update(output1=kwargs["output2"], output2=kwargs["output1"]))

    if ctx.triggered_id == ids.switch2.id():
        return asdict(update(output2=kwargs["output3"], output3=kwargs["output2"]))

    if ctx.triggered_id == ids.switch3.id():
        return asdict(update(output3=kwargs["output4"], output4=kwargs["output3"]))

    if ctx.triggered_id == ids.toggle_btn.id():
        return asdict(
            update(
                output1_isopen=not kwargs["output1_isopen"],
                output2_isopen=not kwargs["output2_isopen"],
                output3_isopen=not kwargs["output3_isopen"],
                output4_isopen=not kwargs["output4_isopen"],
            )
        )

    return asdict(update())


if __name__ == "__main__":
    app.run(debug=True)
