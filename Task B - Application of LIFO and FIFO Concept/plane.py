class Plane:
    def __init__(self, id, fuel, distance):
        self.id = id
        self.fuel = fuel
        self.distance = distance
        self.fuel_level = self.calculate_fuel_level()
        self.FUEL_CATEGORY = ["low", "normal", "high"]

    def calculate_fuel_level(self):
        if self.fuel <= 20:
            return 0 # low
        elif self.fuel > 60:
            return 2 # high
        return 1     # normal

    def __lt__(self, other):
        if self.fuel_level != other.fuel_level:
            return self.fuel_level < other.fuel_level
        return self.distance < other.distance
    
    def __gt__(self, other):
        if self.fuel_level != other.fuel_level:
            return self.fuel_level > other.fuel_level
        return self.distance > other.distance
    
    def __eq__(self, other):
        return (self.fuel_level == other.fuel_level) and (self.distance == other.distance)

    def __str__(self):
        return f"Plane {self.id}: Fuel = {self.fuel} ({self.FUEL_CATEGORY[self.fuel_level]}), Distance = {self.distance} miles"
    
    @staticmethod
    def get_priority_order(priority_queue):
        return 'Queue order: ' + ','.join([plane.id for plane in priority_queue.heap])
