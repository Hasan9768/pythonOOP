
class Phone:
    def call(self):
        print("I can call")
    def message(self):
        print("I can message")

class Noka:
    def call(self):
        print("I can call")

    def message(self):
        print("I can message")
    def Photo(self):
        print("I can take photo")
'''
p=Phone()
p.call()
p.message()
'''
n=Noka()
n.call()
n.message()
n.Photo()

print(issubclass(Noka,Phone))