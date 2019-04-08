from tkinter import *
from tkinter import ttk
import Conjugaison


# 初始化
root = Tk()
root.title("Conjugaison Française")
root.withdraw()
qa = []
incorrect = 0


# 更改测试类型
def update_now(*args):
    global qa
    global incorrect
    qa = Conjugaison.update_now(comboxlist.get())
    incorrect = 0
    lemmetext.set(qa[0])
    reponse.set("")

    if comboxlist.get() != "Participe Passé" and comboxlist.get() != "Participe Présent":
        personne = qa[2]
        if personne == 0:
            p = "Je"
        elif personne == 1:
            p = "Tu"
        elif personne == 2:
            p = "Il/Elle"
        elif personne == 3:
            p = "Nous"
        elif personne == 4:
            p = "Vous"
        elif personne == 5:
            p = "Ils/Elles"
        reponseLabelText.set("réponse: (" + p + ")")
    else:
        reponseLabelText.set("réponse: ")


# 检查输入答案
def veri(*args):
    global qa
    global incorrect

    if reponse.get() == qa[1]:
        message.set("C'est correct! Bon courage!")
        update_now()
    elif reponse.get() != qa[1] and qa[1].find(";") > 0:
        qa_list = qa[1].split(";")
        __flag = 0
        for qa_item in qa_list:
            if reponse.get() == qa_item:
                __flag = 1
        if __flag == 1:
            message.set("C'est correct! (" + qa[1] + ")")
            update_now()
        else:
            incorrect += 1
            if incorrect < 4:
                message.set("Ce n'est pas correct!")
            else:
                message.set("La réponse possible est: " + qa[1])
    else:
        incorrect += 1
        if incorrect < 4:
            message.set("Ce n'est pas correct!")
        else:
            message.set("La réponse correcte est: " + qa[1])


# 固定文字标签
lettreEntry = Label(root, text="")
lettreEntry.grid(row=0, column=0, columnspan=2, padx=25, pady=0, sticky=W+E)
Label(root, text="type de conjugaison").grid(row=1, column=0, padx=25, pady=10)
Label(root, text="lemme").grid(row=3, column=0, padx=25, pady=10)
reponseLabelText = StringVar()
reponseLabelText.set("réponse")
reponseLabel = Label(root, textvariable=reponseLabelText)
reponseLabel.grid(row=4, column=0, padx=25, pady=10)

# 功能选择下拉框
typec = StringVar()
comboxlist = ttk.Combobox(root, textvariable=typec, state='readonly')
comboxlist.grid(row=1, column=1, padx=35, pady=10)
comboxlist['values'] = ("Indicatif Présent",
                        "Participe Passé",
                        "Participe Présent",
                        "Indicatif Futur Simple",
                        "Indicatif Imparfait",
                        "Indicatif Passé Simple",
                        "Indicatif Futur Simple",
                        "Conditionnel Présent",
                        "Subjonctif Présent",
                        "Subjonctif Imparfait",
                        "Impératif Présent")
comboxlist.current(0)
comboxlist.bind("<<ComboboxSelected>>", update_now)

# 问题显示区
lemmetext = StringVar()
lemme = Label(root, textvariable=lemmetext, font=('Helvetica', '14', 'bold'))
lemme.grid(row=3, column=1, padx=35, pady=10)

# 答案输入
reponse = StringVar()
entryreponse = Entry(root, textvariable=reponse)
entryreponse.grid(row=4, column=1, padx=35, pady=10, sticky=W+E)
entryreponse.bind("<Return>", veri)

# 文字提示
message = StringVar()
message.set("Bonjour!")
message_lable = Label(root, textvariable=message, font=('Helvetica', '14', 'bold'))
message_lable.grid(row=5, column=0, columnspan=2, padx=25, pady=30)

frame = Frame(root)
frame.grid(row=6, column=0, columnspan=2, padx=25, pady=0)
button1 = Button(frame, text="à", command=lambda: entryreponse.insert(entryreponse.index(INSERT), "à"))
button1.grid(row=0, column=0, pady=0, padx=3, sticky=W+E)
button2 = Button(frame, text="â", command=lambda: entryreponse.insert(entryreponse.index(INSERT), "â"))
button2.grid(row=0, column=1, pady=0, padx=3, sticky=W+E)
button3 = Button(frame, text="è", command=lambda: entryreponse.insert(entryreponse.index(INSERT), "è"))
button3.grid(row=0, column=2, pady=0, padx=3, sticky=W+E)
button4 = Button(frame, text="é", command=lambda: entryreponse.insert(entryreponse.index(INSERT), "é"))
button4.grid(row=0, column=3, pady=0, padx=3, sticky=W+E)
button5 = Button(frame, text="ê", command=lambda: entryreponse.insert(entryreponse.index(INSERT), "ê"))
button5.grid(row=0, column=4, pady=0, padx=3, sticky=W+E)
button6 = Button(frame, text="î", command=lambda: entryreponse.insert(entryreponse.index(INSERT), "î"))
button6.grid(row=0, column=5, pady=0, padx=3, sticky=W+E)
button7 = Button(frame, text="ï", command=lambda: entryreponse.insert(entryreponse.index(INSERT), "ï"))
button7.grid(row=0, column=6, pady=0, padx=3, sticky=W+E)
button8 = Button(frame, text="ô", command=lambda: entryreponse.insert(entryreponse.index(INSERT), "ô"))
button8.grid(row=0, column=7, pady=0, padx=3, sticky=W+E)
button9 = Button(frame, text="ö", command=lambda: entryreponse.insert(entryreponse.index(INSERT), "ö"))
button9.grid(row=0, column=8, pady=0, padx=3, sticky=W+E)
button10 = Button(frame, text="ù", command=lambda: entryreponse.insert(entryreponse.index(INSERT), "ù"))
button10.grid(row=0, column=9, pady=0, padx=3, sticky=W+E)
button11 = Button(frame, text="û", command=lambda: entryreponse.insert(entryreponse.index(INSERT), "û"))
button11.grid(row=0, column=10, pady=0, padx=3, sticky=W+E)
button12 = Button(frame, text="ü", command=lambda: entryreponse.insert(entryreponse.index(INSERT), "ü"))
button12.grid(row=0, column=11, pady=0, padx=3, sticky=W+E)
button13 = Button(frame, text="ç", command=lambda: entryreponse.insert(entryreponse.index(INSERT), "ç"))
button13.grid(row=0, column=12, pady=0, padx=3, sticky=W+E)
button14 = Button(frame, text="œ", command=lambda: entryreponse.insert(entryreponse.index(INSERT), "œ"))
button14.grid(row=0, column=13, pady=0, padx=3, sticky=W+E)

lettreEntry2 = Label(root, text="")
lettreEntry2.grid(row=7, column=0, columnspan=2, padx=25, pady=3, sticky=W+E)

# 窗口居中显示
root.update()
root.deiconify()
root.withdraw()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
ww = root.winfo_width()
wh = root.winfo_height()
gx = (sw - ww) / 2
gy = (sh - wh) / 2 - 50
# print(sw, sh, ww, wh, gx, gy)
root.geometry("+%d+%d" % (gx, gy))
root.deiconify()

update_now()
root.mainloop()


