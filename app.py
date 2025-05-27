from dash import Dash, html, dcc, callback, Output, Input, dash_table
import pandas as pd
import dash_bio as dashbio
import os
from dash_bio.utils import PdbParser, create_mol3d_style

parser = PdbParser('pdb/126.pdb')
src=""
data_molecule = parser.mol3d_data()
styles = create_mol3d_style(
    data_molecule['atoms'], color_element='atom'
)


def fetch_data(table_name,compound_name):
    
    if (compound_name == ''):
        return pd.read_csv('csv_data/'+table_name+'/data.csv')
    else:
        query_data=pd.read_csv('csv_data/'+table_name+'/data.csv')
        query_data=query_data[query_data['Compound Name']==compound_name]
        return query_data


def process_data(df, first_call=False):
    if (first_call == True):
        df = df[df['PubChem Id'] == 73941365]

    index_list = []
    for i in range(df.shape[0]):
        index_list.append(i)

    df.index = index_list
    df_transposed = df.T.reset_index()
    df_transposed = df_transposed.rename(columns={'index': 'Property', 0: 'Property Value'})
    return df_transposed


# rename genotype options
values = os.listdir('csv_data')
print(values)

labels = []
for item in values:
    labels.append(item)

renamed_gen_options = [{"label": label, "value": value} for label, value in zip(labels, values)]

df = pd.read_csv('data.csv')
df_transposed = process_data(df, first_call=True)


app = Dash()
app.title = "NaturePro"
app._favicon = ("about_database_img_2.jpeg")

# application layout starts from here

