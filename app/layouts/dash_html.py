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

    # Tabs Section
    dcc.Tabs([
        dcc.Tab(label='About Us', children=[
            html.Div([
                html.H2("About Us", style={'text-align': 'center'}),
                html.P(
                    """
                    Parkinson’s disease lacks effective disease-modifying therapies. 
                    We developed a cutting-edge patient-derived organoid platform combined with a Foundation Model-based network for PD therapy discovery.
                    """,
                    style={'font-family': 'Arial', 'font-size': '18px', 'margin': '20px', 'text-align': 'justify'}
                ),
                html.Div(
                    [
                        html.H4("Watch Our Introductory Video", style={'text-align': 'center', 'margin-top': '20px'}),
                        html.Div(
                            html.Iframe(
                                src="https://www.youtube.com/embed/4v35LQY1iuc",
                                style={
                                    'position': 'absolute',
                                    'top': 0,
                                    'left': 0,
                                    'width': '100%',
                                    'height': '100%',
                                    'border': 'none',
                                }
                            ),
                            style={
                                'position': 'relative',
                                'padding-bottom': '50%',  # Slightly modified aspect ratio
                                'height': 0,
                                'overflow': 'hidden',
                                'width': '80%',  # Decreased from 90% to 80%
                                'margin': '0 auto',
                                'margin-top': '20px',
                            }
                        )
                    ],
                    style={'text-align': 'center', 'margin-top': '30px'}
                )
            ])
        ]),
        dcc.Tab(label='Browser', children=[
            html.Div([
                html.H2("Network Browser", style={'text-align': 'center'}),
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
        ]),
        dcc.Tab(label='Team', children=[
            html.Div([
                html.H2("Our Team", style={'text-align': 'center'}),
                html.P(
                    """
                    Meet the innovative team behind the Foundation Model-Based Organoid Networks for CNS Drug Discovery.
                    We are a diverse group of researchers and engineers passionate about advancing neurodegenerative disease treatments.
                    """,
                    style={'font-family': 'Arial', 'font-size': '18px', 'margin': '20px'}
                ),
                # Add team members here if needed with additional HTML content
            ])
        ])
    ])
])
