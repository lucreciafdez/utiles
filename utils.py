import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Div(
                            [html.H6("Deep Legal")],
                            className="seven columns main-title",
                    ),
                    html.A(
                        html.Button("Descargar PDF", id="learn-more-button"),
                        href="javascript: w= window.print(); w.close(); ",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Proveedores Artículos Escolares")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Vista completa",
                                href="/dash-financial-report/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "General",
                href="/dash-financial-report/overview",
                className="tab first",
            ),
            dcc.Link(
                "Precios y comportamiento",
                href="/dash-financial-report/price-performance",
                className="tab",
            ),
            dcc.Link(
                "Portafolio y gerencia",
                href="/dash-financial-report/portfolio-management",
                className="tab",
            ),
            dcc.Link(
                "Tarifas", href="/dash-financial-report/fees", className="tab"
            ),
            dcc.Link(
                "Distribución",
                href="/dash-financial-report/distributions",
                className="tab",
            ),
            dcc.Link(
                "Noticias y comentarios",
                href="/dash-financial-report/news-and-reviews",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
