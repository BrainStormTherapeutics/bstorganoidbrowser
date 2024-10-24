from dash import dcc, html

main_layout = html.Div([
    # Header Section with BrainStorm ICON and Title
    html.Div([
        html.A(
            [
                html.Img(
                    src='assets/icon/BrainStormTherapeutics.jpg',
                    style={
                        'height': '60px',
                        'margin-right': '20px',
                        'vertical-align': 'middle'
                    }
                )
            ],
            href="https://www.brainstormtherapeutics.org/",
            target="_blank"
        ),
        html.H1(
            "Leveraging Foundation Model-Based Organoid Networks for CNS Drug Discovery",
            style={
                'display': 'inline-block',
                'vertical-align': 'middle',
                'font-family': 'Arial',
                'font-size': '32px'
            }
        )
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
                    html.Img(
                        src='assets/about_us/about_us_photo_1.png',
                        style={
                            'width': '80%',
                            'height': 'auto',
                            'margin': '0 auto',
                            'display': 'block',
                            'margin-bottom': '20px'
                        }
                    ),
                    style={'text-align': 'center', 'margin-bottom': '30px'}
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
                                'padding-bottom': '50%',
                                'height': 0,
                                'overflow': 'hidden',
                                'width': '80%',
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
                                {
                                    'label': 'None', 'value': 'none'
                                },
                                {
                                    'label': 'Cluster', 'value': 'cluster'
                                },
                                {
                                    'label': 'GBA1-PD vs WT, Whole organoid, FC Gradient',
                                    'value': 'log2foldChange'
                                },
                                {
                                    'label': 'GBA1-PD vs WT, Whole organoid, Significance',
                                    'value': 'sig'
                                },
                                {
                                    'label': 'PD vs WT, Dopamine Neuron-human brain, Significance',
                                    'value': 'sig_DN'
                                },
                                {
                                    'label': 'LRRK2-PD vs WT, Dopamine Neuron-Organoid, Significance',
                                    'value': 'sig_lrrk2'
                                },
                                {
                                    'label': 'GBA1-PD vs WT, Dopamine Neuron-Organoid, Significance',
                                    'value': 'sig_gba1'
                                },
                                {
                                    'label': 'GBA1-PD vs WT, Glia-Organoid, Significance',
                                    'value': 'sig_gba1_gl'
                                }
                            ],
                            value='none',
                            clearable=False,
                            style={
                                'width': '450px',
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
                html.Div([
                    html.Div([
                        html.Img(
                            src='https://cdn.prod.website-files.com/64a59756747dc7e6d278f60d/66d75d091b53f75930b05ceb_64b710a4ba09dff54ff3eb90_1544022458569_v2.jpg',
                            style={'width': '150px', 'height': '150px', 'object-fit': 'cover', 'border-radius': '50%'}

                        ),
                        html.H3("Dr. Robert Fremeau"),
                        html.H4("Founder and CSO"),
                        html.P("Experienced R&D leader with 20+ years experience in academia and industry.")
                    ], style={'text-align': 'center', 'margin-bottom': '40px'}),
                    html.Div([
                        html.Img(
                            src='https://cdn.prod.website-files.com/64a59756747dc7e6d278f60d/66d75ad294a13f6e1280388e_1639418176911.jpg',
                            style={'width': '150px', 'height': '150px', 'border-radius': '50%'}
                        ),
                        html.H3("Dr. Jun Yin"),
                        html.H4("Co-founder and Chief Technology Officer"),
                        html.P("Scientific leader with 10+ years experience in computational biology and AI")
                    ], style={'text-align': 'center', 'margin-bottom': '40px'}),
                    html.Div([
                        html.Img(
                            src='https://cdn.prod.website-files.com/64a59756747dc7e6d278f60d/66d75f3397ebd79468188a38_Headshot_2_v2.jpg',
                            style={'width': '150px', 'height': '150px', 'border-radius': '50%'}
                        ),
                        html.H3("Dr. Maya Gosztyla"),
                        html.H4("Scientist, Organoid Technology"),
                        html.P("Neurobiologist with 5+ years of experience in cortical organoid disease models and applications of bioinformatics/machine learning in drug discovery")
                    ], style={'text-align': 'center', 'margin-bottom': '40px'}),
                    html.Div([
                        html.Img(
                            src='https://cdn.prod.website-files.com/64a59756747dc7e6d278f60d/64c15ca30b89296a51f6b55e_Allyson-Muotri.jpg',
                            style={'width': '150px', 'height': '150px', 'border-radius': '50%'}
                        ),
                        html.H3("Dr. Alysson Muotri"),
                        html.H4("Stem cell and brain organoid pioneer"),
                        html.P("Created the first human organoid models for neurodevelopmental disorders.")
                    ], style={'text-align': 'center', 'margin-bottom': '40px'}),
                    html.Div([
                        html.Img(
                            src='https://cdn.prod.website-files.com/64a59756747dc7e6d278f60d/64c15cb0554be23d55dd3e4b_James-Treanor.jpg',
                            style={'width': '150px', 'height': '150px', 'border-radius': '50%'}
                        ),
                        html.H3("Dr. James Treanor"),
                        html.H4("Experienced Biotech C-Suite Officer"),
                        html.P("Current BOD, SAB member, and former CEO at ADRx, Inc.")
                    ], style={'text-align': 'center', 'margin-bottom': '40px'}),
                    html.Div([
                        html.Img(
                            src='https://cdn.prod.website-files.com/64a59756747dc7e6d278f60d/6526fc4ddc1434549fc3f168_Mark-Norman.webp',
                            style={'width': '150px', 'height': '150px', 'border-radius': '50%'}
                        ),
                        html.H3("Dr. Mark H. Norman"),
                        html.H4("Innovative medicinal chemist"),
                        html.P("30+ years of drug discovery and development experience.")
                    ], style={'text-align': 'center', 'margin-bottom': '40px'}),
                    html.Div([
                        html.Img(
                            src='https://cdn.prod.website-files.com/64a59756747dc7e6d278f60d/64c15c7c7b65300978749eba_Edoardo-Marcora.jpg',
                            style={'width': '150px', 'height': '150px', 'border-radius': '50%'}
                        ),
                        html.H3("Dr. Edoarda Marcora"),
                        html.H4("Computational biology, software development, and genetics expertise."),
                        html.P("Professor of Genetics, Genomic Sciences, and Neuroscience, Mount Sinai Icahn School of Medicine; member of the Icahn Genomics Institute")
                    ], style={'text-align': 'center', 'margin-bottom': '40px'}),
                    html.Div([
                        html.Img(
                            src='https://cdn.prod.website-files.com/64a59756747dc7e6d278f60d/64c15c8e3c02982c7c22ebc7_Blake-anson.jpg',
                            style={'width': '150px', 'height': '150px', 'border-radius': '50%'}
                        ),
                        html.H3("Dr. Blake Anson"),
                        html.H4("Business Development Professional with deep commercial experience"),
                        html.P("19+ years building new markets and driving paradigm-shifting tools into biopharma, government, and academic organizations.")
                    ], style={'text-align': 'center', 'margin-bottom': '40px'})
                ], style={'display': 'grid', 'grid-template-columns': 'repeat(auto-fit, minmax(300px, 1fr))', 'gap': '20px', 'justify-items': 'center'})
            ])
        ])
    ])
])
