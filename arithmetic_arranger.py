def arithmetic_arranger(problems, answers=None):
    import itertools
    #initiate lists
    num1, op, num2, ans = ([] for i in range(4))
    line1, line2, line3, line4 = "", "", "", ""
    #iterate through problems, creating 3 lists
    if len(problems) > 5:
        return "Error: Too many problems."
    for iprob in problems:
        x = iprob.split()
        num1.append(x[0])
        op.append(x[1])
        num2.append(x[2])
    #return num1, op, num2
    for n in num1:
        if not n.isdigit():
            return "Error: Numbers must only contain digits."
    for n in num2:
        if not n.isdigit():
            return "Error: Numbers must only contain digits."
    # get solutions
    for (a, b, c) in zip(num1, op, num2):
        if len(a) > 4 or len(c)>4:
            return "Error: Numbers cannot be more than four digits."
        if b == "+":
            ans.append(int(a)+int(c))
        elif b == "-":
            ans.append(int(a)-int(c))
        elif b != "+" or b != "-":
            return "Error: Operator must be '+' or '-'."
    for (a, b, c, d) in zip(num1, op, num2, ans):
        length = max(len(a),len(c)) + 2
        line1 += str(a).rjust(length) + "    "
        line2 += (str(b) + str(c).rjust(length-1)+"    ")
        for n in range(length):
            line3 += "-"
        line3 += "    "
        line4 += str(d).rjust(length) + "    "

    if answers:
        arranged_problems = line1.rstrip() + "\n" + line2.rstrip() +"\n" + line3.rstrip() + "\n" + line4.rstrip()
    else:
        arranged_problems = line1.rstrip() + "\n" + line2.rstrip() +"\n" + line3.rstrip()

    return arranged_problems
