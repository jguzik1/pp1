class University():
    def __init__(self):
        self.name = 'CUE'

    def set_name(self,new_name):
        self.name = new_name

    def print_name(self):
        print(self.name)

    
a = University()
a.set_name('BOB')
a.print_name()