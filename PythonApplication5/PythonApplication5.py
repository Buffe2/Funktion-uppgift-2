a = int(input("Hur stor vill du boxen ska vara?"))

def box(a):
    print(a*"==="+"======")
    for i in range(a):
        print("||", a*"   ", "||")
    print(a*"==="+"======")

box(a)