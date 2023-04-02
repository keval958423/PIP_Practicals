#STUDENT ID: 20CE067
#STUDENT NAME: ANERI PANCHAL
#AIM: PRACTICAL-7
#GITHUB LINK: https://github.com/AneriP02/PIP_Practicals.git

def is_lapindrome(s):
    return sorted(s[:len(s)//2]) == sorted(s[(len(s)+1)//2:])

t = int(input())

for i in range(t):
    text = input()
    print("YES" if is_lapindrome(text) else "NO")
