class Thermometer():
    def __init__(self):
        self.is_on = False
        self.temperature = 0

    def turn_on(self):
        '''Turns on the theremomether'''
        self.is_on = True

    def turn_off(self):
        '''Turns off the thermomether'''
        self.is_on = False

    def measure(self,temp):
        '''Measures temperature if thermomether is on'''
        if self.is_on == True and temp > 34.0 and temp < 42.0:
            self.temperature = temp

    def display(self):
        '''displays results'''
        if self.is_on == True and self.temperature != 0:
            if self.temperature >= 41.0:
                print(f'Temperature: {self.temperature} (CRITICAL TEMPERATURE!!)')
            elif self.temperature >= 37.0:
                print(f'Temperature: {self.temperature} (fever)')
            else:
                print(f'Temperature: {self.temperature}')
        else:
            print("Thermomether was off or temperature was too low / high")