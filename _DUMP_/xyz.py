
# n = int(input("Enter value of n:  "))

# l = [0,1]
# for i in range(n-1):
#     l.append(l[-1] + l[-2])
# print(l[n])
    
#===================================================================================================================

# Code has a bug

def calculate(string):


    eligibility = ["True", "none"]
    brac_map = {")":"("}
    brac_array = []


    for index, d in enumerate(string):
        print(d, end=" ")

        if d == ")":

            if (brac_array) and (brac_array[-1] == brac_map[d]) and (string[index - 1] not in ["+", "-", "/", "*", "%"]):
                brac_array.pop()
                print("matched", end=" ")
            else:
                eligibility[0], eligibility[-1] = "False", "parenthesis error"

        elif d == "(" and (string[index + 1] not in ["+", "-", "/", "*", "%"]):
            brac_array.append(d)

    else:
        eligibility[0], eligibility[-1] = f"{bool(brac_array)}", "parenthesis error"


    if eligibility[0] == "True":
        result = eval(string)

    elif eligibility[0] == "False":
        if eligibility[-1] == "parenthesis error":
            result = "Invalid Parenthesis"


    return result


string = "(1+) + (2) * 3"
r = calculate(string)
print("\n", r)


