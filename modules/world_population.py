import json
from country_codes import get_country_code as gcc
from pygal.maps.world import World
from pygal.style import RotateStyle, LightColorizedStyle

filename = 'data\\population_data.json'
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = 'World Population in 2010(Gradient), by Country'
cc_population = {}

with open(filename) as f:
    pop_data = json.load(f)
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            code = gcc(country_name)
            population = int(float(pop_dict['Value']))
            if code:
                cc_population[code] = population
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for code, pop in cc_population.items():
    if pop < 10000000:
        cc_pop_1[code] = pop
    elif pop < 1000000000:
        cc_pop_2[code] = pop
    else:
        cc_pop_3[code] = pop
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)
wm.render_to_file('visualizations\\world_population_gradient_light.svg')
    