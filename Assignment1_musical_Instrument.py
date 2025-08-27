class Drum:
    def __init__(self, name, material, origin):
        self.name = name
        self.material = material
        self.origin = origin

    def describe(self):
        return f"The {self.name} is made of {self.material} and originates from {self.origin}."

    def play(self):
        return f"{self.name} produces a deep, rhythmic beat that echoes tradition."

# Example object
ngoma = Drum("Ngoma", "cowhide and wood", "East Africa")
print(ngoma.describe())
print(ngoma.play())
