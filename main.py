from HashMap import HashMap
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP, '/assets/style.css']  # Ensure this path is correct

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

number_options = [{'label': str(i), 'value': i} for i in range(1, 10)]

app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H1('Movie Recommender', className='text-center my-4'), width=12)
    ),

    dbc.Row([
        dbc.Col([
            dbc.Label('Rating:', className='mt-3 label-title', style={'margin-left': '120px'}),
            dbc.Row([
                dbc.Col(dcc.Dropdown(id='rating-number', options=number_options, value=1, style={'margin-bottom': '20px'}), width=1),
                dbc.Col(dcc.RangeSlider(id='voter-average', min=0, max=10, step=0.1, value=[6, 8],
                            marks={i: str(i) for i in range(11)}), width=8)
            ])
        ], width=8)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Label('Genre:', className='mt-3 label-title', style={'margin-left': '120px'}),
            dbc.Row([
                dbc.Col(dcc.Dropdown(id='genre-number', options=number_options, value=2, style={'margin-bottom': '20px'}), width=1),
                dbc.Col(dcc.Dropdown(id='genre', options=[{'label': genre, 'value': genre} for genre in ["Action","Adventure",
            "Comedy", "Drama", "Horror", "Romance", "Science Fiction", "Crime", "Thriller", "Fantasy", "Mystery",
            "War", "Family", "Animation", "Documentary"]], value=["Action"],
           multi=True, style={'margin-bottom': '20px'}), width=8)
            ])
        ], width=8)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Label('Runtime (minutes):', className='mt-3 label-title', style={'margin-left': '120px'}),
            dbc.Row([
                dbc.Col(dcc.Dropdown(id='runtime-number', options=number_options, value=3, style={'margin-bottom': '20px'}), width=1),
                dbc.Col(dcc.RangeSlider(id='runtime', min=0, max=500, step=10, value=[90, 150],
                            marks={i: str(i) for i in range(0, 501, 50)}), width=8)
            ])
        ], width=8)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Label('Release Date:', className='mt-3 label-title', style={'margin-left': '120px'}),
            dbc.Row([
                dbc.Col(dcc.Dropdown(id='release-date-number', options=number_options, value=4, style={'margin-bottom': '20px'}), width=1),
                dbc.Col(dcc.RangeSlider(id='release-date', min=1900, max=2024, step=1, value=[2000, 2020],
                            marks={i: str(i) for i in range(1900, 2025, 10)}), width=8)
            ])
        ], width=8)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Label('Popularity Score:', className='mt-3 label-title', style={'margin-left': '120px'}),
            dbc.Row([
                dbc.Col(dcc.Dropdown(id='popularity-score-number', options=number_options, value=5, style={'margin-bottom': '20px'}), width=1),
                dbc.Col(dcc.RangeSlider(id='popularity-score', min=0, max=300, step=1, value=[50, 150],
                            marks={i: str(i) for i in range(0, 301, 50)}), width=8)
            ])
        ], width=8)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Label('Revenue (in billions):', className='mt-3 label-title', style={'margin-left': '120px'}),
            dbc.Row([
                dbc.Col(dcc.Dropdown(id='revenue-number', options=number_options, value=6, style={'margin-bottom': '20px'}), width=1),
                dbc.Col(dcc.RangeSlider(id='revenue', min=0, max=4, step=0.1, value=[0.5, 2.5],
                            marks={i: f"${i}B" for i in range(0, 5)}), width=8)
            ])
        ], width=8)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Label('Key Words:', className='mt-3 label-title', style={'margin-left': '120px'}),
            dbc.Row([
                dbc.Col(dcc.Dropdown(id='keywords-number', options=number_options, value=7, style={'margin-bottom': '20px'}), width=1),
                dbc.Col(dcc.Input(id='keywords', type='text', placeholder='Enter keywords separated by commas', style={'margin-bottom': '20px', 'width': '100%'}), width=8)
            ])
        ], width=8)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Label('Production Country:', className='mt-3 label-title', style={'margin-left': '120px'}),
            dbc.Row([
                dbc.Col(dcc.Dropdown(id='production-country-number', options=number_options, value=8, style={'margin-bottom': '20px'}), width=1),
                dbc.Col(dcc.Dropdown(id='production-country', options=[{'label': country, 'value': country} for country in ["United States of America",
            "United Kingdom", "New Zealand", "Canada", "Australia", "France", "Germany", "South Korea", "Japan"]], value=["United States of America"],
                         multi=True, style={'margin-bottom': '20px'}), width=8)
            ])
        ], width=8)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Label('Original Language:', className='mt-3 label-title', style={'margin-left': '120px'}),
            dbc.Row([
                dbc.Col(dcc.Dropdown(id='original-language-number', options=number_options, value=9, style={'margin-bottom': '20px'}), width=1),
                dbc.Col(dcc.Dropdown(id='original-language', options=[{'label': lang, 'value': lang} for lang in ["English", "Spanish", "French", "German", "Chinese"]], value="English",
                         style={'margin-bottom': '20px'}), width=8),
            ])
        ], width=8)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Label('Data Structure Selection:', className='mt-3 label-title'),
            dcc.RadioItems(id='data-structure', options=[
                {'label': 'Hashmap', 'value': 'Hashmap'},
                {'label': 'Red Black Tree', 'value': 'Red Black Tree'}
            ], value='Hashmap', style={'font-size': '1.5em', 'margin': '20px', 'margin-top': '0px'}),
        ], width=8)
    ]),

    dbc.Row(
        dbc.Col(html.Div(dbc.Button('Submit', id='submit-button', n_clicks=0, className='btn btn-primary mt-3 mb-4', style={'width': '10%'})), width=12, className='text-center')
    ),

    dbc.Row(
        dbc.Col(html.Div(id='output-container', className='mt-3'), width=12)
    )
], fluid=True)

