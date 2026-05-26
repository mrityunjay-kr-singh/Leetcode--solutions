def main():
    s = "abab"
    string1 = ""
    string2 = ""
    ans = ""
    for i in range(0,len(s)-1):
        string1 = string1 + s[i]
        string2 = string1
        while(len(string2)<len(s)):
            string2+=string1
        if(string2 == s):
            ans = string2
    if(ans==s):
        print(True)
    else:
        print(False)
main()                    
    
    