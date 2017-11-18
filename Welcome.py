from tkinter import *
from PIL import Image, ImageTk


def raise_frame(frame):
    frame.tkraise()


root = Tk()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f6 = Frame(root)


for frame in (f1, f2, f3, f4,f5,f6):
    frame.grid(row=0, column=0, sticky='news')

Button(f1, text='Never Came', command=lambda:raise_frame(f2)).pack(padx=50,pady=50)
#Label(f1, text='FRAME 1').pack()
Button(f1, text='Came Before', command=lambda:raise_frame(f3)).pack(padx=50,pady=50)


photo = ImageTk.PhotoImage(Image.open("C:\\Users\\User\\Downloads\\sighthound-cloud-tutorial\\code-samples\\python\\Icon-06.jpg")) #path is input
label = Label(f3, image=photo)
label.pack()
Name=Label(f3,text="Gan Ziy En")
Age=Label(f3,text="19 years old")
Disease=Label(f3,text="Threesome")

Name.place(x=20,y=20)
Age.place(x=20,y=40)
Disease.place(x=20,y=60)

Done=Button(f3, text='Recognition Done', command=lambda:  raise_frame(f4))
Done.place(x=130, y=170)

label_1=Label(f2, text='Please take at least 20 photos for registration',bg="white",fg="black",font=100).pack(padx=100,pady=300)

Label(f4, text='Hospital FaceHack',font=100).pack(padx=200)
label_2=Label(f4,text="Doctor's name: ").pack()
entry_2=Entry(f4).pack()
label_3=Label(f4,text="Disease: ").pack()
entry_3=Entry(f4).pack()
label_4=Label(f4,text="Remarks: ").pack()
entry_4=Entry(f4).pack()
label_14=Label(f4,text="Appointment date: ").pack()
entry_14=Entry(f4).pack()

Button(f4, text='Record', command=lambda:raise_frame(f5)).pack()

label_5=Label(f5,text="Laboratory",font=100).pack(padx=200)
label_6=Label(f5,text="Blood Pressure: ").pack()
entry_6=Entry(f5).pack()
label_7=Label(f5,text="Heart Pulse: ").pack()
entry_7=Entry(f5).pack()
label_8=Label(f5,text="Weight: ").pack()
entry_8=Entry(f5).pack()
label_9=Label(f5,text="Height: ").pack()
entry_9=Entry(f5).pack()
label_10=Label(f5,text="Remark: ").pack()
entry_10=Entry(f5).pack()
Button(f5, text='Record', command=lambda:raise_frame(f6)).pack()

photo_2 = ImageTk.PhotoImage(Image.open("C:\\Users\\User\\Downloads\\sighthound-cloud-tutorial\\code-samples\\python\\Icon-06.jpg")) #path is input
label_11 = Label(f6, image=photo_2)
label_11.pack()
label_12 = Label(f6,text="Biling")
Name=Label(f6,text="Gan Ziy En")
Age=Label(f6,text="19 years old")

label_13=Label(f6,text="Payment Done!")

Name.place(x=20,y=20)
Age.place(x=20,y=40)
label_12.place(x=100,y=10)
label_13.place(x=505,y=500)




# label_2.grid(row=1,sticky=E)
# label_3.grid(row=2,sticky=E)
# label_4.grid(row=3,sticky=E)
#
# entry_2.grid(row=1,column=1)
# entry_3.grid(row=2,column=1)
# entry_4.grid(row=3,column=1)



raise_frame(f1)

root.mainloop()