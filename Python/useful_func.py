abc = "abcdefghijklmnopqrstuvwxyz"

def get_user_input():
    user_input = input()
    try:
        val = int(user_input)
        return val
    except ValueError:
        try:
            val =  float(user_input)
            return val
        except ValueError:
            try:
                val =  bool(user_input)
                return val
            except ValueError:
                val = str(user_input)
                return val

def read_txt_file_content(file_path):
    file = (open(file_path,'r', encoding='UTF8'))
    file_content = file.read()
    return file_content

def Clean(txt:str):
       text = ToLower(txt)
       #txt.replace('  ', ' ')
       #txt ="".join(c for c in txt if c.isalpha())
       return text

def ToLower(txt:str):
    x = txt.lower()
    return x

