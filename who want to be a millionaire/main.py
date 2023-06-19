            """ "Who want to be a billionaire" show
                        created by soban """


while True:
    print("""
            Wellcome to the Worlds BIGGEST show 
            \"WHO WANTS TO BE A BILLIONAIRE\"       
        """)
    x = input("Sir, Please tell us your name: \n ")   #asking name 

    print("So", x, "should we start out show \n" )      #permission to start
    y = input("type yes to start: \n")
    while y != "yes":
        y = input("say yes bastard: \n")
        match y:
            case "yes":
                break
            case _:
                continue
    print(""""\n", Mr. Beast will ask you some questions
                after every correct answer 5,000,000 $ will be addded to 
                your beast account (that doesnt even exists)""")
    print("\n", x, "be ready and cheating is allowed for people under 60 age")

    q1 = "who is the president of america in 2023"
    q2 = "who was the prime minister of pakistan in 2022"
    q3 = "what is the name of your father"
    q4 = "what is the best for web development"
    q5 = "which of the following is best programming language for making money"

    l1 = ["abama", "bush", "joe bijan", "tramp"]
    l2 = ["imran pathan", "shehbaz thulla", "bilawal tangain", "modi sandho"]
    l4 = ["python", "java", "html", "javascript"]
    l5 = ["python", "assembly", "brainf**k,", "javascript"]

    p = 0
    global i
    i = 0

    def ask():
        print("do you want to risk this money for next question")
        z1 = input("say yes to continue: \n")
        if(z1!="yes"):
            global i
            i = i + 1
            print("\n \n good buy")
            
            

    print("\n", x, "your first question is: \n", q1)
    print("here are the choices: \n", l1)
    a1 = input("type the correct spelling:\n \n")

    if(a1 == "joe bijan"):
        print("\n", x, "your answer is correct and you receive your 5 million $")
        p = p + 5000000
        print("your bank balance is", p)
        ask()
        if(i == 1):
                break
        else:
                "ok"
        
    else:
        print(x, "your answer is false the correct answer is \"joe bijan\"")
        p = p


    print("\n", x, "your second question is: \n", q2)
    print("and here are the choices: \n", l2)
    a2 = input("type the correct spelling:\n")

    if(a2 == "shehbaz thulla"):
        print("\n", x, "your answer is correct and you receive your another 5 million $")
        p = p + 5000000
        print("\n", "now your bank balance is", p)
        ask()
        if(i == 1):
                break
        else:
                "ok"
    else:
        print("\n", x, "your answer is false the correct answer is \"shehbaz thulla\"")
        p = p
        print("\n", "now your bank balance is still", p)
        ask()
        if(i == 1):
                break
        else:
                "ok"

   

    print("\n", x, "your third question is: \n", q3)
    print("and it has no choices :) \n")
    a3 = input("enter you real father name:\n")
    if(a3 == "soban"):
        print("\n", "you got the correct answer wow")
    else: 
        while a3 != "soban":
            a = input(("thats wrong answer \n enter my name \"soban\" to proceed in show and get double money: \n"))
            match a:
                case "soban":
                    print("\n", "thanks for changing your father here have a bonus 10 million")
                    p = p + 10000000
                    break
                case _:
                    print("\n", "thats wrong answer \n enter my name \"soban\"to proceed in show and get double money")
    print("\n", "your bank balance is", p)
    ask()
    if(i == 1):
                break
    else:
                "ok"



    print("\n", x, "your fourth question is: \n", q4)
    print("and here are the choices: \n", l4)
    a4 = input("type the correct spelling:\n")

    if(a4 == "html"):
        print("\n", x, "your answer is correct and you receive your another 5 million $")
        p = p + 5000000
        print("\n", "your bank balance is", p)
        ask()
        if(i == 1):
                break
        else:
                "ok"
        

    else:
        print("\n", x, "html is the only best language for web development and it is the best \n you better get out of the show")
        p = p
        print("\n", "now your bank balance is still", p)
        ask()
        if(i == 1):
                break
        else:
                "ok"
        


    


    print("\n", x, "your last question is: \n", q5)
    print("and here are the choices: \n", l5)
    a5 = input("type the correct spelling:\n")

    if(a5 == "python"):
        print("\n", x, "your answer is correct and you receive your another 5 million $")
        p = p + 5000000
        break
    else:
        print("\n", x, "wtf man its wrong")
        p = p
        break

print("\n", "your award is ", p)
print("\n", "thanks for playing with us you can play anytime again", "\n")
