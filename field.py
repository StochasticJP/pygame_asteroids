class Field():
    # class const
    SCREEN_HEIGHT = 720
    SCREEN_WIDTH = 720

    def __init__(self):
        self.screen = None
        create_field(self)

    def create_field(self):
        return [[(255, 255, 255) for _ in range(0, self.SCREEN_WIDTH)] for _ in range(0, self.SCREEN_HEIGHT)]

    