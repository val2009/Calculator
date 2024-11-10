import time
RED = '\033[31m'
BLUE = '\033[34m'
TURQUOISE = '\033[36m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'
while True:
    print(f"{BLUE}Calculatrice")
    while True:
        try:
            num1 = float(input(f"{TURQUOISE}1er nombre : "))
            break 
        except ValueError:
            print(f"{RED}ERROR :{YELLOW} Veuillez entrer un nombre.")

    while True:
        try:
            num2 = float(input(f"{TURQUOISE}2ème nombre : "))
            break  
        except ValueError:
            print(f"{RED}ERROR :{TURQUOISE} Veuillez entrer un nombre.")
    while True:
        i = input(f"Choisissez un calcule :{BLUE} \n+\n-\n*\n/\n")
        if i == "+":
            ans = num1 + num2
            break

        elif i == "-":
            ans = num1 - num2
            break

        elif i == "*":
            ans = num1 * num2
            break

        elif  i == "/": 
            if num2 != 0:
                ans = num1 / num2
                break
            elif num2 == 0:
                print(f"{RED}ERROR : {YELLOW}le deuxième nombre ne peut être égale a zero.")
                continue
        else:
            print(f"{RED}ERROR : {YELLOW}Veuillez rentrer un signe valable.")
            continue
                
    
    print(f"{GREEN}réponse:{RESET}", ans)
    time.sleep(2)

    while True:
        x = input(f"{TURQUOISE}Appuyez sur [x] pour continuer.\nOu\nEntrez 'exit' pour quitter.\n")
        if x.lower() == "exit" :
            break
        elif x.lower() == "x":
            break
        else:
            print(f"{RED}ERROR : {YELLOW}Entrée non valide. Veuillez réessayer.")
    if x.lower() == "exit" :
        break
    else:
        continue


