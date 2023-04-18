from consciousness.multiverse import Multiverse
import math as math
import numpy as np
import seaborn.objects as seabornObjects
from matplotlib import pyplot as plt

multiversePopulateionAmount = 100
multiverseCoordinatesStore = []
MAX_MATRIX_WIDTH = 100
MAX_MATRIX_HEIGHT = 100
MAX_MATRIX_DENSITY = 100

for multiverseID in range(0, multiversePopulateionAmount):
    multiverse = Multiverse(name="multiverse-{}".format(multiverseID))
    multiverse.setCoordinates(x=np.random.randint(0, MAX_MATRIX_WIDTH), y=np.random.randint(0, MAX_MATRIX_HEIGHT), z=np.random.randint(0, MAX_MATRIX_DENSITY))
    multiverseCoordinatesStore.append(multiverse.coordinate)

MULTIVERSAL_MATRIX_PLOT = plt.figure()
MULTIVERSAL_MATRIX_AXES = plt.axes(projection="3d")

# cleaning co-ordinate data for all x, y and z axes
# also mutliversal-coordinate-data will keep the actual co-ordinate system stable.
# at the same time, can be used to manipulate values with different densities, value changes 
# and error rates.
MULTIVERSAL_COORDINATE_DATA = []
MULTIVERSAL_X_COORDINATE_DATA = []
MULTIVERSAL_Y_COORDINATE_DATA = []
MULTIVERSAL_Z_COORDINATE_DATA = []
for data in multiverseCoordinatesStore:
    MULTIVERSAL_X_COORDINATE_DATA.append(data[0])
    MULTIVERSAL_Y_COORDINATE_DATA.append(data[1])
    MULTIVERSAL_Z_COORDINATE_DATA.append(data[2])

MULTIVERSAL_MATRIX_AXES.scatter3D(MULTIVERSAL_X_COORDINATE_DATA, MULTIVERSAL_Y_COORDINATE_DATA, MULTIVERSAL_Z_COORDINATE_DATA)
plt.savefig("MULTIVERSAL-MATRIX-PLOT.png")
