class TV():
    def __init__(self):
        self.is_on = False
        self.chanel = 1

    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def channel_no(self,new_channel):
        self.chanel = new_channel

    def show_status(self):
        if self.is_on == True:
            print(f"TV is on and active chanel is {self.chanel}")
        else:
            print("TV is off")


Samsung = TV()

Samsung.show_status()
Samsung.turn_on()
Samsung.show_status()
Samsung.channel_no(5)
Samsung.show_status()
Samsung.turn_off()
Samsung.show_status()