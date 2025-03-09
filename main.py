from tkinter import *




screen=Tk()
screen.title("BMI Calculator")
screen.minsize(width=300,height=300)
screen.resizable(False,False)
screen.config(bg="light blue")


size_label=Label(text="Enter Your Height"+"(cm)",width=17)
size_label.config(bg="light blue")
size_label.place(x=150-62,y=45)

kilogram_label=Label(text="Enter Your Weight"+"(kg)",width=17)
kilogram_label.config(bg="light blue")
kilogram_label.place(x=150-62,y=130)

warningMessageLabel=Label(text="Hoşgeldiniz! ")
warningMessageLabel.config(bg="light blue")
warningMessageLabel.place(x=110,y=230)


entry_size=Entry()
entry_size.place(x=150-62,y=75-19/2)
entry_size.update()
print(entry_size.winfo_height())
print(entry_size.winfo_width())



entry_kilogram=Entry()
entry_kilogram.place(x=150-62,y=150)

def Calculator():

    if entry_size.get() =="":
        try:
            warningMessageLabel.config(text="Lütfen gerekli alanları boş bırakmayınız!!")
            warningMessageLabel.place(x=0, y=230)
            return
        except ValueError:
            warningMessageLabel.config(text="Beklenmedik Hata")
    if entry_kilogram.get() =="":
        try:
            warningMessageLabel.config(text="Lütfen gerekli alanları boş bırakmayınız!!")
            warningMessageLabel.place(x=0, y=230)
            return
        except ValueError:
            warningMessageLabel.config(text="Beklenmedik Hata")
    try:
        float(entry_kilogram.get())
        float(entry_size.get())
    except ValueError:
        warningMessageLabel.config(text="Lütfen geçerli bir sayı giriniz!!")
        warningMessageLabel.place(x=0, y=230)
    try:
        if float(entry_kilogram.get())<0 or float(entry_size.get())<0:
            warningMessageLabel.config(text="Lütfen geçerli bir sayı giriniz!!")
            warningMessageLabel.place(x=0, y=230)
            return
    except ValueError:
        warningMessageLabel.config(text="Lütfen geçerli bir sayı giriniz!!")
        warningMessageLabel.place(x=0, y=230)
    sonuc =int(entry_kilogram.get())/(int(entry_size.get())/100)**2
    if sonuc <18.5:
        warningMessageLabel.config(text=f"BMI değeriniz :{sonuc:.1f} Kategoriniz :ZAYIF")
        warningMessageLabel.place(x=0, y=230)
        warningMessageLabel.config(fg="red")
    elif 18.5<= sonuc <24.9 :
        warningMessageLabel.config(text=f"BMI değeriniz :{sonuc:.1f} Kategoriniz :NORMAL KİLO")
        warningMessageLabel.place(x=0, y=230)
        warningMessageLabel.config(fg="green")
    elif 24.9<= sonuc <29.9 :
        warningMessageLabel.config(text=f"BMI değeriniz :{sonuc:.1f} Kategoriniz :FAZLA KİLOLU")
        warningMessageLabel.place(x=0, y=230)
        warningMessageLabel.config(fg="red")
    elif 29.9<= sonuc <34.9 :
        warningMessageLabel.config(text=f"BMI değeriniz :{sonuc:.1f} Kategoriniz :1.DERECE OBEZİTE")
        warningMessageLabel.place(x=0, y=230)
        warningMessageLabel.config(fg="red")
    elif 34.9<= sonuc <39.9 :
        warningMessageLabel.config(text=f"BMI değeriniz :{sonuc:.1f} Kategoriniz :2.DERECE OBEZİTE")
        warningMessageLabel.place(x=0, y=230)
        warningMessageLabel.config(fg="red")
    elif 39.9<=sonuc :
        warningMessageLabel.config(text=f"BMI değeriniz :{sonuc:.1f} Kategoriniz :3.DERECE OBEZİTE \n (MORBİD OBEZİTE)")
        warningMessageLabel.place(x=0, y=230)
        warningMessageLabel.config(fg="red")

button=Button(text="Calculate",command=Calculator)
button.config(bg="cyan",fg="green")
button.place(x=150-30,y=188)
entry_size.focus()
screen.mainloop()
