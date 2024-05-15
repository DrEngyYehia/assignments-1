
import tkinter as tk
from tkinter import messagebox

loan_type = ""
loan_program = ""

root = tk.Tk()
root.title("Banque Misr  |  Plan Your Loan ")
root.geometry("1200x500")
root.resizable(False, False)
# root.minsize(width=1200, height=500)

root_frame = tk.Frame(root)
root_frame.config(background="#ffffff", width=1200, height=500)
root_frame.pack()


# # creating main frames
frame_1 = tk.Frame(root_frame)
frame_1.config(background="#871e35", width=400, height=500)
frame_1.grid(column=0,row=0,columnspan=1, sticky="nsew")

frame_2 = tk.Frame(root_frame)
frame_2.config(background="#f8f9fa", width=400, height=500)
frame_2.grid(column=1,row=0,columnspan=1, sticky="nsew")

frame_3 = tk.Frame(root_frame)
frame_3.config(background="#343a40", width=400, height=500)
frame_3.grid(column=2,row=0,columnspan=2, sticky="nsew")

# frame 1 contents
img = tk.PhotoImage(file="logo.png")
logo_image = tk.Label(frame_1, image=img)
logo_image.config(width=400)
logo_image.pack()

f1_label1 = tk.Label(frame_1,text="Plan Your Loan")
f1_label1.config(background="#871e35", foreground="#ffffff", font=("Arial", 30, "bold"))
f1_label1.pack(pady=50, ipadx=30)

f1_label2 = tk.Label(frame_1,text="Manage your money with us")
f1_label2.config(background="#871e35", foreground="#ffffff", font=("Arial", 15, "bold"))
f1_label2.pack(pady=0, ipadx=30)

# frame 3 contents
f3_total_loan_label = tk.Label(frame_3, text="Total Loan")
f3_total_loan_label.config(background="#343a40", foreground="white", font=("arial", 15, "bold"))
f3_total_loan_label.pack(pady=20)

f3_total_loan = tk.Label(frame_3, text="0 EGP")
f3_total_loan.config(background="#343a40", foreground="white", font=("arial", 30, "bold"), width=12)
f3_total_loan.pack(pady=5)

# f3_decreasing_interest_rate_label = tk.Label(frame_3, text="Decreasing Interest Rate")
# f3_decreasing_interest_rate_label.config(background="#343a40", foreground="white", font=("arial", 12, "bold"))
# f3_decreasing_interest_rate_label.pack(pady=5)

# f3_decreasing_interest_rate = tk.Label(frame_3, text="0.00%")
# f3_decreasing_interest_rate.config(background="#343a40", foreground="white", font=("arial", 15, "bold"))
# f3_decreasing_interest_rate.pack(pady=5)

f3_fixed_interest_rate_label = tk.Label(frame_3, text="Fixed Interest Rate")
f3_fixed_interest_rate_label.config(background="#343a40", foreground="white", font=("arial", 12, "bold"))
f3_fixed_interest_rate_label.pack(pady=5)

f3_fixed_interest_rate = tk.Label(frame_3, text="0.00%")
f3_fixed_interest_rate.config(background="#343a40", foreground="white", font=("arial", 15, "bold"))
f3_fixed_interest_rate.pack(pady=5)

f3_pay_per_month_label = tk.Label(frame_3, text="Pay/Month")
f3_pay_per_month_label.config(background="#343a40", foreground="white", font=("arial", 12, "bold"))
f3_pay_per_month_label.pack(pady=5)

f3_pay_per_month = tk.Label(frame_3, text="0 EGP")
f3_pay_per_month.config(background="#343a40", foreground="white", font=("arial", 15, "bold"))
f3_pay_per_month.pack(pady=5)

f3_total_interests_label = tk.Label(frame_3, text="Total Interests")
f3_total_interests_label.config(background="#343a40", foreground="white", font=("arial", 12, "bold"))
f3_total_interests_label.pack(pady=5)

f3_total_interests = tk.Label(frame_3, text="0 EGP")
f3_total_interests.config(background="#343a40", foreground="white", font=("arial", 15, "bold"))
f3_total_interests.pack(pady=5)


