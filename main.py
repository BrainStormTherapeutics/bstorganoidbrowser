import dash

from dash.dependencies import Input, Output, State

from app.utils.utils import load_gene_data, load_annotations, filter_valid_annotations
from app.layouts.dash_html import main_layout
from app.config import data_path, annotations_path
from app.controllers.callbacks import update_plot


data = load_gene_data(data_path)
annotations = filter_valid_annotations(load_annotations(annotations_path))

app = dash.Dash(__name__)
app.layout = main_layout

app.callback(
    [Output('tsne-plot', 'figure'), Output('gene-list', 'children'), Output('gene-list', 'style')],
    [Input('gene-search', 'value'), Input('color-scale', 'value'), Input('tsne-plot', 'selectedData')],
    [State('tsne-plot', 'figure')]
)(update_plot(data, annotations))


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
