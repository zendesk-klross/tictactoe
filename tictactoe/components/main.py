from reactpy import component, html, run, hooks

def cell_style():
    return {
        "style": {
            "width": "3em",
            "height": "3em",
            "border": "1px dotted black",
        },
    }

def table_style():
    return {
        "style": {
            "text-align": "center",
        },
    }

def form_style():
    return {
        "style": {
            "margin-top": "1em",
        },
    }

@component
def Main():
    GRID_HEIGHT = 3
    GRID_WIDTH = 3

    return (html.div(
        html.h1("XoXoXo"),
        Grid(GRID_HEIGHT, GRID_WIDTH, "*"),
        InputBox()
    ))


@component
def Grid(height, width, filler):
    def cell(value=""):
        return html.td(cell_style(), value)

    def row(cell_number, value):
        cells = [cell(filler)] * cell_number
        return html.tr(cells)

    def render_grid(row_number, cell_number, value):
        rows = [row(cell_number, value)] * row_number
        return html.table(table_style(), rows)

    return render_grid(height, width, filler)

@component
def InputBox():

    input_val, set_input_val = hooks.use_state('')
    form_state, set_form_state = hooks.use_state('')

    def on_change(event):
        set_input_val(event['target']['value'])

    def handle_submit(event):
        set_form_state("Form submitted")

    return html.div(
        html.form(
        {"on_submit": handle_submit},
        html.label({"htmlFor": "textField"}, "Make your move: "),
        html.input({
            "type": "text",
            "id": "textField",
            "name": "textField",
            "value": input_val,
            "onChange": on_change,
        }),
        html.input({
            "type": "submit"
        }),),
        html.p(input_val),
        html.p(form_state)
    )

run(Main)

# TODO:
# - can components inherit props? (for the value)

#  type="text"
#         value={inputValue}
#         onChange={(e) => setInputValue(e.target.value)}
#         placeholder="Enter something..."