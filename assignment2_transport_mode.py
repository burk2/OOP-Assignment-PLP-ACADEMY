class Bicycle:
    def move(self):
        return "Pedaling along the village path..."

class Matatu:
    def move(self):
        return "Zooming through Nairobi traffic with loud music..."

class Train:
    def move(self):
        return "Gliding steadily across the countryside..."

# Polymorphic behavior
vehicles = [Bicycle(), Matatu(), Train()]
for vehicle in vehicles:
    print(vehicle.move())
