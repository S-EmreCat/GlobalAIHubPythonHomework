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
#kullanıcıdan derslerin alınıp liste oluşturulması
def Lessons(*args):
    lessons=[]
    for arg in args:
        lessons.append(arg)
    # print(lessons)
    # print(len(lessons))
    return(len(lessons))

# almak istenilen ders sayısı foknsiyona gönderilir.
def Lessons_Selected(numberOfLessons):
    selected_lessons=[]
    lessons_value=Lessons('lesson 1','lesson 2','lesson 3','lesson 4','lesson 5')
    if numberOfLessons<3:
        raise "You failed in class"
    elif 3<=lessons_value<=5:
        print('*'*30+"\n"+"Selecting your lessons.\n"+'*'*30)
        for i in range(numberOfLessons):
            selected_lessons.append('lesson '+str(i+1))
        print(selected_lessons)

def not_hesapla():
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
Student_SignIn()
Lessons_Selected(3)
not_hesapla()