from os.path import split

#from exercise.string_Same_place_rerevse import reversed_word

a= [12,12,13,"qnkt",12]
print(a)
print(type(a))

name = "vikas verma"
words= name.split()

for word in words:
    reversed_word=""
    for char in word:
        reversed_word=char+reversed_word
    print(reversed_word,end="")
