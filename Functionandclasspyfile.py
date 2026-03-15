class Allinoneclass():
    def subfields():
        print("Sub-fields in AI are:")
        Fields= ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for temp in Fields:
            print(temp)

    def OddEven():
        div=int(input("Enter a number:"))
        if(div%2==0):
            print(div,"is Even number")
        else:
            print(div,"is Odd number")

    def Elegible():
        gen=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gen == "Male" and age >= 21):
            print("ELIGIBLE")
        elif(gen == "Female" and age >= 18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        Subject1=int(input("Subject1="))
        Subject2=int(input("Subject2="))
        Subject3=int(input("Subject3="))
        Subject4=int(input("Subject4="))
        Subject5=int(input("Subject5="))
        SumTablelist=[Subject1,Subject2,Subject3,Subject4,Subject5]
        Totalmark=sum(SumTablelist)
        countofsubject=len(SumTablelist)
        print("Total :",Totalmark)
        Percentage=Totalmark/countofsubject
        print("Percentage :",Percentage)
    
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        Triangle=(Height*Breadth)/2 
        print("Area of Triangle:",Triangle)
        Height1=int(input("Height1:")) 
        Height2=int(input("Height2:")) 
        Breadth=int(input("Breadth:"))
        Perimeter=Height1+Height2+Breadth 
        print("Perimeter of Triangle:",Perimeter)

            