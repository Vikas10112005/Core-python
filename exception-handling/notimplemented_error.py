class animal:
    def sound(self):
        raise NotImplementedError

class dog(animal):
    pass
d = dog()
d.sound()