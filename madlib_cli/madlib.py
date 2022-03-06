import re
def welcome():
    print('*'*40)
    print ('**' + ' '*9 + 'Welcome to MadLibs' + ' '*9 + '**')
    print ('**' +' '*36 +  '**')
    print ('**' + '   ' + 'Please fill in the template and  ' + '**')
    print ('**' + '   ' + '   get ready to be impressed     ' + '**' )
    print ('**' +' '*36 +  '**')
    print('*'*40)

def read_template():
    try:
        with open ("assets/dark_and_stormy_night_template.txt", 'r') as txt:
            content = txt.read()
            returned_string = str(content)
            print(returned_string)
            return(returned_string)
    except FileNotFoundError:
        raise FileNotFoundError('File not found')
    


def parse_template():
    pass


def merge():
    pass
welcome()
read_template()