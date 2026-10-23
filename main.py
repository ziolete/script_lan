from simpleeval import simple_eval
KV = {}
def forloop():
    pass
def whileloop():
    pass
def functionss():
    pass

def is_arithmetic(expr):
    try:
        check = simple_eval(expr)
        if type(check) == float or type(check) == int:
            return True
        else:
            return False
    except Exception as v:
        pass
        return False
def intfunc(typee,var,value):
    if typee == 'int':
        keys = [var]
        values = [value]
        for k,v in zip(keys,values):
            KV[k] = v
    return KV
def floatfunc(typee,var,value):
    if typee == 'float':
        keys = [var]
        values = [value]
        for k,v in zip(keys,values):
            KV[k] = v
    return KV
def boolfunc(typee,var,value):
    if typee == 'bool':
        if value == 'True' or value == 'False':
            keys = [var]
            values = [value]
            for k,v in zip(keys,values):
                KV[k] = v
    return KV
def strfunc(var,value):
    if type(value) == str:
        if value[0] == '"' and value[-1] == '"':
            keys = [var]
            values =[value]
            for k,v in zip(keys,values):
                KV[k] = v
    return KV
while True:

    language_input = input("idk :>")
    try:
        s = language_input.split()
#>

        if len(s) >1:
            
            if s[0] == 'print':
                print(' '.join(s[1::]))

        if len(s) >= 4:
            ss = ''.join(s[3::])
#assigning vars
            if s[2] == '=':
                if s[0] == 'int':
                    if is_arithmetic(ss) == True:
                        intfunc('int',s[1],round(simple_eval(ss)))
                elif s[0] == 'float':
                    if is_arithmetic(ss) == True:
                        floatfunc('float',s[1],simple_eval(ss))
                elif s[0] == 'bool':
                    boolfunc('bool',s[1],(s[3]))
                elif s[0] == 'str':
                    strfunc(s[1],s[3::])
        if language_input in KV:
            print(KV[language_input])


    except Exception as e:
        print(f"Error{e} in line 76")
    if language_input == 'exit':
        break
    try:
        pass
    except Exception as e:
        print(f"Error{e} in line 82")

        pass
    try:
        a = is_arithmetic(s[0])
        if a == True:
            print(simple_eval(s[0]))

    except Exception as e:
        pass
