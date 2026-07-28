def readfile():
    file = open("C:/Users/hp/Desktop/file-io/abc.txt",'r')
    text = file.read()
    print(text)
    file.close()

readfile()