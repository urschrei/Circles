# Circles

![Circles](circles.png "Winkel III isn't available, and I don't want to use Kavrayskiy VII, because I don't want to be thought of as an obscurantist.")

A map projection is a systematic transformation of the latitudes and longitudes of locations on the surface of a sphere or an ellipsoid into locations on a plane. ([Snyder, J. P., 1989](http://pubs.usgs.gov/pp/1453/report.pdf))

Simply drawing a circle on the 2-dimensional representation using cartesian co-ordinates will result in something that is…[wrong](http://www.economist.com/node/1788311).

Thomas Lecoq has [helpfully translated](http://www.geophysique.be/2011/02/19/matplotlib-basemap-tutorial-08-shooting-great-circles/) some [JS code written by Ed Williams](http://williams.best.vwh.net/gccalc.htm) into Python, in order to allow the correct calculation of great-circle distances for the [WGS84 ellipsoid](http://en.wikipedia.org/wiki/World_Geodetic_System). I've reproduced it here with some minor alterations, in the form of Circles, a small convenience library. It's designed to be used with the [Basemap](http://matplotlib.org/basemap/) extension to matplotlib, and it requires the [Numpy](http://www.numpy.org) library. Install it using pip: `pip install circles`

`Circles` exposes a single method, `circle()`. Pass it your Basemap instance, latitude and longitude of the point you'd like as the centre of your circle, and the radius. It will return a list of lon, lat tuples *in map projection coordinates*, which can be passed to your Basemap instance for plotting, or converted into Polygons using [Shapely](http://toblerity.org/shapely/manual.html), and then plotted using [Descartes](https://bitbucket.org/sgillies/descartes/).

An example:  

```Python
from Circles.circles import circle
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
from descartes import PolygonPatch
import numpy as np

# use the Robinson projection - it'll distort nicely
m = Basemap(resolution='l', projection='robin', lon_0=0)

radii = [2000]
centerlon = 0.135875
centerlat = 51.5219198
coords = [circle(m, centerlon, centerlat, radius) for radius in radii]

# let's initialise a point and construct a polygon
# http://mitpress.mit.edu/books/road-not-road-and-open-city-ritoque-chile
p = Point(m(-71.530303, -32.824977))
buffered = p.buffer(2000000)
# let's do the same with our calculated coordinates
pol = Polygon(coords[0])

# let's plot everything
plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111, axisbg='w', frame_on=False)

patch1 = PolygonPatch(buffered, fc='#FFCC66', ec='#ffffff', alpha=.75, zorder=2)
patch2 = PolygonPatch(pol, fc='#00BABA', ec='#ffffff', alpha=.75, zorder=2)

m.drawcountries()
m.drawcoastlines()
m.fillcontinents(color='#C4C4C4', lake_color='white')
m.drawparallels(np.arange(-90., 120., 30.))
m.drawmeridians(np.arange(0., 360., 60.))
m.drawmapboundary(fill_color='white')

ax.add_patch(patch1)
ax.add_patch(patch2)

# with apologies to the Sugababes
plt.title("Round round baby, round round")
fig.set_size_inches(12., 8.)
plt.show()
```

The orange circle is drawn using cartesian coordinates, and the teal circle is drawn using Circles. As can be seen, it is correctly distorted, as is to be expected with the [Robinson projection](http://en.wikipedia.org/wiki/Robinson_Projection), which distorts moderately at the [latitude](https://www.google.com/maps/dir/51.5219198,-0.135875/51°31'19.0%22N+0°08'10.0%22E/@51.5217378,-0.1327161,14z/data=!4m13!1m4!3m3!1s0x0:0x0!2zNTHCsDMxJzE5LjAiTiAwwrAwOCcxMC4wIkU!3b1!4m7!1m0!1m5!1m1!1s0x0:0x0!2m2!1d0.136111!2d51.521944) upon which the circles are centered.
