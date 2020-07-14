def helps():
    print("The program calculates the sum and the substration of numbers")


def exits():
    print("Bye!")  
    exit()  


def split_string(string):
    string = string.replace("^","**").split()
    numbers = [string[0]]

    for s in string[1:len(string)+1]: # len(string)
        if s.isnumeric():
            numbers.append(s)
        elif s in "+-" and s.count(s) == 1:
            numbers.append(s)
        elif "-" in s and s.count("-") % 2 == 0:
            numbers.append("+")
        elif "-" in s and s.count("-") % 2 == 1:
            numbers.append("-")
        elif "+" in s:
            numbers.append("+")
    
    return "".join(numbers)


def replace_var(numbers):
    ret = []
    error = 0
    y = 0
    for i in numbers:
        if i.isnumeric() or i in "-+*/()":
            if i == "/" and numbers[y + 1] == "/":
                error = 1
                break
            else:
                ret.append(str(i))
        else:
            if i in dict_variables.keys():
                ret.append(str(dict_variables[i]))
            else:
                error = 1
                break
        y += 1
    if error == 0:
        return "".join(ret)
    return "1"
    
    
    


def smart_calculator(string="0"):
    numbers = split_string(string)
    retorno = replace_var(numbers)
    #print(retorno)
    if retorno == "1":
        print("Invalid expression")
    else:

            try:
                print(int(eval(retorno)))
            except SyntaxError:
                print("Invalid expression")
            except NameError:
                print("Invalid expression")


def val_variable(variables="0"):
    
    num1, num2 = 0, 0
    if variables.count("=") > 1:
        print("Invalid assignment")
    elif variables.count("=") == 1:
        num1, num2 = variables.replace(" ","").split("=")
        if num1.isalpha() and num2.isnumeric():
            dict_variables[num1] = int(num2)
        elif num2.isalpha() and num2 in dict_variables.keys():
            dict_variables[num1] = dict_variables[num2]
        elif num2.isalpha() and num2 not in dict_variables.keys():
            print("Unknown variable")
        else:
            print("Invalid assignment")
    elif variables.isalnum() and not variables.isalpha() and not variables.isnumeric():
        print("Invalid assignment")
    
    else:
        if variables.isnumeric():
            print(variables)
        elif variables not in dict_variables.keys():
            print("Unknown variable")
        else:
            print(dict_variables[variables])



def main():
    
    while True:
        string = input().strip()
        if string.startswith("/"):
            if string == "/exit":
                exits()
            elif string == "/help":
                helps()
            else:
                print("Unknown command")
        elif string != "":

            if "=" in string or string.isalnum():
                val_variable(string)  # validar asignacion de variables
            else:
                smart_calculator(string.replace(" ",""))
        
        #print(dict_variables)


# global    
dict_variables = dict()
main()
