from tkinter import *
    

window = Tk()
window.title("대출 계산기")
    
l1 = Label(window, text = "연이율")
l1.grid(row = 1, column = 1)
l2 = Label(window, text = "대출년수")
l2.grid(row = 2, column = 1)
l3 = Label(window, text = "대출금")
l3.grid(row = 3, column = 1)
l4 = Label(window, text = "월상환금")
l4.grid(row = 4, column = 1)
l5 = Label(window, text = "총상환금")
l5.grid(row = 5, column = 1)
l6 = Label(window, text = "")
l6.grid(row = 4, column = 2)
l7 = Label(window, text = "")
l7.grid(row = 5, column = 2)


e1 = Entry(window)
e1.grid(row = 1, column = 2)
e2 = Entry(window)
e2.grid(row = 2, column = 2)
e3 = Entry(window)
e3.grid(row = 3, column = 2)

def process():
    a = float(e3.get()) #a는 대출받은 원금
    b = (float(e1.get())*0.01)/12 #b는 대출에 대한 이자율
    n = float(e2.get())*12 #n은 대출상환개월수
    monthly_repayment = ((a*b*((1+b)**n))/(((1+b)**n)-1))
    total_repayment = monthly_repayment*n
    monthly_repayment = format(monthly_repayment, "10.2f")
    total_repayment = format(total_repayment, "10.2f")
    l6['text'] = str(monthly_repayment)
    l7['text'] = str(total_repayment)
    
b1 = Button(window, text="상환금계산하기", command=process)
b1.grid(row = 6, column = 2)


window.mainloop()
