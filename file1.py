class Fiber:
    """A sample Fiber class"""

    def __init__(self, types, micron, texture):
        self.types = types
        self.micron = micron
        self.texture = texture

    @property
    def micron(self):
        return '{}, {} microns'.format(self.types, self.micron)

    @property
    def texture(self):
        return '{}'.format(self.texture)


