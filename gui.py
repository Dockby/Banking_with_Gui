import tkinter as tk
from email.message import Message
from tkinter import PhotoImage
from tkinter import messagebox
from models import *
from PIL.ImageStat import Global
from click import option
import json
from models import Customer

def load_cust_data():
    with open("Customer_data.json","r") as file:
        data=json.load(file)
        return data
def run_app():
    window = tk.Tk()
    window.title("DockNow")
    window.geometry("800x700")
    window.config(bg="white")

    canva = tk.Canvas(window, height=200, width=900, bg="white", highlightthickness=0)
    img = PhotoImage(file="fin_logo-2.png")
    canva.create_image(400, 100, image=img)
    canva.grid(row=0, column=0)

    intro = tk.Label(text="Welcome to DockNow A Unique Place For all Your Finance And Funds related Queries",
                     font=("Ariel", 15), fg="white", bg="green")
    intro.grid(row=7, column=0, sticky="w", padx=80)

    subintro = tk.Label(text="What would you Like To Do Today?", font=("Ariel", 15), fg="green", bg="white")
    subintro.grid(row=8, column=0, sticky="w", padx=240)


    def acc_withdraw():



        mainwindow = tk.Toplevel()
        mainwindow.title("DockNow")
        mainwindow.geometry("800x700")
        mainwindow.config(bg="white")
        canva = tk.Canvas(mainwindow, height=200, width=900, bg="white", highlightthickness=0)
        img = PhotoImage(file="fin_logo-2.png")
        canva.create_image(400, 100, image=img)
        canva.grid(row=0, column=0)

        label1 = tk.Label(mainwindow, text=" Enter Account Number :", bg="green", fg="white", font=("Ariel", 18))
        label1.grid(row=2, column=0, sticky="w", padx=20)
        Acc_entry = tk.Entry(mainwindow, bg="lightgray", fg="darkblue", relief="sunken", font=("Ariel", 15))
        Acc_entry.grid(row=2, column=0, sticky="w", padx=230)

        label2 = tk.Label(mainwindow, text=" Enter Your Password    :", bg="green", fg="white", font=("Ariel", 18))
        label2.grid(row=3, column=0, sticky="w", padx=20, pady=50)
        pass_entry = tk.Entry(mainwindow, bg="lightgray", fg="darkblue", relief="sunken", font=("Ariel", 15))
        pass_entry.grid(row=3, column=0, sticky="w", padx=230)



        def valid_pass():
            account=Acc_entry.get()
            passwordy=pass_entry.get()
            if (len(account)==0 or len(int(passwordy)) == 0):
                messagebox.showerror(title="Error", message="Invalid Input ")
            customer_data=load_cust_data()
            if account in customer_data:
                if customer_data[account]["password"]==int(passwordy):
                    messagebox.showinfo(title="Login Status",message="Login SuccesFull")
                    mainwindow = tk.Toplevel()
                    mainwindow.title("DockNow")
                    mainwindow.geometry("800x700")
                    mainwindow.config(bg="white")
                    canva = tk.Canvas(mainwindow, height=200, width=900, bg="white", highlightthickness=0)
                    img = PhotoImage(file="fin_logo-2.png")
                    canva.create_image(400, 100, image=img)
                    canva.grid(row=0, column=0)
                    label2 = tk.Label(mainwindow, text=" Enter Amount In Numbers: ₹", bg="green", fg="white",
                                      font=("Ariel", 18))
                    label2.grid(row=3, column=0, sticky="w", padx=20, pady=50)
                    Amt_entry = tk.Entry(mainwindow, bg="lightgray", fg="darkblue", relief="sunken", font=("Ariel", 15))
                    Amt_entry.grid(row=3, column=0, sticky="w", padx=260)

                    def withdraw_success():
                        Amount=Amt_entry.get()

                        if int(Amount )> customer_data[account]["balance"]:
                            messagebox.showinfo(title="Transaction Declined",message="Your Balance is Insufficient")
                        else:
                            Customer1 = Customer(account, passwordy)
                            if Customer1.Money_withdraw(Amount):
                                messagebox.showinfo(title="Transaction Successful",message=f"Amount withdrawn ₹{Amount} Thank You")



                    btn_withdraw = tk.Button(mainwindow, text="Withdraw", font=("Ariel", 18), command=withdraw_success)
                    btn_withdraw.grid(row=5, column=0, sticky="w", padx=250)
                    mainwindow.mainloop()
                else:
                    messagebox.showinfo(title="Login Status",message="Password is incorrect")
            else:
                messagebox.showinfo(title="Login Status",message="Account does not Exist")
        btn = tk.Button(mainwindow, text="Submit", font=("Ariel", 18),command=valid_pass)
        btn.grid(row=4, column=0, sticky="w", padx=50)

        mainwindow.mainloop()

    def acc_status():
        mainwindow = tk.Toplevel()
        mainwindow.title("DockNow")
        mainwindow.geometry("800x700")
        mainwindow.config(bg="white")
        canva = tk.Canvas(mainwindow, height=200, width=900, bg="white", highlightthickness=0)
        img = PhotoImage(file="fin_logo-2.png")
        canva.create_image(400, 100, image=img)
        canva.grid(row=0, column=0)

        label1 = tk.Label(mainwindow, text=" Enter Account Number :", bg="green", fg="white", font=("Ariel", 18))
        label1.grid(row=2, column=0, sticky="w", padx=20)
        Acc_entry = tk.Entry(mainwindow, bg="lightgray", fg="darkblue", relief="sunken", font=("Ariel", 15))
        Acc_entry.grid(row=2, column=0, sticky="w", padx=230)

        label2 = tk.Label(mainwindow, text=" Enter Your Password    :", bg="green", fg="white", font=("Ariel", 18))
        label2.grid(row=3, column=0, sticky="w", padx=20, pady=50)
        pass_entry = tk.Entry(mainwindow, bg="lightgray", fg="darkblue", relief="sunken", font=("Ariel", 15))
        pass_entry.grid(row=3, column=0, sticky="w", padx=230)

        def Active_btn(Acc_entry, pass_entry):
            account = Acc_entry.get()
            passwordy = pass_entry.get()

            customer_data = load_cust_data()
            if account in customer_data:
                if customer_data[account]["password"] == int(passwordy):
                    mainwindow = tk.Toplevel()
                    mainwindow.title("DockNow")
                    mainwindow.geometry("800x700")
                    mainwindow.config(bg="white")
                    canva = tk.Canvas(mainwindow, height=200, width=900, bg="white", highlightthickness=0)
                    img = PhotoImage(file="fin_logo-2.png")
                    canva.create_image(400, 100, image=img)
                    canva.grid(row=0, column=0)

                    canva = tk.Canvas(mainwindow, height=200, width=900, bg="white", highlightthickness=0)
                    img = PhotoImage(file="fin_logo-2.png")
                    canva.create_image(400, 100, image=img)
                    canva.grid(row=0, column=0)
                    label1 = tk.Label(mainwindow, text=f" Your Account Status is :", bg="green", fg="white",
                                      font=("Ariel", 18))
                    label1.grid(row=2, column=0, sticky="w", padx=20)
                    Acc_entry = tk.Label(mainwindow, text=f"{customer_data[account]["status"]}", bg="lightgray",
                                         fg="darkblue", relief="sunken",
                                         font=("Ariel", 20))
                    Acc_entry.grid(row=2, column=0, sticky="w", padx=270)
                    btn_home = tk.Button(mainwindow, text="RETURN TO PREVIOUS PAGE", bg="yellow", fg="black",
                                         font=("Ariel", 22), command=acc_balance)
                    btn_home.grid(row=4, column=0, sticky="w", padx=280, pady=100, columnspan=8)
                    mainwindow.mainloop()
                else:
                    messagebox.showinfo(title="Instruction declined", message="Password Incorrect")
            else:
                messagebox.showinfo(title="Instruction declined", message="  Account Does Not Exist :( ")

        btn = tk.Button(mainwindow, text="Submit", font=("Ariel", 18),
                        command=lambda: Active_btn(Acc_entry, pass_entry))
        btn.grid(row=4, column=0, sticky="w", padx=50)
        mainwindow.mainloop()

    def success():
      messagebox.showinfo(title="Transaction Status",message="Amount Is Deposited. Thank You For Trusting In DockNow Pvt Ltd")
    def acc_deposit():
      mainwindow = tk.Toplevel()
      mainwindow.title("DockNow")
      mainwindow.geometry("800x700")
      mainwindow.config(bg="white")
      canva = tk.Canvas(mainwindow, height=200, width=900, bg="white", highlightthickness=0)
      img = PhotoImage(file="fin_logo-2.png")
      canva.create_image(400, 100, image=img)
      canva.grid(row=0, column=0)

      label1 = tk.Label(mainwindow, text=" Enter Account Number :", bg="green", fg="white", font=("Ariel", 18))
      label1.grid(row=2, column=0, sticky="w", padx=20)
      Acc_entry = tk.Entry(mainwindow, bg="lightgray", fg="darkblue", relief="sunken", font=("Ariel", 15))
      Acc_entry.grid(row=2, column=0, sticky="w", padx=230)
      label2 = tk.Label(mainwindow, text=" Enter Amount In Numbers: ₹", bg="green", fg="white", font=("Ariel", 18))
      label2.grid(row=3, column=0, sticky="w", padx=20, pady=50)
      Amt_entry = tk.Entry(mainwindow, bg="lightgray", fg="darkblue", relief="sunken", font=("Ariel", 15))
      Amt_entry.grid(row=3, column=0, sticky="w", padx=260)
      def submit_action():
        acc_no=Acc_entry.get()
        amt=Amt_entry.get()
        if (len(acc_no)==0 or len(int(amt)) == 0):
            messagebox.showerror(title="Error", message="Invalid Input ")
        Customer1 =Customer(acc_no,"dummypass")
        if Customer1.Money_deposit(amt):

          messagebox.showinfo("Deposit Success",message=f"Amount Credited: ₹{amt}")

      btn_add = tk.Button(mainwindow, text="Submit", font=("Ariel", 18),command=submit_action)
      btn_add.grid(row=4, column=0, sticky="w", padx=50)
      mainwindow.mainloop()
      return acc_deposit




    def acc_balance():

      mainwindow = tk.Toplevel()
      mainwindow.title("DockNow")
      mainwindow.geometry("800x700")
      mainwindow.config(bg="white")
      canva = tk.Canvas(mainwindow, height=200, width=900, bg="white", highlightthickness=0)
      img = PhotoImage(file="fin_logo-2.png")
      canva.create_image(400, 100, image=img)
      canva.grid(row=0, column=0)

      label1 = tk.Label(mainwindow, text=" Enter Account Number :", bg="green", fg="white", font=("Ariel", 18))
      label1.grid(row=2, column=0, sticky="w", padx=20)
      Acc_entry = tk.Entry(mainwindow, bg="lightgray", fg="darkblue", relief="sunken", font=("Ariel", 15))
      Acc_entry.grid(row=2, column=0, sticky="w", padx=230)

      label2 = tk.Label(mainwindow, text=" Enter Your Password    :", bg="green", fg="white", font=("Ariel", 18))
      label2.grid(row=3, column=0, sticky="w", padx=20, pady=50)
      pass_entry = tk.Entry(mainwindow, bg="lightgray", fg="darkblue", relief="sunken", font=("Ariel", 15))
      pass_entry.grid(row=3, column=0, sticky="w", padx=230)
      def Balance_btn(Acc_entry,pass_entry):
          account =Acc_entry.get()
          passwordy = pass_entry.get()
          if(len(account)==0 or len (int(passwordy))== 0):
              messagebox.showerror(title="Error",message="Invalid Input ")

          customer_data = load_cust_data()
          if account in customer_data:
              if customer_data[account]["password"] == int(passwordy):
               mainwindow = tk.Toplevel()
               mainwindow.title("DockNow")
               mainwindow.geometry("800x700")
               mainwindow.config(bg="white")
               canva = tk.Canvas(mainwindow, height=200, width=900, bg="white", highlightthickness=0)
               img = PhotoImage(file="fin_logo-2.png")
               canva.create_image(400, 100, image=img)
               canva.grid(row=0, column=0)

               canva = tk.Canvas(mainwindow, height=200, width=900, bg="white", highlightthickness=0)
               img = PhotoImage(file="fin_logo-2.png")
               canva.create_image(400, 100, image=img)
               canva.grid(row=0, column=0)
               label1 = tk.Label(mainwindow, text=f" Your Account Balance is ₹:", bg="green", fg="white",
                                font=("Ariel", 18))
               label1.grid(row=2, column=0, sticky="w", padx=20)
               Acc_entry = tk.Label(mainwindow, text=f"{customer_data[account]["balance"]}", bg="lightgray", fg="darkblue", relief="sunken",
                                   font=("Ariel", 20))
               Acc_entry.grid(row=2, column=0, sticky="w", padx=270)
               btn_home = tk.Button(mainwindow, text="RETURN TO PREVIOUS PAGE", bg="yellow", fg="black",
                                   font=("Ariel", 22), command=acc_balance)
               btn_home.grid(row=4, column=0, sticky="w", padx=280, pady=100, columnspan=8)
               mainwindow.mainloop()
              else:
               messagebox.showinfo(title="Instruction declined",message="Password Incorrect")
          else:
              messagebox.showinfo(title="Instruction declined",message="  Account Does Not Exist :( ")





      btn = tk.Button(mainwindow, text="Submit", font=("Ariel", 18), command=lambda:Balance_btn(Acc_entry,pass_entry))
      btn.grid(row=4, column=0, sticky="w", padx=50)
      mainwindow.mainloop()
     def register():
        mainwindow = tk.Toplevel()
        mainwindow.title("DockNow")
        mainwindow.geometry("800x700")
        mainwindow.config(bg="white")
        canva = tk.Canvas(mainwindow, height=200, width=900, bg="white", highlightthickness=0)
        img = PhotoImage(file="fin_logo-2.png")
        canva.create_image(400, 100, image=img)
        canva.grid(row=0, column=0)

        label1 = tk.Label(mainwindow, text=" Enter Account Number :", bg="green", fg="white", font=("Ariel", 18))
        label1.grid(row=2, column=0, sticky="w", padx=20)
        Acc_entry = tk.Entry(mainwindow, bg="lightgray", fg="darkblue", relief="sunken", font=("Ariel", 15))
        Acc_entry.grid(row=2, column=0, sticky="w", padx=230)

        label2 = tk.Label(mainwindow, text=" Enter Your Password    :", bg="green", fg="white", font=("Ariel", 18))
        label2.grid(row=3, column=0, sticky="w", padx=20, pady=50)
        pass_entry = tk.Entry(mainwindow, bg="lightgray", fg="darkblue", relief="sunken", font=("Ariel", 15))
        pass_entry.grid(row=3, column=0, sticky="w", padx=230)
        label3 = tk.Label(mainwindow, text=" Enter Your Account Status(type Valid) :", bg="green", fg="white", font=("Ariel", 18))
        label3.grid(row=4, column=0, sticky="w", padx=20)
        Acc_status = tk.Entry(mainwindow, bg="lightgray", fg="darkblue", relief="sunken", font=("Ariel", 15))
        Acc_status.grid(row=4, column=0, sticky="w", padx=350)

        deposit = tk.Label(mainwindow, text=" Enter Initial Amount :", bg="green", fg="white", font=("Ariel", 18))
        deposit.grid(row=5, column=0, sticky="w", padx=20, pady=50)
        deposit_entry = tk.Entry(mainwindow, bg="lightgray", fg="darkblue", relief="sunken", font=("Ariel", 15))
        deposit_entry.grid(row=5, column=0, sticky="w", padx=210)

        def submit():
            account_info=Acc_entry.get()
            pass_info=pass_entry.get()
            acc_stat=Acc_status.get()
            deposit_info=deposit_entry.get()


            if(len(account_info)==0 or len(pass_info)==0 or len(acc_stat)==0 or len(deposit_info)==0):
                    messagebox.showerror(title="Error", message="Please Enter the Value Correctly in the Fields")
            else:

                    data_2_add={
                            "password":pass_info,
                            "balance":deposit_info,
                            "status":acc_stat
                    }

                    with open("Customer_data.json","r") as data_file:
                        data_2=json.load(data_file)
                        data_2[account_info]=data_2_add
                    with open("Customer_data.json","w") as data_file:
                        json.dump(data_2,data_file,indent=4)
                    messagebox.showinfo(title="Congratulations",message="Account is successfully created ")
                    Acc_entry.delete(0,len(account_info))
                    pass_entry.delete(0,len(pass_info))
                    Acc_status.delete(0,len(acc_stat))
                    deposit_entry.delete(0,len(deposit_info))




        submit_reg=tk.Button(mainwindow,text="Submit",font=("Ariel", 20),command=submit)
        submit_reg.grid(row=6,column=0,sticky="w",padx=50)

        mainwindow.mainloop()









    btn1 = tk.Button(text="Money Deposit", font=("Ariel", 20), command=acc_deposit)
    btn1.grid(row=12, column=0, sticky="w", padx=150, pady=50, )
    btn2 = tk.Button(text="Money Withdraw", font=("Ariel", 20),command=acc_withdraw)
    btn2.grid(row=12, column=0, sticky="w", padx=350)
    btn3 = tk.Button(text="Account Status", font=("Ariel", 20), command=acc_status)
    btn3.grid(row=14, column=0, sticky="w", padx=150)
    btn4 = tk.Button(text="Account Balance", font=("Ariel", 20), command=acc_balance)
    btn4.grid(row=14, column=0, sticky="w", padx=350)
    btn5=tk.Button(text="Register For New Account",bg="green",fg="black",font=("Ariel", 20),command=register)
    btn5.grid(row=18,column=0,sticky="w",pady=50,padx="200")
    window.mainloop()
    window.mainloop()

if __name__ == "__main__":
    run_app()
