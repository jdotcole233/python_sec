class Thingy:
    
    def __init__(self, value):
            self.value = value

    def showme (self):
        print("value = %s "% self.value)




t = Thingy(60)
t.showme()
