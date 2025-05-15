value_1=int(input("Enter the first number"))
value_2=int(input("Enter the second number"))



def fn_calculate(value_1,value_2):
    add_res=value_1 + value_2
    sub_res=value_1 - value_2
    mul_res=value_1 * value_2
    div_res=value_1/value_2
    print(f"Addition:{add_res}")
    print(f"Subtraction:{sub_res}")
    print(f"Multiplication:{mul_res}")
    print(f"Division:{div_res}")

fn_calculate(value_1,value_2)