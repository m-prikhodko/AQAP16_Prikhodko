class Monitor:

    def __init__(self, matrix, high):
        self.weight = weight
        self.high = high

    def show(self, image):
        print("Show:", image)

    def get_size(self):
        print("weight:", self.weight, ". high:", self.high)


usual_screen = Screen(100, 100)
usual_screen.show("Cartoon")
usual_screen.get_size()
