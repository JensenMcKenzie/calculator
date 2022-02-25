#hey
def hasSubtraction (s) :
    for i in range(0, len(s)) :
        before = False
        after = False
        if s[i] == '-' :
            if s[i+1].isdigit() :
                after = True
            if s[i-1].isdigit() and i-1 >= 0:
                before = True
            if before and after :
                return True, i;
    return False;

def checkOperations (s) :
    if hasSubtraction(s):
        return True
    if s.find("(") != -1 or s.find("^") != -1 or s.find("*") != -1 or s.find("/") != -1 or s.find("+") != -1 :
        return True;
    return False;

def getOperation (s) :
    if s.find("(") != -1 :
        return "P"
    elif s.find("^") != -1 :
        return "E"
    elif s.find("*") != -1 :
        return "M"
    elif s.find("/") != -1 :
        return "D"
    elif s.find("+") != -1 :
        return "A"
    elif s.find("-") != -1 :
        return "S"

def getTerms (s, index) :
    first = ""
    second = ""
    start = -1
    end = -1
    current = index + 1
    try:
        done = False
        while (s[current].isdigit()  or s[current] == "." or s[current] == "-") and current <= len(s) -1 and not done:
            if s[current] == '-' :
                if s[current-1].isdigit():
                    done = True
                    current -= 1
                else :
                    second += s[current]
            else :
                second += s[current]
            current += 1
        if s[current] == '-' :
            current -= 1
    except IndexError :
        pass
    end = current
    current = index - 1
    while (s[current].isdigit()  or s[current] == "." or s[current] == "-") and current >= 0:
        first = s[current] + first
        current -= 1
        if s[current] == '-' :
            first = "-" + first
            break
    if float(first) < 0 :
        start = current
    else :
        start = current + 1
    return first, second, start, end

solved = list()
answers = list()

def replaceStuff(start, finish, st, s) :
    if not start == 0 and not st[0] == '-' and s[start-1].isdigit():
        st = '+' + st
        return s.replace(s[start:finish], st, 1)
    else :
        return s.replace(s[start:finish], st, 1)

def parse (s, p = False, ps = "") :
    if p == False :
        for i in range(0, len(solved)) :
            if s.find(solved[i]) != -1 :
                s = s.replace(solved[i],answers[i])
    print(s)
    if checkOperations(s):
        op = getOperation(s)
        if op == "P" and p == False:
            one = s.find("(")
            two = s.find(")")
            print("Solving parentheses: " + s[one:two+1])
            ps = s[one:two+1]
            parse(s[one+1:two], True,ps)
        elif op == "E" :
            index = s.find("^")
            arr = getTerms(s , index)
            operation = float(arr[0]) ** float(arr[1])
            print("Exponent: " + s[arr[2]:arr[3]+1] + " = " + str(operation))
            s = replaceStuff(arr[2], arr[3]+1, str(operation), s)
        elif op == "M" :
            index = s.find("*")
            arr = getTerms(s , index)
            operation = float(arr[0]) * float(arr[1])
            print("Multiplication: " + s[arr[2]:arr[3]+1] + " = " + str(operation))
            s = replaceStuff(arr[2], arr[3]+1, str(operation), s)
        elif op == "D" :
            index = s.find("/")
            arr = getTerms(s , index)
            operation = float(arr[0]) / float(arr[1])
            print("Division: " + s[arr[2]:arr[3]+1] + " = " + str(operation))
            s = replaceStuff(arr[2], arr[3]+1, str(operation), s)
        elif op == "A" :
            index = s.find("+")
            arr = getTerms(s , index)
            operation = float(arr[0]) + float(arr[1])
            print("Addition: " + s[arr[2]:arr[3]+1] + " = " + str(operation))
            s = replaceStuff(arr[2], arr[3]+1, str(operation), s)
        elif op == "S":
            index = hasSubtraction(s)[1]
            arr = getTerms(s , index)
            operation = float(arr[0]) - float(arr[1])
            print("Subtraction: " + s[arr[2]:arr[3]+1] + " = " + str(operation))
            s = replaceStuff(arr[2], arr[3]+1, str(operation), s)
        return parse(s,p,ps)
    else :
        if p :
            answers.append(s)
            solved.append(ps)
            p = False
            ps = ""
            print("Parentheses solved")
        else :
            print("Done")

while True :
    st = input("Enter an equation to be solved: ")
    st = st.replace(" ", "")
    parse(st)
    done = input("\nWould you like to enter another problem? (Y or N): ")
    print()
    if done == "N" or done == "n" :
        print("Application closed.")
        break