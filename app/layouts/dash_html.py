from dash import dcc, html

main_layout = html.Div([
    # Header Section with BrainStorm ICON and Title
    html.Div([
        html.A(
            html.Img(
                src="https://cdn.prod.website-files.com/64a59756747dc7e6d278f5c3/64b5a1d57f2421194d49e869_BST-Logo.png",
                style={
                    'height': '60px',
                    'margin-right': '20px',
                    'vertical-align': 'middle'
                }
            ),
            href="https://www.brainstormtherapeutics.org/",
            target="_blank"  # Open the link in a new tab
        ),
        html.H1(
            "Leveraging Foundation Model-Based Organoid Networks for CNS Drug Discovery",
            style={
                'display': 'inline-block',
                'vertical-align': 'middle',
                'font-family': 'Arial',
                'font-size': '32px'
            }
        ),
    ], style={
        'display': 'flex',
        'align-items': 'center',
        'justify-content': 'center',
        'margin-bottom': '30px'
    }),

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
                    {'label': 'Gene Cluster', 'value': 'cluster'},
                    {'label': 'GBA1-PD vs WT, Organoid, Significance', 'value': 'sig'},
                    {'label': 'GBA1-PD vs WT, Organoid, FC Gradient', 'value': 'fc'}
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
        config={
            'displayModeBar': True,
            'modeBarButtonsToAdd': ['lasso2d', 'select2d'],
        },
        style={
            'margin': '0 auto',
            'width': '80%',
            'height': '800px'
        },
        clear_on_unhover=False,
        figure={}
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
