from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry('280x380')
root.resizable(0,0)
root.configure(background="black")

first=second=oper=None

def get_operator(op):
    global first,oper
    first=int(result_label['text'])
    oper=op
    result_label.config(text='')

def get_result():
    global first,second,oper

    second=int(result_label['text'])

    if oper=='+':
        result_label.config(text=str(first+second))

    elif oper=='-':
        result_label.config(text=str(first-second))

    elif oper=='*':
        result_label.config(text=str(first*second))

    else:
        if second==0:
            result_label.config(text="error")
        else:
            result_label.config(text=str(first/second))


def get_digit(digit):
    curr=result_label['text']
    new=curr+str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')


result_label=Label(root,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=7,pady=(50,25),sticky='w')
result_label.config(font=("verdana",30,'bold'))


btn7=Button(root,text='7',bg='green',fg='white',width=5,height=2,command=lambda :get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14))

btn8=Button(root,text='8',bg='green',fg='white',width=5,height=2,command=lambda :get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14))

btn9=Button(root,text='9',bg='green',fg='white',width=5,height=2,command=lambda :get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14))

btnAdd=Button(root,text='+',bg='green',fg='white',width=5,height=2,command=lambda :get_operator('+'))
btnAdd.grid(row=1,column=3)
btnAdd.config(font=('verdana',14))


btn4=Button(root,text='4',bg='green',fg='white',width=5,height=2,command=lambda :get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14))

btn5=Button(root,text='5',bg='green',fg='white',width=5,height=2,command=lambda :get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14))

btn6=Button(root,text='6',bg='green',fg='white',width=5,height=2,command=lambda :get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14))

btnSub=Button(root,text='-',bg='green',fg='white',width=5,height=2,command=lambda :get_operator('-'))
btnSub.grid(row=2,column=3)
btnSub.config(font=('verdana',14))


btn1=Button(root,text='1',bg='green',fg='white',width=5,height=2,command=lambda :get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14))

btn2=Button(root,text='2',bg='green',fg='white',width=5,height=2,command=lambda :get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14))

btn3=Button(root,text='3',bg='green',fg='white',width=5,height=2,command=lambda :get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14))

btnMul=Button(root,text='*',bg='green',fg='white',width=5,height=2,command=lambda :get_operator('*'))
btnMul.grid(row=3,column=3)
btnMul.config(font=('verdana',14))


btnClr=Button(root,text='C',bg='green',fg='white',width=5,height=2,command=lambda : clear())
btnClr.grid(row=4,column=0)
btnClr.config(font=('verdana',14))

btn0=Button(root,text='0',bg='green',fg='white',width=5,height=2,command=lambda :get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',14))

btnEq=Button(root,text='=',bg='green',fg='white',width=5,height=2,command=get_result)
btnEq.grid(row=4,column=2)
btnEq.config(font=('verdana',14))

btnDiv=Button(root,text='/',bg='green',fg='white',width=5,height=2,command=lambda :get_operator('/'))
btnDiv.grid(row=4,column=3)
btnDiv.config(font=('verdana',14))


root.mainloop()