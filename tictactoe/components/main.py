from reactpy import component, html, run

def cell_style():
    return {
        "style": {
            "width": "3em",
            "height": "3em",
            "border": "5px solid red",
        },
    }

def table_style():
    return {
        "style": {
            "text-align": "center",
        },
    }


@component
def Main():
    GRID_HEIGHT = 3
    GRID_WIDTH = 3

    return (html.div(
        html.h1("XoXoXo"),
        Grid(GRID_HEIGHT, GRID_WIDTH, "*"),
        InputBox
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


run(Main)

# TODO:
# - can components inherit props? (for the value)