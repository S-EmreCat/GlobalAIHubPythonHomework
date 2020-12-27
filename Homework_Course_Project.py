import sys


# ogrenci girisi için gerekli işlemler
def Student_SignIn():
    name='Saban Emre'
    surname='Cat'
    count=3
    while count>0:
        input_name=input("Please enter your name: ")
        input_surname=input("Please enter your surname: ")
        if name==input_name and surname==input_surname:
            print(f"Welcome {name} {surname}")
            break
        else:
            count-=1
            print(f"You have {count} tries left.")
            if count==0:
                print("Please try again later")
                sys.exit()
# kullanıcıdan derslerin alınıp liste oluşturulması
# almak istenilen ders sayısı foknsiyona gönderilir.
def Lessons_Selected(numberOfLessons,ders_listesi):
    selected_lessons=[]
    all_lessons=[]
    all_lessons=ders_listesi
    # for arg in args:
    #     all_lessons.append(arg)
    len_lessons=len(all_lessons)
    # print("ders sayısı: ",len_lessons)
    if numberOfLessons<3:
        raise "You failed in class"
    elif 3<=len_lessons<=5:
        print('*'*30+"\n"+"Selecting your lessons.\n"+'*'*30)
        for i in range(numberOfLessons):
            try:
                selected_lessons.append(all_lessons[i])
            except:
                raise "Wrong Choice. Try less than 5"
        print(f"Selected Lessons: {selected_lessons} ")
    
    return selected_lessons

# dersin harf notunu hesaplar
def Calculator_Grade():
    Exam_Notes={"midterm":'98',"final": "100","proje": "89"}
    midterm=int(Exam_Notes['midterm'])
    proje=int(Exam_Notes['proje'])
    final=int(Exam_Notes['final'])
    grade=midterm*0.3+final*0.5+proje*0.2
    if grade>=90:
        print(f"Grade is {grade} AA")
    elif grade<90 and grade>=70 :
        print(f"Grade is {grade} BB")
    elif grade<70 and grade>=50:
        print(f"Grade is {grade} CC")
    elif grade<50 and grade>=30:
        print(f"Grade is {grade} DD")   
    elif grade<30:
        print(f"Grade is ({grade}) less than 30 (FF).")


dersler=[]
Student_SignIn()
    
for i in range(5):
    ders=input(f"Course {i+1} name: ")
    dersler.append(ders)

print(f"All Lessons: ",dersler)

numberofLessons=int(input("Enter the number of courses you want to take: "))

Lessons_Selected(numberOfLessons=numberofLessons,ders_listesi=dersler)

harfnotu_dersi=input("Enter the lesson you want to learn your grade for: ")
Calculator_Grade()