app.layout = [
html.Div([
    html.Div([],style={'width':'70%'}),
    html.Div([
        html.Div([
            dcc.Link(html.Button("Home", className="button_info"), href="assets/about_database.html", refresh=True),

        ], style={"display": "inline-block", 'margin-right': '5px'}),
        html.Div([
            html.Button("Data Search",className="button_info")

        ],style={"display":"inline-block",'margin-right':'5px'}),

        html.Div([
            dcc.Link(html.Button("Contact Us", className="button_info"), href="assets/about_us.html", refresh=True),

        ], style={"display": "inline-block"}),

    ],style={"width":"70%"})

],style={"display":'flex','margin':'10px'}),


    html.Div(className="about-section", children=[
    html.H1("NaturePro"),
    html.H2("Plant-Derived Natural Products Database for Crop Protection")

],
                       ),
              # NAV blcok
              html.Div([
                  # NAV Div Block
                  html.Div([
                    html.Div(className="sidenav", children=[
                  html.Div([
                      html.H3('Select Crop/Plant', style={'textAlign': 'center','padding-top':'10px'}),
                      dcc.Dropdown(options=renamed_gen_options,
                                   value=values[0], id='table',style={'font-style':'italic'})
                  ]
                  ),

                  html.Div([
                      html.H3('Select Compound', style={'textAlign': 'center'}),
                      dcc.Dropdown(df['Compound Name'].unique(), df['Compound Name'][0], id='compound')
                  ]),
                  # Statistics Div
                  html.Div([
                      html.H1("Statistics", style={'font-size': '30', 'margin-top': '10px',
                                                   'text-align': 'center'}, ),
                      dcc.Textarea(
                          id='textarea_total_gen',
                          value='Total Crops/Plants \nin Database\n262',
                          style={'width': '100%', 'height': 150, },
                          className="text_area"
                      ),

                      dcc.Textarea(
                              id='textarea_total_compounds',
                              value='Total Compounds \nin Database\n5281',
                              style={'width': '100%', 'height': 150},
                              className="text_area"
                      ),

                      dcc.Textarea(
                          id='textarea_sel_compounds',
                          value='Total Compounds in\n'
                                'Selected Crop/Plant\n'
                                '20',
                          style={'width': '100%', 'height': 150, 'text-align': 'center'},
                          className="text_area"
                      ),
                      html.Div([
                            html.H1("Downloads", style={'font-size': '30', 'margin-top': '10px',
                                                   'text-align': 'center'}, ),
                            html.Button("Download All Compounds (SDF format)", id='sdf_dnld',className="button_dnld"),
                            dcc.Download(id="download_sdf")
                      ],style={'width':'100%'}),

                      html.Div([
                          html.Button("Download All Compounds (PDB format)", id='pdb_dnld',className="button_dnld"),
                            dcc.Download(id="download_pdb")
                      ],style={'width':'100%','margin-top':'5px'}),

                      html.Div([
                          html.Button("Download Antiviral Compounds (SDF format)", id='antiviral_sdf_dnld', className="button_dnld"),
                             dcc.Download(id="download_antiviral_sdf")
                     ], style={'width': '100%', 'margin-top': '5px'}),

                      html.Div([
                          html.Button("Download Antifungal Compounds (SDF format)", id='antifungal_sdf_dnld', className="button_dnld"),
                             dcc.Download(id="download_antifungal_sdf")
                     ], style={'width': '100%', 'margin-top': '5px'}),

                  ])
                  # End of Statistics Div
              ]),  # End of Side Nav

                  ]),
                  # content Div Block
                  html.Div([
                    html.Div(className="content", children=[

                  html.H3('General Properties', style={'text-align': 'center'}),
                  dash_table.DataTable(
                      id='data_table_general',
                      columns=[{"name": col, "id": col} for col in df_transposed.columns],
                      data=df_transposed.iloc[:6].to_dict('records'),
                      style_data_conditional=[
                          {
                              'if': {'row_index': 'odd'},
                              'backgroundColor': '#E8E8E8',
                              ##8C92AC
                          },
                          {
                              'if': {'column_id': 'Property'},
                              'fontWeight': 'bold',
                              'font_size': '14px'

                          }
                      ],
                      style_header={
                          ##0D98BA
                          'backgroundColor': '#81d8d0',
                          'fontWeight': 'bold',
                          'font_size': '15px'
                      },

                      # we have less data in this example, so setting to 20
                      style_table={'width': '100%', 'overflowY': 'scroll','overflowX': 'scroll'},
                      style_cell={
                          'whiteSpace': 'normal',
                          'height': 'auto', 'minWidth': '80px', 'width': '100px',
                          'maxWidth': '350px', 'textAlign': 'left', 'font_size': '12px'}
                  ),

                  html.Hr(style={"width": "100%", "border-color": "red"}),

                  html.H3('2-D Molecule Image', style={'text-align': 'center'}),
                  html.Hr(style={"width": "100%", "border-color": "red"}),
                  html.Div([
                      html.Img(id='image', src=app.get_asset_url(path='Images/126.png'),
                               style={'height': '50%', 'width': '50%', 'object-fit': 'cover',
                                      }
                               ), ], style={'display': 'flex', 'justify-content': 'center'
                                            }),
                  html.Hr(style={"width": "100%", "border-color": "red"}),
                  html.H3('3-D Molecule Structure', style={'text-align': 'center'}),
                  html.Hr(style={"width": "100%", "border-color": "red"}),
                  html.Div([
                        html.Div([
                            html.Button("Download Structure", id="btn_structure"),
                            dcc.Download(id="download-structure")
                        ])
                      ,
                      dashbio.Molecule3dViewer(
                          id='dashbio-default-molecule3d',
                          modelData=data_molecule,
                          styles=styles,
                          style={'text-align': 'center', 'height': '100%', 'width': '100%', 'object-fit': 'cover'},
                          width=700
                      ), ]),
                  html.Div(id='default-molecule3d-output', style={'text-align': 'center'}),

                  html.Hr(style={"width": "100%", "border-color": "red"}),

                  # data-table for ADME Properties
                  html.H3('ADME and Drug-likeness Properties', style={'text-align': 'center'}),
                  html.Hr(style={"width": "100%", "border-color": "red"}),
                  dash_table.DataTable(
                      id='data_table_adme',
                      columns=[{"name": col, "id": col} for col in df_transposed.columns],
                      data=df_transposed.iloc[6:30].to_dict('records'),
                      style_data_conditional=[
                          {
                              'if': {'row_index': 'odd'},
                              'backgroundColor': '#E8E8E8',
                              ##8C92AC
                          },
                          {
                              'if': {'column_id': 'Property'},
                              'fontWeight': 'bold',
                              'font_size': '14px'

                          }
                      ],
                      style_header={
                          ##0D98BA
                          'backgroundColor': '#81d8d0',
                          'fontWeight': 'bold',
                          'font_size': '15px'
                      },

                      # we have less data in this example, so setting to 20
                      style_table={'width': '100%', 'overflowY': 'scroll'},
                      style_cell={
                          'whiteSpace': 'normal',
                          'height': 'auto', 'minWidth': '180px', 'width': '180px',
                          'maxWidth': '180px', 'textAlign': 'left', 'font_size': '12px'}
                  ),

                  html.Hr(style={"width": "100%", "border-color": "red"}),

                  # data-table for ADME Properties
                  html.H3('Toxicity Properties', style={'text-align': 'center'}),
                  html.Hr(style={"width": "100%", "border-color": "red"}),
                  dash_table.DataTable(
                      id='data_table_toxicity',
                      columns=[{"name": col, "id": col} for col in df_transposed.columns],
                      data=df_transposed.iloc[30:].to_dict('records'),
                      style_data_conditional=[
                          {
                              'if': {'row_index': 'odd'},
                              'backgroundColor': '#E8E8E8',
                              ##8C92AC
                          },
                          {
                              'if': {'column_id': 'Property'},
                              'fontWeight': 'bold',
                              'font_size': '14px'

                          }
                      ],
                      style_header={
                          ##0D98BA
                          'backgroundColor': '#81d8d0',
                          'fontWeight': 'bold',
                          'font_size': '15px'
                      },

                      # we have less data in this example, so setting to 20
                      style_table={'width': '100%', 'overflowY': 'scroll'},
                      style_cell={
                          'whiteSpace': 'normal',
                          'height': 'auto', 'minWidth': '180px', 'width': '180px',
                          'maxWidth': '180px', 'textAlign': 'left', 'font_size': '12px'}
                  ),
              ])

                  ],style={'display':'inline-block','margin-left':'20px','width':'100%'})

              ],style={'display':'flex'}),

             html.Div(className="footer",children=[
                 html.H3(className="footer_text",children=[
                     "ICAR Data Use Licence"
                 ]),
                html.H3(children=[
                     "Copyright © ICAR - Indian Agricultural Statistics Research Institute"
                 ]),
                    html.H3(children=[
                     "Library Avenue, PUSA, New Delhi - 110 012 (INDIA)"
                 ]),
                    html.H3(children=[
                    "Phone: 91-11-25847121-24, 25841254 (PBX), Fax: 91-11-25841564"
                 ]),
                    html.H3(children=[
                    "All rights reserved"
                 ]),
                    html.A(href="https://iasri.icar.gov.in/",children=[html.Img(src=app.get_asset_url(path='iasri.png'),
                               style={'height': '100px', 'width': '100px', 'border-radious':'50%'
                                      })]),
                    html.A(href="https://icar.org.in/",children=[html.Img(src=app.get_asset_url(path='test_icar.jpg'),
                               style={'height': '100px', 'width': '100px', 'border-radious':'50%'
                                      })]),

                 html.A(href="https://www.iari.res.in/en/index.php", children=[html.Img(src=app.get_asset_url(path='iari.png'),
                                                                        style={'height': '100px', 'width': '100px',
                                                                               'border-radious': '50%'
                                                                               })]),

             ])



]

