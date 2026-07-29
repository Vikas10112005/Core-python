import shutil

source = "C:/Users/hp/Desktop/png.1.jfif";
target = "C:/Users/hp/Desktop/file-io/png.1.jfif";

shutil.copyfile(source, target)
print(source + " is copied to " + target)