# frame 2 contents
loan_programs = {
"Auto Loan": ["40% surrogate income", "50% surrogate income", "50% surrogate income(used)", "60% surrogate income","60% surrogate income(used)"],
"Durable Loans": ["employed-salary certificate", "pension retired without undertaking durables", "income proof durable contract salary transfer public", "payroll durable private sector", "payroll durable ppublic"],
"Commercial Loans": ["commercial loans for government employee with a pledge", "commercial loans for pension beneficairies with a pledge", "commercial loans for pension beneficairies without a pledge", "commercial loans with proof of income for government sector", "commercial loans with salary/installment transfer(privet sector employee)" ],
"Mortgage Loans": ["CBE initiative for mortgage of middle income 3%", "CBE initiative for mortgeg of middle income 8%", "Egyptians Abroad Individual Mortgage-up to 5", "Egyptians Abroad Individual Mortgage-up to 15" ],
"Murabaha By Wakulla": ["Business Owner income proof" ,"Employee of banks and telecom companies", "Freelancer activities income proof", "Income proof (Private sector) - Non-Contracted companies", "Income proof (Governmental and public sector) Non-Contracted companies"],
"Personal Loans": ["income proof professionals /doctors", "Employee of banks and telecommunications companies", "Freelancer activities income proof", "Governmental and public companies Income proof", "Business owner Income proof"],
"Real Estate Lease Ending With Ownership": ["UNSECURED EJARAH- Registered units", "UNSECURED EJARAH- Unregistered units"],
"scooter Loans": ["Employed - Salary/Installment Transfer", "Income Proof Scooter", "Professional Scooter"]
}
loan_programs_var = tk.StringVar(frame_2)
loan_programs_var.set("Select your loan program")
# loan_programs_var.trace_add('write', lambda *args: loan_program = loan_programs_var)
loan_programs_menu = tk.OptionMenu(frame_2, loan_programs_var, "")
loan_programs_menu.config(width=70)

def change_loan_program(choice):
    global loan_programs_menu
    # loan_programs_menu.set("")
    loan_programs_menu["menu"].delete(0, "end")
    for opt in loan_programs[choice]: 
        loan_programs_menu['menu'].add_command(label=opt, command=tk._setit(loan_programs_var, opt))
    loan_programs_var.set("Select your loan program")

loan_types=[ "Auto Loan", "Durable Loans", "Commercial Loans", "Mortgage Loans", "Murabaha By Wakulla", "Personal Loans", "Real Estate Lease Ending With Ownership", "scooter Loans"]
loan_types_var = tk.StringVar(frame_2)
loan_types_var.set("Select your loan type")
loan_types_menu = tk.OptionMenu(frame_2, loan_types_var, *loan_types, command=change_loan_program)
loan_types_menu.config(width=70)
loan_types_menu.pack()

loan_programs_menu.pack()

loan_value_label = tk.Label(frame_2, text="Loan Value (min 2,500 EGP, max 3,000,000 EGP):")
loan_value_label.config(background="#f8f9fa")
loan_value_label.pack(pady=10)

loan_value_input = tk.Text(frame_2, width=50, height=2)
loan_value_input.config(background="#999999")
loan_value_input.pack(pady=5)

loan_period_label = tk.Label(frame_2, text="Loan Period (min 6 months, max 60 months):")
loan_period_label.config(background="#f8f9fa")
loan_period_label.pack(pady=10)

loan_period_input = tk.Text(frame_2, width=50, height=2)
loan_period_input.config(background="#999999")
loan_period_input.pack(pady=5)

def calculate():
    # loan_value_input
    # loan_period_input
    loan_value = 0
    loan_period = 0
    try:
        loan_value = int(loan_value_input.get("1.0",tk.END))
        loan_period = int(loan_period_input.get("1.0",tk.END))

        if loan_types_var.get() == "Select your loan type":
            messagebox.showerror("Error", "A loan Type must be chosen")
        elif loan_programs_var.get() == "Select your loan program":
            messagebox.showerror("Error", "A loan program must be chosen")
        else:
            if loan_value < 2500 or loan_value > 3000000:
                messagebox.showerror("Error", "Loan Value must be between 2,500 EGP and 3,000,000 EGP")

            if loan_period < 6 or loan_period > 60:
                messagebox.showerror("Error", "Loan period must be between 6 months and 60 months")

            interest = 0
            loan_years = int(loan_period / 12)
            if loan_years == 0:
                loan_years += 1

            if loan_years == 1:
                interest = 0.1376
            elif loan_years == 2 or loan_years == 3:
                interest = 0.1406
            elif loan_years == 4 or loan_years == 5:
                interest = 0.1487
            else:
                interest = 0.1571

            interest_in_one_year = interest * loan_value
            total_interest = loan_years * interest_in_one_year
            total_loan = loan_value + total_interest
            pay_per_month = total_loan / loan_period

            f3_total_loan.config(text=f"{total_loan:.02f} EGP")
            f3_fixed_interest_rate.config(text=f"{interest*100:.02f}%")
            f3_pay_per_month.config(text=f"{pay_per_month:.02f} EGP")
            f3_total_interests.config(text=f"{total_interest:.02f} EGP")


    except ValueError:
        messagebox.showerror("Errot", "Loan Value and Loan Period must be integers")



def clear():
    loan_value_input.delete('1.0', tk.END)
    loan_period_input.delete('1.0', tk.END)
    loan_types_var.set("Select your loan type")
    loan_programs_var.set("Select your loan program")

btn = tk.Button(frame_2, text="Calculate", command=calculate)
btn.pack(pady=10)

btn = tk.Button(frame_2, text="Clear", command=clear)
btn.pack(pady=10)

root.mainloop()