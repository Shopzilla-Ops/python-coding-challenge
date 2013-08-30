calc_operators = ['+','-','/','*']

def get_nums():
    num1 = float(raw_input("Enter your first number: "))
    oper = "none"
    while oper not in calc_operators:
        oper = str(raw_input("Enter either + , - , /, * "))
    num2 = float(int(raw_input("Enter your second number: ")))
    answer = do_calc(num1,oper,num2)
    return answer

def do_calc(num1,oper,num2):
    if oper == "+":
        answer = num1+num2
    elif oper == "-":
        answer = num1-num2
    elif oper == "/":
        answer = num1/num2
    elif oper == "*":
        answer = num1*num2
    return answer

def main():
    print get_nums()

main()    
