from dash import html

import pandas as pd
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px
import matplotlib.colors as mcolors


def update_plot(data, annotations):
    def callback(gene_search, color_scale, selected_data, current_figure):
        # Default color to gray
        data['color'] = 'gray'

        # Define the column that contains gene names
        gene_column = data.columns[0]

        # Ensure the gene names column contains strings
        data[gene_column] = data[gene_column].astype(str)

        # Coloring based on different columns
        if color_scale == 'log2foldChange':
            # Gradient coloring for 'log2foldChange'
            norm_fc = (data['log2foldChange'] - data['log2foldChange'].min()) / (data['log2foldChange'].max() - data['log2foldChange'].min() + 1e-9)
            data['color'] = px.colors.sample_colorscale('RdBu', norm_fc)

        elif color_scale == 'cluster':
            # Get unique clusters and create a color map
            unique_clusters = data['cluster'].unique()
            palette = sns.color_palette("hsv", len(unique_clusters))
            hex_palette = [mcolors.to_hex(c) for c in palette]
            color_map = {cluster: hex_palette[i] for i, cluster in enumerate(unique_clusters)}
            data['color'] = data['cluster'].map(color_map)

        elif color_scale in ['sig', 'sig_DN', 'sig_lrrk2', 'sig_gba1', 'sig_gba1_gl']:
            # Color by significance columns
            color_map = {1: 'red', 0: 'gray', -1: 'blue'}
            data['color'] = data[color_scale].map(color_map)

        # Create or reuse the figure
        if current_figure:
            fig = go.Figure(current_figure)
            fig.update_traces(marker=dict(color=data['color']))
        else:
            # Create a new figure with updated colors
            fig = go.Figure(data=go.Scatter(
                x=data['x'],
                y=data['y'],
                mode='markers',
                marker=dict(color=data['color'], size=4, opacity=0.75),
                hovertext=data[gene_column],
                hoverinfo='text'
            ))

        # Add annotations only if the figure is new
        if not current_figure:
            for _, row in annotations.iterrows():
                fig.add_annotation(
                    x=row['x'],
                    y=row['y'],
                    text=row['label'],
                    showarrow=False,
                    font=dict(
                        color='#5F5F5F', size=18, family='Arial'
                    ),
                    bordercolor='black',
                    borderwidth=2,
                    bgcolor="rgba(255, 255, 255, 0.7)",
                    borderpad=4
                )

        # Initialize the list of genes to display
        gene_list_items = []
        selected_count = 0

        # Handle lasso selection with filtering
        if selected_data and 'points' in selected_data:
            selected_genes = [
                pt.get('hovertext', None) for pt in selected_data['points']
            ]
            # Filter out None values
            selected_genes = [gene for gene in selected_genes if isinstance(gene, str)]
            selected_count = len(selected_genes)

            if selected_genes:
                # Add selected points to the figure
                fig.add_trace(go.Scatter(
                    x=[pt['x'] for pt in selected_data['points']],
                    y=[pt['y'] for pt in selected_data['points']],
                    mode='markers+text',
                    marker=dict(color='green', size=10),
                    text=selected_genes,
                    textposition='top center'
                ))
                # Add selected genes to the list below the graph
                gene_list_items.extend([html.Li(gene) for gene in selected_genes])

        # Handle gene search input (now using the gene names)
        if gene_search:
            search_labels = [label.strip().lower() for label in gene_search.split(',')]
            if gene_column in data.columns:
                # Ensure the 'gene' column contains strings
                matched_labels = data[data[gene_column].str.lower().isin(search_labels)]

                if not matched_labels.empty:
                    fig.add_trace(go.Scatter(
                        x=matched_labels['x'], y=matched_labels['y'],
                        mode='markers+text',
                        marker=dict(color='red', size=10),
                        text=matched_labels[gene_column],
                        textposition='top center'
                    ))
                    # Add matched labels to the list
                    gene_list_items.extend([html.Li(label) for label in matched_labels[gene_column]])

        # Create the HTML list component with the selected count
        gene_list = html.Div([
            html.P(f"Selected Points: {selected_count}", style={'font-weight': 'bold'}),
            html.Ul(
                gene_list_items,
                style={
                    'overflow-y': 'scroll',
                    'height': '300px',
                    'margin-top': '10px',
                    'text-align': 'center'
                }
            )
        ])

        display_style = {
            'display': 'block', 'margin-top': '20px', 'text-align': 'center'
        } if gene_list_items else {'display': 'none'}

        # Adjust Y-axis range with padding
        y_min, y_max = data['y'].min(), data['y'].max()
        y_range = y_max - y_min
        new_y_min = y_min - 0.25 * y_range
        new_y_max = y_max + 0.25 * y_range

        # Update the layout of the figure
        fig.update_layout(
            title='',
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
