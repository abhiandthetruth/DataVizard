import pygal
from pygal.maps.world import World

wm = World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 3412600, 'us':309349000, 'mx':113423000})
wm.render_to_file('visualizations\\na_populations.svg') 