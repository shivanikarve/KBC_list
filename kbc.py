question_list=[
    "how many continents are there ?",       
    "what is the capital of india?",          
    "Ng mei kon se course padhaya jaata hai",  
]
option_list=[
    ["Four", "nine", "seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"],
]
solution_list=[3,4,1]
ans=["seven","delhi","softwvare engineering"]
i=0
count=0
while i<len(question_list):
    m=question_list[i]
    print(m)
    j=0
    k=i
    while j<len(option_list[k]):
        d=option_list[k][j]
        print(j+1,option_list[k][j])
        j=j+1
    user_input=input("do you using lifeline")
    if user_input=="yes":
        print("5050")
        if count==0:
            print(option_list[i][i])
            print(ans[i])
            a=int(input("only now time using lifeline"))
            if a==2:
                print("your answer is correct")
                count=count+1
            else:
                print("you ans is wrong")
                break

        else:
            print("you can't use more lifeline")
            b=int(input("choose the answer"))
            if b==solution_list[i]:
                print("your ans is correct")
            else:
                print("your ans is wrong")
                break
    else:
        c=int(input("choose the answer"))
        if c==solution_list[i]:
            print("your answer is correct")
        else:
            print("your answer is wrong")
        i=i+1