# callback to update the compound dropdown
@callback(
    [Output('compound', 'options'),
            Output('compound', 'value'),
            Output('textarea_sel_compounds', 'value')],
    Input('table', 'value')
)
def update_compund_dropdwon(value):

    data=fetch_data(value,'')
    total_mols = data.shape[0]
    text_area_text = 'Total Compounds in\nSelected Crop/Plant\n' + str(total_mols)

    options=data['Compound Name']
    value=options[0]
    return options,value,text_area_text


# callback to update the table, image and SDF structure
@callback(
[Output('data_table_general', 'data'),
        Output('data_table_adme', 'data'),
        Output('data_table_toxicity', 'data'),
        Output('image', 'src'),
        Output('dashbio-default-molecule3d','modelData'),
        Output('dashbio-default-molecule3d', 'styles')],

    [Input('table', 'value'),
        Input('compound', 'value')]
)
def update_table_img_structure(table_name,compound_name):

    global src
    data=fetch_data(table_name,compound_name)
    


    data_t=process_data(data.copy())
    
    src=str(data['PubChem Id'].iloc[0])
    src=src.strip()
    img_path=app.get_asset_url('Images/'+src+'.png')

    parser = PdbParser('pdb/'+src + '.pdb')
    data_molecule = parser.mol3d_data()
    styles = create_mol3d_style(
        data_molecule['atoms']
    )
    return data_t[:6].to_dict('records'),data_t[6:30].to_dict('records'),data_t[30:].to_dict('records'),img_path,data_molecule,styles


# download single structure
@callback(
    Output("download-structure", "data"),
    Input("btn_structure", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    global src
    return dcc.send_file(
        'pdb/' + src + '.pdb'
    )

# download all sdf structures
@callback(
    Output("download_sdf", "data"),
    Input("sdf_dnld", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    global src
    return dcc.send_file(
        'assets/all_compounds.sdf'
    )

# download all pdb structures
@callback(
    Output("download_pdb", "data"),
    Input("pdb_dnld",
          "n_clicks"),
    prevent_initial_call=True,
)

def func(n_clicks):
    global src
    return dcc.send_file(
        'assets/all_compounds.pdb'
    )

# download antiviral compounds
@callback(
    Output("download_antiviral_sdf", "data"),
    Input("antiviral_sdf_dnld",
          "n_clicks"),
    prevent_initial_call=True,
)

def func(n_clicks):
    global src
    return dcc.send_file(
        'assets/antiviral.sdf'
    )

# download antifungal compounds
@callback(
    Output("download_antifungal_sdf", "data"),
    Input("antifungal_sdf_dnld",
          "n_clicks"),
    prevent_initial_call=True,
)

def func(n_clicks):
    global src
    return dcc.send_file(
        'assets/antifungal.sdf'
    )


if __name__ == '__main__':
    data = fetch_data('abutilon_indicum','')
    # app.run(host="200.200.202.79",port="8050")
    app.run()