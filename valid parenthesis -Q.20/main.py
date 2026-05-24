# Question No. 20 :- Valid Parenthesis.

def main():
    s = "({[]})"
    stack = []
    for i in range(0,len(s)):
        stack.append(s[i])
        if(len(stack)<=1):
            continue
        elif(stack[-2]=="(" and stack[-1]==")"):
            stack.pop()
            stack.pop()
        elif(stack[-2]=="[" and stack[-1]=="]"):
            stack.pop()
            stack.pop()
        elif(stack[-2]=="{" and stack[-1]=="}"):
            stack.pop()
            stack.pop()
    if(len(stack)==0):
        print(True)
    else:
        print(False)
main()        