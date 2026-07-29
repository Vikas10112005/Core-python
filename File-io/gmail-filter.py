import re #Regular Expression



def readLine():

    input_file = open("C:/Users/hp/PycharmProjects/CorePython/file/gmails.py", 'r')
    output_file = open("C:/Users/hp/PycharmProjects/CorePython/file/correct_gmail.py", "w")
    output_files = open("C:/Users/hp/PycharmProjects/CorePython/file/correct_hotmail.py","w")
    output_filess = open("C:/Users/hp/PycharmProjects/CorePython/file/correct_outlook.py","w")
    for line in input_file:
        if (re.search("@gmail.com", line)):
            output_file.write(line)
            print(line)
        if (re.search("@hotmail.com", line)):
            output_files.write(line)
            print(line)
        if (re.search("@outlook.com", line)):
            output_filess.write(line)
            print(line)
    input_file.close()
    output_file.close()
    output_files.close()
    output_filess.close()



readLine()