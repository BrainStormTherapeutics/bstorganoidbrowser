from dash import dcc, html

main_layout = html.Div([
    html.H1(
        "t-SNE Plot with Gene Labels",
        style={
            'text-align': 'center',
            'font-family': 'Arial',
            'font-size': '32px'
        }
    ),

    # Wrapper Div with Flexbox layout for horizontal alignment
    html.Div([
        html.Div([
            html.Label(
                "Search for Genes (separate by commas):",
                style={
                    'font-family': 'Arial',
                    'font-size': '16px',
                    'margin-bottom': '5px'
                }
            ),
            dcc.Input(
                id='gene-search',
                type='text',
                placeholder='Enter genes...',
                debounce=True,
                style={
                    'width': '300px',
                    'height': '40px',
                    'font-size': '16px',
                    'padding': '5px',
                    'border-radius': '5px',
                    'border': '1px solid #ccc',
                    'box-sizing': 'border-box'
                }
            )
        ], style={
            'display': 'flex',
            'flex-direction': 'column',
            'align-items': 'flex-start',
            'margin-right': '20px'
        }),

        html.Div([
            html.Label(
                "Choose Color Scale:",
                style={
                    'font-family': 'Arial',
                    'font-size': '16px',
                    'margin-bottom': '5px'
                }
            ),
            dcc.Dropdown(
                id='color-scale',
                options=[
                    {'label': 'None', 'value': 'none'},
                    {'label': 'Significance (sig)', 'value': 'sig'},
                    {'label': 'FC Gradient', 'value': 'fc'}
                ],
                value='none',
                clearable=False,
                style={
                    'width': '300px',
                    'height': '40px',
                    'font-size': '16px',
                    'padding': '0',
                    'box-sizing': 'border-box'
                }
            )
        ], style={
            'display': 'flex',
            'flex-direction': 'column',
            'align-items': 'flex-start'
        })
    ], style={
        'display': 'flex',
        'justify-content': 'center',
        'align-items': 'center',
        'margin-bottom': '30px',
        'gap': '20px'
    }),

    # Graph Section
    dcc.Graph(
        id='tsne-plot',
        style={
            'margin': '0 auto',
            'width': '80%',
            'height': '800px'
        }
    ),

    # Gene List Section (hidden by default)
    html.Div(
        id='gene-list',
        style={
            'margin-top': '20px',
            'text-align': 'center',
            'font-family': 'Arial',
            'font-size': '16px',
            'display': 'none'
        }
    )
])
