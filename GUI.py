from tkinter import *
from tkinter.messagebox import *
import pyttsx3 as p


engine = p.init()

# some variables
font = ('Verdana', 22, 'bold')



# Functions
def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)


def all_clear():
    textField.delete(0, END)


def click_btn_function(event):
    print("button clicked")
    b = event.widget
    text = b['text']
    print(text)

    if text == "x":
        textField.insert(END, "*")
        return
    if text == '=':
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0, END)
            textField.insert(0, answer)
        except Exception as e:
            print("Error.....", e)
            showerror("Error....", e)

        return

    textField.insert(END, text)


def speck():
    import operator
    import speech_recognition as s_r
    engine = p.init()
    engine.say("Say expression to calculate")
    engine.runAndWait()

    print("Your speech_recognition version is: " + s_r.__version__)
    r = s_r.Recognizer()
    my_mic_device = s_r.Microphone()
    with my_mic_device as source:
        print("Say what you want to calculate, example: 3 plus 3")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    my_string = r.recognize_google(audio)
    print(my_string)
    def get_operator_fn(op):
        return {
            '+': operator.add,
            '-': operator.sub,
            'x': operator.mul,
            'divided': operator.__truediv__,
            'Mod': operator.mod,
            'mod': operator.mod,
            '^': operator.xor,
        }[op]

    def eval_binary_expr(op1, oper, op2):
        op1, op2 = int(op1), int(op2)
        return get_operator_fn(oper)(op1, op2)

    answer = eval_binary_expr(*(my_string.split()))
    print(answer)
    engine.say("The answer is")

    engine.say(int(answer))
    engine.runAndWait()

# creating a window


window = Tk()

window.title('Voice Based Calculator')
window.geometry('470x700')

# picture lable


pic = PhotoImage(file='img/cal.png')

headinglable = Label(window, image=pic)
headinglable.pack(side=TOP, pady=10)

# heading level
heading = Label(window, text='My Calulator', font=font, justify=CENTER)
heading.pack(side=TOP)

# textfiels
textField = Entry(window, font=font)

textField.pack(side=TOP, fill=X, pady=10, padx=10)

# buttons
buttonFrame = Frame(window)
buttonFrame.pack()

# adding button
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief='ridge', activebackground='pink',
                     activeforeground='white')
        btn.grid(row=i, column=j, padx=3, pady=3)
        temp = temp + 1
        btn.bind('<Button-1>', click_btn_function)

zerobtn = Button(buttonFrame, text='0', font=font, width=5, relief='ridge', activebackground='pink',
                 activeforeground='white')
zerobtn.grid(row=3, column=1, padx=3, pady=3)

equalbtn = Button(buttonFrame, text='=', font=font, width=5, relief='ridge', activebackground='pink',
                  activeforeground='white')
equalbtn.grid(row=3, column=2, padx=3, pady=3)

dotbtn = Button(buttonFrame, text='.', font=font, width=5, relief='ridge', activebackground='pink',
                activeforeground='white')
dotbtn.grid(row=3, column=0, padx=3, pady=3)

plusbtn = Button(buttonFrame, text='+', font=font, width=5, relief='ridge', activebackground='pink',
                 activeforeground='white')
plusbtn.grid(row=0, column=3, padx=3, pady=3)

minsbtn = Button(buttonFrame, text='-', font=font, width=5, relief='ridge', activebackground='pink',
                 activeforeground='white')
minsbtn.grid(row=1, column=3, padx=3, pady=3)

multbtn = Button(buttonFrame, text='*', font=font, width=5, relief='ridge', activebackground='pink',
                 activeforeground='white')
multbtn.grid(row=2, column=3, padx=3, pady=3)

divibtn = Button(buttonFrame, text='/', font=font, width=5, relief='ridge', activebackground='pink',
                 activeforeground='white')
divibtn.grid(row=3, column=3, padx=3, pady=3)

clrbtn = Button(buttonFrame, text='<-', font=font, width=11, relief='ridge', activebackground='pink',
                activeforeground='white', command=clear)
clrbtn.grid(row=4, column=0, padx=3, pady=3, columnspan=2)

allclrbtn = Button(buttonFrame, text='AC', font=font, width=11, relief='ridge', activebackground='pink',
                   activeforeground='white', command=all_clear)
allclrbtn.grid(row=4, column=2, padx=3, pady=3, columnspan=2)

# binding buttons
plusbtn.bind('<Button-1>', click_btn_function)
minsbtn.bind('<Button-1>', click_btn_function)
multbtn.bind('<Button-1>', click_btn_function)
divibtn.bind('<Button-1>', click_btn_function)
zerobtn.bind('<Button-1>', click_btn_function)
equalbtn.bind('<Button-1>', click_btn_function)
dotbtn.bind('<Button-1>', click_btn_function)


def handle_keypress1(event):
    print("Succesfully started")
    if event:
        speck()


def handle_keypress2(event):
    if event:
        engine.say("Exiting the program")
        window.destroy()



# Bind keypress event to handle_keypress()

window.bind("<space>" , handle_keypress1)

window.bind("<Escape>", handle_keypress2)


window.mainloop()
