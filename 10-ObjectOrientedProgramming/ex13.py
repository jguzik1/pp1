class TV():
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.avalible_channels = []
        self.volume = 0

    def turn_on(self):
        '''Turns on TV'''
        self.is_on = True
    
    def turn_off(self):
        '''Turns off TV'''
        self.is_on = False

    def show_status(self):
        '''shows TV status'''
        if self.is_on == True:
            try:
                print(f"TV is on and active chanel is {self.channel} ({self.avalible_channels[self.channel - 1]}) and volume is {self.volume}")
            except:
                print('TV on, channel number exceeded')
        else:
            print("TV is off")

    def channel_no(self,new_channel_no):
        '''changes channel number'''
        self.channel = new_channel_no

    def set_channels(self, new_channels):
        '''adds new channels'''
        for channel in new_channels:
            self.avalible_channels.append(channel)

    def show_channels(self):
        '''Shows avalible channels'''
        print(self.avalible_channels)
    
    def vol_up(self):
        '''turns up tv volume'''
        if self.volume < 10:
            self.volume += 1

    def vol_down(self):
        '''turns down tv volume'''
        if self.volume > 0:
            self.volume -= 1

list_of_channels = ['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery']

help(TV())

Samsung = TV()
Samsung.show_status()
Samsung.turn_on()
Samsung.show_status()
Samsung.show_channels()
Samsung.set_channels(list_of_channels)
Samsung.show_channels()
Samsung.channel_no(1)
Samsung.vol_up()
Samsung.show_status()
Samsung.turn_off()
Samsung.show_status()