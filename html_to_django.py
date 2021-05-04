import re
import os.path


def input_module():
    file_name = input("Please put the file to be edited in the same directory as this script. \n Enter the file's name : ")
    new_file = naming(file_name)
    return file_name, new_file


def naming(file_name):
    base = os.path.basename(file_name)
    new_file = re.sub(r"(\.[a-z]*)", r"_new\1",base)
    return new_file

def modifier(line):
    new_line = re.sub(r"(href=\")([a-zA-Z0-9\:\-\/\.]*)(\")" , r"\1{% static '\2' %}\3", line)
    new_line = re.sub(r"(src=\")([a-zA-Z0-9\-\/\.]*)(\")" , r"\1{% static '\2' %}\3", new_line)
    return new_line 

def rw(file_name, new_file):
    with open(file_name, 'r', encoding = 'utf-8') as file:
        
        with open(new_file, 'w', encoding = 'utf-8') as f:
            f.write("{% load static %}\n")
            for line in file:
            
                
                
                line = modifier(line)
                
                #print(line)
                f.write(line)
            



def main():
    file_name, new_file = input_module()
    
    rw(file_name, new_file)


if __name__ == "__main__":
    main()
