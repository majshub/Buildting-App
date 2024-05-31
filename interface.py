import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title('Building App')

def openExpenses():
    top = tk.Toplevel()
    top.title('Expenses Page')

    # Creating expenses dropdown list
    expenseLabel = tk.Label(top, text='Expense Type')
    expenseLabel.grid(row=0, column=0, padx=10, pady=10)

    ExpenseTypes = ['Utility', 'Salary', 'Maintenance']
    selectedExpenseType = tk.StringVar()
    selectedExpenseType.set(ExpenseTypes[0])
    expenseTypeList = tk.OptionMenu(top, selectedExpenseType, *ExpenseTypes)
    expenseTypeList.grid(row=0, column=1, padx=10, pady=10)

    # Creating expense entry
    cost_label = tk.Label(top, text='Cost')
    cost_label.grid(row=0, column=2, padx=10, pady=10)

    cost = tk.Entry(top, width=35, borderwidth=3)
    cost.grid(row=0, column=3, columnspan=3, padx=10, pady=10)

    # Creating date frame
    dateFrame = tk.LabelFrame(top, text='Date', padx=10, pady=10)
    dateFrame.grid(row=1, column=0, padx=10, pady=10)

    dayLabel = tk.Label(dateFrame, text='Day')
    dayLabel.grid(row=0, column=0)
    days = [str(d) for d in range(1, 32)]
    day = tk.StringVar()
    dayDropList = tk.OptionMenu(dateFrame, day, *days)
    dayDropList.grid(row=0, column=1, padx=10, pady=10)

    monthLabel = tk.Label(dateFrame, text='Month')
    monthLabel.grid(row=0, column=2)
    months = [str(m) for m in range(1, 13)]
    month = tk.StringVar()
    monthDropList = tk.OptionMenu(dateFrame, month, *months)
    monthDropList.grid(row=0, column=3, padx=10, pady=10)

    yearLabel = tk.Label(dateFrame, text='Year')
    yearLabel.grid(row=0, column=4)
    years = [str(y) for y in range(2010, 2025)]
    year = tk.StringVar()
    yearDropList = tk.OptionMenu(dateFrame, year, *years)
    yearDropList.grid(row=0, column=5, padx=10, pady=10)

    # Creating payment method frame
    payMethodFrame = tk.LabelFrame(top, text='Payment Method', padx=10, pady=10)
    payMethodFrame.grid(row=1, column=1, padx=10, pady=10)

    selectedPayMethod = tk.StringVar()
    bankButton = tk.Radiobutton(payMethodFrame, text='Bank', variable=selectedPayMethod, value='Bank')
    bankButton.grid(row=0, column=0, padx=10, pady=10)
    cashBoxButton = tk.Radiobutton(payMethodFrame, text='Cash Box', variable=selectedPayMethod, value='Cash Box')
    cashBoxButton.grid(row=0, column=1, padx=10, pady=10)

    def getValues():
        global expense_type, amount, date_paid, payment_method
        expense_type = selectedExpenseType.get()
        amount = cost.get()
        date_paid = f"{year.get()}-{month.get()}-{day.get()}"
        payment_method = selectedPayMethod.get()
        messagebox.showinfo("Info", f"Expense Type: {expense_type}\nCost: {amount}\nDate Paid: {date_paid}\nPayment Method: {payment_method}")

    submitButton = tk.Button(top, text="Submit", command=getValues)
    submitButton.grid(row=3, column=0, columnspan=4, pady=10)

expensesButton = tk.Button(root, text='Expenses', command=openExpenses)
expensesButton.pack(padx=10, pady=10)

tk.mainloop()
