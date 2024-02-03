class Screen:

    def __init__(self, weight, high):
        self.weight = weight
        self.high = high

    def show(self, image):
        print("Show:", image)

    def get_size(self):
        print("weight:", self.weight, ". high:", self.high)


usual_screen = Screen(100, 100)
usual_screen.show("Cartoon")
usual_screen.get_size()


class Monitor(Screen):

    def __init__(self, type, name, weight, high):
        super().__init__(weight, high)
        self._type = type
        self.name = name
        self.is_connected = False

    def connect_to_usb(self, is_connected):
        self.is_connected = is_connected
        if self.is_connected:
            print("Connected")
        else:
            print("Disconnected")


dell = Monitor('oled', 'dell', 100, 100)
dell.show("Cartoon")
dell.connect_to_usb(True)
dell.connect_to_usb(False)