@app.callback(
    Output('output-container', 'children'),
    Input('submit-button', 'n_clicks'),
    State('data-structure', 'value'),
    State('original-language', 'value'),
    State('original-language-number', 'value'),
    State('voter-average', 'value'),
    State('rating-number', 'value'),
    State('popularity-score', 'value'),
    State('popularity-score-number', 'value'),
    State('keywords', 'value'),
    State('keywords-number', 'value'),
    State('genre', 'value'),
    State('genre-number', 'value'),
    State('revenue', 'value'),
    State('revenue-number', 'value'),
    State('runtime', 'value'),
    State('runtime-number', 'value'),
    State('production-country', 'value'),
    State('production-country-number', 'value'),
    State('release-date', 'value'),
    State('release-date-number', 'value')
)

def update_output(n_clicks, data_structure, original_language, original_language_number, voter_average, rating_number, popularity_score, popularity_score_number, keywords, keywords_number, genre, genre_number, revenue, revenue_number, runtime, runtime_number, production_country, production_country_number, release_date, release_date_number):
    if n_clicks > 0 and n_clicks is not None:
        n_clicks = 0

        if data_structure == 'Hashmap':
            # if hashmap is selected do below else
            filters = [
                ("vote_average", (voter_average[0], voter_average[1]), rating_number),
                ("popularity", (popularity_score[0], popularity_score[1]), popularity_score_number),
                ("revenue", (revenue[0], revenue[1]), revenue_number),
                ("runtime", (runtime[0], runtime[1]), runtime_number),
                ("genres", genre, genre_number),
                ("release_date", [release_date[0], release_date[1]], release_date_number),
                ("keywords", keywords, keywords_number),
                ("production-country", production_country, production_country_number),
                ("original-language", original_language, original_language_number)
            ]

            # Sort filters based on their priority values
            filters_sorted = sorted(filters, key=lambda x: x[2])

            # Build the filters_priorities list
            priority_filters = [(filter[0], filter[1]) for filter in filters_sorted]
            hashmap = HashMap(size=100000)
            hashmap.read_csv_and_insert_into_hashmap('TMDB_movie_dataset_v11.csv')
            results = hashmap.filter(priority_filters)
            movies = [results[x][0] for x in range(len(results))]
            return html.Div([
                html.H4("Recommended Movies:"),
            html.Ul([html.Li(name) for name in movies])
            ])
        #elif data_structure == "Red Black Tree":


if __name__ == '__main__':
    app.run_server(debug=True)
