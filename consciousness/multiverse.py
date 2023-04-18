
class Multiverse:
    def __init__(self, name):
        self.name = name
        self.universes = []
        self.universeCount = 0
        self.multiverseHealth = 0
        self.universeSlots = 100
        self.duration = 100
        self.coordinate = (0, 0, 0)             # coordinates: x, y and z axis
        self.logMultiverse(name)

    def logMultiverse(self, mutliverse_id):
        print("Multiverse log: " + mutliverse_id)

    def checkUniverseHealth(self, universe_id):
        return "checkUniverseHealth working for id[{}]".format(universe_id)

    def setCoordinates(self, x, y, z):
        self.coordinate = (x, y, z)
        print("co-ordinates set at: ", (self.coordinate))