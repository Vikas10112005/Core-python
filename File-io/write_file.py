def writefile():
    file = open("C:/Users/hp/Desktop/file-io/abc.txt", 'w')
    file.write("hi\n")
    file.write("i am vikas chandravanshi\n")
    file.write("this is my python file")
    print("successfully write")
    file.close()
writefile()