class TV():
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on == True:
            print("TV is on")
        else:
            print("TV is off")


Samsung = TV()

Samsung.show_status()
Samsung.turn_on()
Samsung.show_status()
Samsung.turn_off()
Samsung.show_status()