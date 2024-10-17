from dash import html

import plotly.graph_objs as go
import plotly.express as px


def update_plot(data, annotations):
    """Update the t-SNE plot based on the input parameters."""
    def callback(gene_search, color_scale):

        data['color'] = 'black'

        # Coloring for 'sig'
        if color_scale == 'sig':
            color_map = {1: 'red', 0: 'gray', -1: 'blue'}
            data['color'] = data['sig'].map(color_map)

        # Coloring for 'fc'
        elif color_scale == 'fc':
            if data['fc'].max() == data['fc'].min():
                norm_fc = (data['fc'] - data['fc'].min())
            else:
                norm_fc = (data['fc'] - data['fc'].min()) / (data['fc'].max() - data['fc'].min())

            # Use RdBu colorscale for normalized values
            data['color'] = px.colors.sample_colorscale('RdBu', norm_fc)

        fig = go.Figure(data=go.Scatter(
            x=data['x'],
            y=data['y'],
            mode='markers',
            marker=dict(color=data['color'], size=4, opacity=0.75),
            hovertext=data['gene'],
            hoverinfo='text'
        ))

        for _, row in annotations.iterrows():
            fig.add_annotation(
                x=row['x'],
                y=row['y'],
                text=row['label'],
                showarrow=False,
                font=dict(color='red', size=14)
            )

        # Search input
        gene_list = []
        display_style = {'display': 'none'}

        if gene_search:
            search_genes = [gene.strip().lower() for gene in gene_search.split(',')]
            matched_genes = data[data['gene'].str.lower().isin(search_genes)]

            if not matched_genes.empty:
                fig.add_trace(go.Scatter(
                    x=matched_genes['x'], y=matched_genes['y'],
                    mode='markers+text',
                    marker=dict(color='red', size=10),
                    text=matched_genes['gene'],
                    textposition='top center'
                ))
                gene_list = html.Ul([html.Li(g) for g in matched_genes['gene']])
                display_style = {'display': 'block', 'margin-top': '20px', 'text-align': 'center'}

        # Adjust Y-axis range
        y_min, y_max = data['y'].min(), data['y'].max()
        y_range = y_max - y_min
        new_y_min = y_min - 0.25 * y_range
        new_y_max = y_max + 0.25 * y_range

        # Update layout with new axis range and styling
        fig.update_layout(
            title='t-SNE Plot with Gene Labels',
            title_font=dict(size=24, family='Arial'),
            xaxis_title='X axis',
            yaxis_title='Y axis',
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(
                showgrid=False,
                zeroline=False,
                range=[new_y_min, new_y_max]
            ),
            plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False
        )

        return fig, gene_list, display_style

    return callback
