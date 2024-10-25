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
            "Leveraging Foundation Model-Based Organoid Gene Networks for CNS Drug Discovery",
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
                #html.H2("About Us", style={'text-align': 'center'}),
                html.P([
                    "Parkinson’s disease (PD) is the second most common neurodegenerative disorder, affecting over 10 million people globally, with over 90,000 new cases diagnosed annually in the U.S. Conventional drug discovery has yet to produce safe and effective disease-modifying therapies that prevent dopamine neuron degeneration and slow PD progression.",
                    html.Br(),
                    html.Br(),                    
                    "Our project introduces a cutting-edge midbrain organoid platform derived from Parkinson’s patients, combined with a Foundation Model-based network analysis protocol. This platform enables clearer profiling of disease mechanisms, accelerating the discovery of novel therapeutic targets, identifying biomarkers, and improving patient stratification for clinical trials.",                    
                    html.Br(),
                    html.Br(), 
                    "Visit us at ",
                    html.A(
                        "BrainStorm Therapeutics",
                        href="https://www.brainstormtherapeutics.org/",  # Replace with the correct URL for BrainStorm Therapeutics
                        target="_blank",  # Opens the link in a new tab
                        style={'text-decoration': 'underline', 'color': 'blue'}  # Style for the link
                    ),
                    "."
                ],
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
                                #{
                                #    'label': 'GBA1-PD vs WT, Whole organoid, FC Gradient',
                                #    'value': 'log2foldChange'
                                #},
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
                html.H2("Team BST, Bio x ML Hackathon", style={'text-align': 'center', 'margin-bottom': '30px'}),
                html.Div([
                    html.Div([
                        html.Img(
                            src='assets/team/Robert_Fremeau.png',
                            style={
                                'width': '150px',
                                'height': '150px',
                                'object-fit': 'cover',
                                'border-radius': '50%'
                            }
                        ),
                        html.H3("Dr. Robert Fremeau"),
                        html.H4("Founder and CSO, BrainStorm Therapeutics"),                       
                        html.P("Experienced R&D leader with 20+ years experience in academia and industry."),
                        html.A(
                            "LinkedIn Profile",  # Text for the link
                            href="https://www.linkedin.com/in/robertfremeau/",  # Replace with the actual LinkedIn URL
                            target="_blank",  # Opens the link in a new tab
                            style={'font-size': '16px', 'color': 'blue', 'text-decoration': 'underline', 'margin-top': '10px'}
                        )                        
                    ], style={
                        'text-align': 'center',
                        'margin-bottom': '40px'
                    }),
                    html.Div([
                        html.Img(
                            src='assets/team/Jun_Yin.png',
                            style={
                                'width': '150px',
                                'height': '150px',
                                'object-fit': 'cover',
                                'border-radius': '50%'
                            }
                        ),
                        html.H3("Dr. Jun Yin"),
                        html.H4("Co-founder and CTO, BrainStorm Therapeutics"),
                        html.P("Scientific leader with 10+ years experience in computational biology and AI."),
                        html.A(
                            "LinkedIn Profile",  # Text for the link
                            href="https://www.linkedin.com/in/yinjun111/",  # Replace with the actual LinkedIn URL
                            target="_blank",  # Opens the link in a new tab
                            style={'font-size': '16px', 'color': 'blue', 'text-decoration': 'underline', 'margin-top': '10px'}
                        )                          
                    ], style={
                        'text-align': 'center',
                        'margin-bottom': '40px'
                    }),
                    html.Div([
                        html.Img(
                            src='assets/team/Maya_Gosztyla.png',
                            style={
                                'width': '150px',
                                'height': '150px',
                                'object-fit': 'cover',
                                'border-radius': '50%'
                            }
                        ),
                        html.H3("Dr. Maya Gosztyla"),
                        html.H4("Scientist, Organoid Technology, BrainStorm Therapeutics"),
                        html.P("Neurobiologist with 5+ years of experience in cortical organoid disease models and applications of bioinformatics/machine learning in drug discovery."),
                        html.A(
                            "LinkedIn Profile",  # Text for the link
                            href="https://www.linkedin.com/in/mayagosztyla/",  # Replace with the actual LinkedIn URL
                            target="_blank",  # Opens the link in a new tab
                            style={'font-size': '16px', 'color': 'blue', 'text-decoration': 'underline', 'margin-top': '10px'}
                        )  
                    ], style={
                        'text-align': 'center',
                        'margin-bottom': '40px'
                    }),
                    html.Div([
                        html.Img(
                            src='assets/team/Birkan_Gokbag.png',
                            style={
                                'width': '150px',
                                'height': '150px',
                                'object-fit': 'cover',
                                'border-radius': '50%'
                            }
                        ),
                        html.H3("Dr. Birkan Gokbag"),
                        html.H4(""),
                        html.P("5th year PhD Candidate, Ohio State University"),
                        html.A(
                            "LinkedIn Profile",  # Text for the link
                            href="https://www.linkedin.com/in/birkan-gokbag/",  # Replace with the actual LinkedIn URL
                            target="_blank",  # Opens the link in a new tab
                            style={'font-size': '16px', 'color': 'blue', 'text-decoration': 'underline', 'margin-top': '10px'}
                        ) 
                    ], style={
                        'text-align': 'center',
                        'margin-bottom': '40px'
                    }),
                    html.Div([
                        html.Img(
                            src='assets/team/Anna_Rychkova.png',
                            style={
                                'width': '150px',
                                'height': '150px',
                                'object-fit': 'cover',
                                'border-radius': '50%'
                            }
                        ),
                        html.H3("Dr. Anna Rychkova"),
                        html.H4(""),
                        html.P("Former team leader, Alector"),
                        html.A(
                            "LinkedIn Profile",  # Text for the link
                            href="https://www.linkedin.com/in/annarychkova/",  # Replace with the actual LinkedIn URL
                            target="_blank",  # Opens the link in a new tab
                            style={'font-size': '16px', 'color': 'blue', 'text-decoration': 'underline', 'margin-top': '10px'}
                        ) 
                    ], style={
                        'text-align': 'center',
                        'margin-bottom': '40px'
                    }),
                    html.Div([
                        html.Img(
                            src='assets/team/Jens_Schwamborn.png',
                            style={
                                'width': '150px',
                                'height': '150px',
                                'object-fit': 'cover',
                                'border-radius': '50%'
                            }
                        ),
                        html.H3("Dr. Jens Schwamborn"),
                        html.H4(""),
                        html.P("Professor, University of Luxembourg; Co-Founder, OrganoTherapeutics"),
                        html.A(
                            "LinkedIn Profile",  # Text for the link
                            href="https://www.linkedin.com/in/jens-schwamborn-8a350676/",  # Replace with the actual LinkedIn URL
                            target="_blank",  # Opens the link in a new tab
                            style={'font-size': '16px', 'color': 'blue', 'text-decoration': 'underline', 'margin-top': '10px'}
                        ) 
                    ], style={
                        'text-align': 'center',
                        'margin-bottom': '40px'
                    }),
                ], style={
                    'display': 'grid',
                    'grid-template-columns': 'repeat(auto-fit, minmax(300px, 1fr))',
                    'gap': '20px',
                    'justify-items': 'center'
                })
            ])
        ])
    ])
])
