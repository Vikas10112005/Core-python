class teacher:
    def teach(self):
        return "teaching"

class singer:
    def sing(self):
        return "singing"
    
class person(teacher,singer):
    def dance(self):
        return "dancing"

p = person()

print(p.teach())
print(p.sing())
print(p.dance())