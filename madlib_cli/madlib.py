import re
def welcome():
    """
    This function just to send a welcome msg on the user point , welcoming them to my game
    """
    print('*'*40)
    print ('**' + ' '*9 + 'Welcome to MadLibs' + ' '*9 + '**')
    print ('**' +' '*36 +  '**')
    print ('**' + '   ' + 'Please fill in the template and  ' + '**')
    print ('**' + '   ' + '   get ready to be impressed     ' + '**' )
    print ('**' +' '*36 +  '**')
    print('*'*40)

def read_template(path):
    """
    This function will take a path as a arguement to a targeted text to open the file in read mode and return the content while handiling the I/O errors.

    """
    try:
        with open(path, 'r') as txt:
            content = txt.read()
            print(content)
            return(content)
    except FileNotFoundError:
        raise FileNotFoundError('File not found')
    


def parse_template(content):
    """
    Takes in a string, returns two separate values. 
    Returns a string with language parts removed and a list of the removed language parts.

    """
    parse = re.findall(r'\{.*?\}', content)
    final_list = []
    for i in parse:
        string_edit = (i[1:-1])
        final_list.append(string_edit)
    correct_list = tuple(final_list)
  
    template = re.sub(r'\{.*?\}', "{}", content)
    
    return(template, correct_list)



def merge(content, inputs):
    return content.format(*inputs)
    

def madlib_game():
    welcome()
    template = read_template("assets/template.txt")
    content, correct_list = parse_template(template)
    
    inputs = [input(f"\nPlease enter a {i}: ") for i in correct_list]
    return merge(content, inputs)
