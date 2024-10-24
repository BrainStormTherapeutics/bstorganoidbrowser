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

        # Coloring for 'sig'
        if color_scale == 'sig':
            color_map = {1: 'red', 0: 'gray', -1: 'blue'}
            data['color'] = data['sig'].map(color_map)

        # Coloring for 'fc'
        elif color_scale == 'fc':
            norm_fc = (data['fc'] - data['fc'].min()) / (data['fc'].max() - data['fc'].min() + 1e-9)
            data['color'] = px.colors.sample_colorscale('RdBu', norm_fc)

        # Coloring for 'cluster'
        elif color_scale == 'cluster':
             # Get unique clusters
            unique_clusters = data['cluster'].unique()

            # Generate a color palette for the number of unique clusters
            palette = sns.color_palette("hsv", len(unique_clusters))  # Or use 'tab10', 'Set2', etc.

            # Convert RGB tuples from the palette to hex format
            hex_palette = [mcolors.to_hex(c) for c in palette]

            # Create a mapping of each unique cluster to a color in hex format
            color_map = {cluster: hex_palette[i] for i, cluster in enumerate(unique_clusters)}

            # Assign colors to the 'color' column based on the cluster
            data['color'] = data['cluster'].map(color_map)
         

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
                hovertext=data['gene'],
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
                    bordercolor='black',  # Color of the square border
                    borderwidth=2,  # Thickness of the border
                    bgcolor="rgba(255, 255, 255, 0.7)",  # Background color with 0.7 alpha
                    borderpad=4  # Padding between the text and border
                )                

            # Load and add additional annotations from inputfile2.txt
            extra_annotations = pd.read_csv('app/files/scgpt_br_ft_sel_network_anno.txt', sep='\t')
            extra_annotations.columns = ['label', 'x', 'y']
            extra_annotations = extra_annotations.dropna()

            #for _, row in extra_annotations.iterrows():
            #    fig.add_annotation(
            #        x=row['x'],
            #        y=row['y'],
            #        text=row['label'],
            #        showarrow=False,
            #        font=dict(color='red', size=14)
            #    )

        # Initialize the list of genes to display
        gene_list_items = []
        selected_count = 0

        # Handle lasso selection with filtering
        if selected_data and 'points' in selected_data:
            selected_genes = [
                pt.get('hovertext', None) for pt in selected_data['points']
            ]
            # Filter out None values
            selected_genes = [gene for gene in selected_genes if gene]
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
                # Add matched genes to the list
                gene_list_items.extend([html.Li(g) for g in matched_genes['gene']])

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
