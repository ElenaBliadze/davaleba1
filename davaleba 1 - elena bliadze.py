#მეგობრებო, ქვემოთ კომენტარის სახედ მოცემულია დავალების პირობები. ყოველი ამოცანის ქვეშ დაწერეთ თქვენი პასუხი. პითონ ფაილის ჩამოტვირთვისას დააწერეთ davaleba 1 - elena bliadze.py 
# ოღონდ elena bliadze -ს ნაცვლად თქვენი სახელი და გვარი. გისურვებთ წარმატებას !



# 1.	დაწერეთ კოდი, რომელიც გამოიტანს შემდეგ კითხვას „ What do you call a bear with no teeth? “  
# და პასუხად გამოუტანს „ A gummy bear!” ეცადე, რომ განალაგო ისინი ერთ ხაზზე.

# messg1 = " What do you call a bear with no teeth?"
# messg2  = "A gummy bear! "
# print(messg1,messg2)
# print(messg1 + messg2)


# # 2.	დაწერე პროგრამა, რომელიც მომხარებელს შეაყვანინებს ორ რიცხვს და შემდეგ შედეგად დაბეჭდავს („Total is :”, შედეგი)

# x = eval(input("Enter first numebr: "))
# y = eval(input("Enter second numebr: "))
# summ = x+y
# print(f"Total is : {summ }")

# # 3.	დაწერე პროგრამა, რომელიც მომხმარებელს შეაყვანინებს 3 რიცხვს.
# # შეაჯამებთ პირველი 2 რიცხვი და შემდგომ გაამრავლეთ მესამეზე. დაბეჭდეთ შედეგი და პრინტში მიუთითეთ თქვენთვის სასურველი ტექსტი.
# num1 = eval(input("Enter first numebr: "))
# num2 = eval(input("Enter second numebr: "))
# num3 = eval(input("Enter third numebr: "))
# oper = ( num1 + num2 ) * num3
# print("Operation result is : ", oper)

# # 4.	დაწერეთ პროგრამა, რომელიც მომხმარებელს კითხავს რამდენი პიცის ნაჭერი ქონდა და რამდენი შეჭამა. 
# # გამოითვალეთ რამდენი ნაჭერი დარჩა და შედეგი თქვენთვის სასურველი ფორმით გამოიტანეთ.
# total = int(input(" Total number of pizzas slices: "))
# slices = int(input(" Number of Eaten pizzas slices: "))
# darcha = total - slices
# print("Now you have: " , darcha)

# # 5.  1 კილოგრამში 2204 ფუნტია. შესთავაზეთ მომხმარებელს შეიყვანოს მისი წონა კილოგრამებში, ცოლო თქვენმა პროგრამამ გადაიყვანოს ის ფუტებში.
# kgint = float(input(" დაწერე წონა კგ-ებში: "))
# funt = 2204 * kgint
# print(f"შენს მიერ შემოყვანილი წონა : {kgint} გადაყვანილი წონა ფუნტებში {funt}")

# # 6. დაწერე მოცემული ბლოკისთვის პროგრამა if, else, elif ის გამოყენებით: ( სურათი განთავსებულია ცალკე)

# num = int(input("Enter your number: "))

# if num > 10 :
#     print("This is over 10")
    
# elif num == 10:
#     print("This is equal 10")

# else: print("This is under 10")


# # 7. შესთავაზეთ მომხმარებელს შეიყვანოს რიცხვები 10 დან 20 ის ჩათვლით. 
# # თუ რიცხვი მომხმარებლის მიერ შეყვანილი იქნება, მოცემული დიაპაზონიდან, პროგრამამ დაპრინტოს „Thank you” 
# # საწინააღმდეგო შემთხვევაში დაპრინტოს „Incorrect answer”.
# num = int(input("Enter your number between 10 and 20: "))
# if 10< num < 20 :
#      print("Thank you")
# else: print("Incorrect answer")
    

# # 8. შეაყვანინეთ მომხმარებელს მისი სახელი, გვარი და ასაკი. თუ ასაკი 18 წელია ან/ და მეტი მაშინ დაბეჭდეთ „(name) cavn vote “,
# # თუ 17 ის ტოლია  „ (name, surname) can learn to drive” , 
# # თუ 16 მაშინ „ (name) can go Trick-or Treating”.

# name = input("Enter your number: ")
# surname = input("Enter your number: ")
# age = int(input("Enter your age : "))

# if 18<= age <= 75  :
#     print(f"{name} can vote")
    
# elif age == 17:
#     print(f"{name} {surname} can learn to drive")

# elif age == 16: 
#     print(f"{name} can go Trick-or Treating")
    
# else: print("You are baby, or you are very old")


# # 9. შეაყვანინეთ მომხმარებელს ინფორმაცია ტემპერატურაზე ფარენგეიტებში და მოცემული ფორმულის მეშვეობით C=(F-32)*5/9 გადაიყვანე ცელსიუსში. არ დაგავიწყდეს განსაზღვრო სწორი შესაყვანი რიცხვის ტიპი.
# # შემდეგ გამოიყენე and, or , not , ასევე ორზე მეტი პირობის ქონის შესაძლებლობა და დაუბეჭდე რა შემთხვევაში შეიძლება რომ ქონდეს ქოლგა, ა რა შემთხვევაში უნდა ჩაიცვას თბილად ან თხლად. 
# # გამოიყენე შენი კრეატიულობა.

# tempf = float(input("Shemoiyvane ricxvi F-usshi: "))
# tempc = (tempf-32)*5/9

# if not tempc == 30:
#     if tempc >= 26:
#         print("Titqmis dzalian tskhela")       
# print ("Arc ise dzalian tskhela")

# if tempc < 18:
#     print("tsiva , tsvims daiwire qolga")
    
# elif tempc <18 or tempc>5:
#     print("Tsiva tbilad chaicvi")
    
# elif  tempc == 0 and tempc == 5:
#     print("Auicleblad chaicvi tbilad: ")

# else: print("Daazuste amindis prognozi: ")

#Hello
    


# 10. შემოაყვაანინე მომხმარებელს რიცხვები და შეამოწმე არიან კენტი თუ ლუწი, და 7 ზე გაყოფის შემთხვევაში რომელს აქვს ნაშთი, 2, 3, 4, 5 .
# მიფიქრე და დაუბეჭდე შენთვის სასურველი მესიჯები.

