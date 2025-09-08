import prettymaps
import matplotlib.pyplot as plt

params = {'layers':
            {'perimeter': {},
             'streets': {'width': {'motorway': 5,
                                   'trunk': 5,
                                   'primary': 4.5,
                                   'secondary': 4,
                                   'tertiary': 3.5,
                                   'cycleway': 3.5,
                                   'residential': 3,
                                   'service': 2,
                                   'unclassified': 2,
                                   'pedestrian': 2,
                                   'footway': 1,
                                   'river': 5,'stream':4,"canal":4,"drain":3
                                   }
                         },
             'industrial_land': {'tags': {'landuse': ['construction','industrial','commercial']
                                          }},
             #'residential_land': {'tags': {'landuse': 'residential'}},
             #'farm_land': {'tags': {'landuse': ['farmland','basin']}},
             'building': {'tags': {'building': True
                                       #['office','apartments','residential',
                                   # 'commercial','school','house','retail',
                                   # #'university','kindergarden','dormitory','stadium','college','yes'],
                                   },'union': False
                          },
             'water': {'tags': {'natural': ['water', 'bay','spring'],
                                'waterway': True,
                                'leasure': 'water_park',
                                'landuse': 'reservoir'},'union': False},
             'forest': {'tags': {'landuse': ['forest']}},
             'green': {'tags': {'landuse': ['grass','recreation_ground','meadow',"greenfield",
                                            'farmland','basin','brownfield','farmyard'],
                                'natural': ['island', 'wood','wetland'],
                                'boundary': 'national_park',
                                'place': 'island',
                                'leisure': ['park','common','nature_reserve','marina']
                                },'union': False
                       },
             'beach': {'tags': {'natural': 'beach'}},
             'parking': {'tags': {'amenity': 'parking',
                                  'highway': 'pedestrian',
                                  'man_made': 'pier'
                                  }
                         }
             },
          'style':
              {'perimeter': {'fill': False,
                             'lw': 0,
                             'zorder': 0
                            },
               'background': {'fc': '#F2F4CB',
                              'zorder': -1
                             },
               'green': {'fc': '#8BB174',
                            'ec': '#2F3737',
                            'hatch_c': '#A7C497',
                            'hatch': 'ooo...',
                            'lw': 0.5,
                            'zorder': 2
                            },
               'forest': {'fc': '#64B96A',
                             'ec': '#2F3737',
                             'lw': 0.5,
                             'zorder': 2},
               'water': {'fc': '#a8e1e6',
                            'ec': '#a8e1e6',
                            'hatch_c': '#9bc3d4',
                            'hatch': 'ooo...',
                            'lw': 1,
                            'zorder': 3
                            },
               'beach': {'fc': '#8BB174',
                            'ec': '#2F3737',
                            'hatch_c': '#d4d196',
                            'hatch': 'ooo...',
                            'lw': 0.5, 'zorder': 3
                            },
               'parking': {'fc': '#F2F4CB',
                              'ec': '#2F3737',
                              'lw': 0.5, 'zorder': 4
                           },
               'streets': {'fc': '#2F3737',
                              'ec': '#475657',
                              'alpha': 1,
                              'lw': 0.1,
                              'zorder': 5
                           },
               'building': {'fc':'#FF5E5B',
                   #'palette': ['#433633', '#FF5E5B'],
                               'ec': '#2F3737',
                               'lw': 0.5,
                               'zorder': 6
                            },
               'industrial_land': {'fc':'#433633',
                               'ec': '#2F3737',
                               'lw': 0.5,
                               'zorder': 1
                                   }
               #'residential_land': {'fc':'#4B7B42','ec': '#2F3737','lw': 0.5,'zorder': 5}
               }
          }

plot = prettymaps.plot((34.61270572183845, 112.39602672401526), #extract location query from Google map
                       radius=2500,
                       layers=params["layers"],
                       style=params['style'])
plt.savefig('High-tech Zone.png', dpi=500)
#plt.show()
#data = plot.geodataframes['water']
#print(prettymaps.preset("abraca-redencao"))
#import pandas as pd
#df = pd.DataFrame(data)

#df.to_excel('output3.xlsx', index=False)
