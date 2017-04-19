import tkinter
from tkinter import*
from tkinter import Tk,StringVar,ttk
import random
import datetime
import time






root = Tk()
root.geometry ("1200x750+0+0")
root.title ('stock Control System')

TopFrame = Frame(root, width=950, height=100, bd =10, relief ='raise')
TopFrame.pack(side=TOP)

BottomFrame = Frame(root, width =950, height =200, bd =10, relief ='raise')
BottomFrame.pack(side=BOTTOM)

LeftMidFrame = Frame(BottomFrame, width =600, height =1500, bd =8, relief ='raise')
LeftMidFrame.pack(side=LEFT)

RightMidFrame = Frame(BottomFrame, width =750, height =1500, bd =8, relief ='raise')
RightMidFrame.pack(side=RIGHT)


lblTitle = Label(TopFrame, font =('arial',40, 'bold'), text="Stock Control System",bd=10, width= 41, justify='center')
lblTitle.grid(row=0,column=0)

#============================Variables =====================================

var1 = StringVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
VAT = StringVar()
Tax = StringVar()
Date1 = StringVar()
Discount=IntVar()
CostperUnit = IntVar()
OutofStock = IntVar()
Remainder = IntVar()
SubTotal= IntVar()
Total= IntVar()

var1.set("")
var2.set("")
var3.set("")
var4.set("")
var5.set("")
var6.set("")
var7.set("")
var8.set("")
var9.set("")
var10.set("")
VAT.set("")
Tax.set("0")
Discount.set("0")
CostperUnit.set("0")
OutofStock.set("")
Remainder.set ("0")
SubTotal.set("0")
Total.set("0")

Date1.set(time.strftime("%d/%m/%y"))

def Product():
    if (var1.get()=="PID001"):
        var2.set("Rice")
        var3.set("White Seed")
        var4.set(200)
        value1 =(var5.get())
        var5.set(value1)
        var6.set(2)
        var7.set(value1)
        var8.set(50)
        CostperUnit.set(20)
        Discount1 =float(Discount.get())
        R = float((var4.get()) - (var5.get()))
        SubTotal1 = ((value1 * 20)- Discount1)
        SubTotal.set(SubTotal1)
        Tax1 = (SubTotal1 * 5)/100
        Tax.set(Tax1)
        #Total1 = (Tax1 + SubTotal1)
        #Total.set= (Total1)
        Remainder.set(R)
        SubTotal2 =("$", str(SubTotal1))
        Tax2 = ("$",str((SubTotal1 * 5)/100))
        Total2 = ("$", str(Tax1 + SubTotal1))

        SubTotal.set(SubTotal2)
        Tax.set(Tax2)
        Total.get(Total2)
        if (R <=30):
            var9.set ("Re-Order Product")
            OutofStock.set ("Low Stock")
        elif (R>= 31):
            var9.set("No Order Requested")
            OutofStoc.set("High Stock")
        
      

    elif (var1.get() == "PID002"):
        var2.set("Beans")
        var3.set("White Seed")
        var4.set(120)
        value1 =float(var5.get())
        var5.set(value1)
        var6.set(2)
        var7.set(value1)
        var8.set(50)
        CostperUnit.set(17)
        Discount1 =float(Discount.get())
        R = float((var4.get()) - (var5.get()))
        SubTotal1 = ((value1 * 17)- Discount1)
        SubTotal.set(SubTotal1)
        Tax1 = (SubTotal * 4.5)/100
        Tax.set(Tax1)
        Total1 = (Tax1 + SubTotal1)
        Total.set= (Total1)
        Remainder.set(R)
        SubTotal2 =("$", str(SubTotal1))
        Tax2 = ("$",str((SubTotal1 * 4.5)/100))
        Total2 = ("$", str(Tax1 + SubTotal1))

        SubTotal.set(SubTotal2)
        Tax.set(Tax2)
        Total.get(Total2)
        if (R <=30):
            var9.set ("Re-Order Product")
            OutofStock.set ("Low Stock")
        elif (R>= 31):
            var9.set("No Order Requested")
            OutofStoc.set("High Stock")

            
    elif (var1.get() == "PID003"):
        var2.set("Carrot")
        var3.set("Vegetable")
        var4.set(150)
        value1 =float(var5.get())
        var5.set(value1)
        var6.set(2)
        var7.set(value1)
        var8.set(50)
        CostperUnit.set(15)
        Discount1 =float(Discount.get())
        R = float((var4.get()) - (var5.get()))
        SubTotal1 = ((value1 * 15)- Discount1)
        SubTotal.set(Subtotal1)
        Tax1 = (SubTotal * 4.5)/100
        Tax.set(Tax1)
        Total1 = (Tax1 + SubTotal1)
        Total.set= (Total1)
        Remainder.set(R)
        SubTotal2 =("$", str(SubTotal1))
        Tax2 = ("$",str((SubTotal1 * 4.5)/100))
        Total2 = ("$", str(Tax1 + SubTotal1))

        SubTotal.set(SubTotal2)
        Tax.set(Tax2)
        Total.get(Total2)
        if (R <=30):
            var9.set ("Re-Order Product")
            OutofStock.set ("Low Stock")
        elif (R>= 31):
            var9.set("No Order Requested")
            OutofStoc.set("High Stock")

            
    elif (var1.get() == "PID002"):
        var2.set("Bread")
        var3.set("Flour/Grain")
        var4.set(400)
        value1 =float(var5.get())
        var5.set(value1)
        var6.set(2)
        var7.set(value1)
        var8.set(50)
        CostperUnit.set(250)
        Discount1 =float(Discount.get())
        R = float((var4.get()) - (var5.get()))
        SubTotal1 = ((value1 * 300)- Discount1)
        SubTotal.set(SubTotal1)
        Tax1 = (SubTotal * 4.5)/100
        Tax.set(Tax1)
        Total1 = (Tax1 + SubTotal1)
        Total.set= (Total1)
        Remainder.set(R)
        SubTotal2 =("$", str(SubTotal1))
        Tax2 = ("$",str((SubTotal1 * 4.5)/100))
        Total2 = ("$", str(Tax1 + SubTotal1))

        SubTotal.set(SubTotal2)
        Tax.set(Tax2)
        Total.get(Total2)
        if (R <=30):
            var9.set ("Re-Order Product")
            OutofStock.set ("Low Stock")
        elif (R>= 31):
            var9.set("No Order Requested")
            OutofStoc.set("High Stock")
    elif (var1.get() == "PID005"):
        var2.set("Eggs")
        var3.set("Poultry")
        var4.set(500)
        value1 =float(var5.get())
        var5.set(value1)
        var6.set(2)
        var7.set(value1)
        var8.set(50)
        CostperUnit.set(50)
        Discount1 =float(Discount.get())
        R = float((var4.get()) - (var5.get()))
        SubTotal1 = ((value1 * 50)- Discount1)
        SubTotal.set(SubtoTal1)
        Tax1 = (SubTotal * 5)/100
        Tax.set(Tax1)
        Total1 = (Tax1 + SubTotal1)
        Total.set= (Total1)
        Remainder.set(R)
        SubTotal2 =("$", str(SubTotal1))
        Tax2 = ("$",str((SubTotal1 * 5)/100))
        Total2 = ("$", str(Tax1 + SubTotal1))

        SubTotal.set(SubTotal2)
        Tax.set(Tax2)
        Total.get(Total2)
        if (R <=30):
            var9.set ("Re-Order Product")
            OutofStock.set ("Low Stock")
        elif (R>= 31):
            var9.set("No Order Requested")
            OutofStoc.set("High Stock")





def iExit():
    qExit= messagebox.askyesno("Quit System","Do you want to quit")
    if qExit > 0:
        root.destroy()
        return


def Reset():
    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")
    var5.set("")
    var6.set("")
    var7.set("")
    var8.set("")
    var9.set("")
    Remainder.set("0")
    Discount.set("0")
    VAT.set("")
    Tax.set("0")
    OutofStock.set("")
    CostperUnit.set("0")
    SubTotal.set("0")
    Total.set("0")






#============================Product Details ===============================Left frame====



lblProductID1= Label(LeftMidFrame, font =('arial',14, 'bold'), text="Product ID",bd=10, width= 20, anchor='w')
lblProductID1.grid(row=0,column=0)

cmbProductID = ttk.Combobox(LeftMidFrame, textvariable = var1 , state='readonly', font =('arial',14, 'bold'), width= 20)
cmbProductID['value']=('','PID001','PID002','PID003','PID004','PID005')
cmbProductID.current (0)
cmbProductID.grid(row=0,column=1)

lblProductName1 = Label(LeftMidFrame, font =('arial',14, 'bold'), text="Product Name",bd=10, width= 20 ,anchor='w')
lblProductName1.grid(row=1,column=0)
lblProductName2 = Label(LeftMidFrame, font =('arial',14, 'bold'), textvariable=var2,bd=10, width= 18,relief ='sunken' )
lblProductName2.grid(row=1,column=1)

lblDescription1 = Label(LeftMidFrame, font =('arial',14, 'bold'), text="Description",bd=10, width= 20 ,anchor='w')
lblDescription1.grid(row=2,column=0)
lblDescription2 = Label(LeftMidFrame, font =('arial',14, 'bold'), textvariable=var3,bd=10, width= 18, relief ='sunken' )
lblDescription2.grid(row=2,column=1)

lblStockLevel1 = Label(LeftMidFrame, font =('arial',14, 'bold'), text="Stock Level",bd=10, width= 20 ,anchor='w')
lblStockLevel1.grid(row=3,column=0)
lblStockLevel2 = Label(LeftMidFrame, font =('arial',14, 'bold'), textvariable=var4,bd=10, width= 18,relief ='sunken' )
lblStockLevel2.grid(row=3,column=1)

lblReorderLevel1 = Label(LeftMidFrame, font =('arial',14, 'bold'), text="Reorder Level",bd=10, width= 20 ,anchor='w')
lblReorderLevel1.grid(row=4,column=0)
lblReorderLevel2 = Label(LeftMidFrame, font =('arial',14, 'bold'), textvariable=var8,bd=10, width= 18,relief ='sunken' )
lblReorderLevel2.grid(row=4,column=1)

lblOutofStock1 = Label(LeftMidFrame, font =('arial',14, 'bold'), text="Out of Stock",bd=10, width= 20 ,anchor='w')
lblOutofStock1.grid(row=5,column=0)
lblOutofStock2 = Label(LeftMidFrame, font =('arial',14, 'bold'), textvariable=OutofStock,bd=10, width= 18, relief ='sunken' )
lblOutofStock2.grid(row=5,column=1)

lblNoofOrder1 = Label(LeftMidFrame, font =('arial',14, 'bold'), text="No. of Order",bd=10, width= 20 ,anchor='w')
lblNoofOrder1.grid(row=6,column=0)

txtNoofOrder = Entry(LeftMidFrame,textvariable=var5 ,font =('arial',14, 'bold'), bd=10, width= 18 )
txtNoofOrder.grid(row=6,column=1)



lblAction1 = Label(LeftMidFrame, font =('arial',14, 'bold'), text="Action",bd=10, width= 20 ,anchor='w')
lblAction1.grid(row=7,column=0)
lblAction2 = Label(LeftMidFrame, font =('arial',14, 'bold'), textvariable=var9,bd=10, width= 18,relief ='sunken' )
lblAction2.grid(row=7,column=1)

lblReorderDate1 = Label(LeftMidFrame, font =('arial',14, 'bold'), text="Reorder Date",bd=10, width= 20 ,anchor='w')
lblReorderDate1.grid(row=8,column=0)
lblReorderDate2 = Label(LeftMidFrame, font =('arial',14, 'bold'), textvariable=Date1,bd=10, width= 18,relief ='sunken' )
lblReorderDate2.grid(row=8,column=1)

lblDiscount1 = Label(LeftMidFrame, font =('arial',14, 'bold'), text="Discount",bd=10, width= 20 ,anchor='w')
lblDiscount1.grid(row=9,column=0)

cmbDiscount = ttk.Combobox(LeftMidFrame, textvariable = Discount , state='readonly', font =('arial',14, 'bold'), width= 20)
cmbDiscount['value']=(0,5,10,15,20,25)
cmbDiscount.current (0)
cmbDiscount.grid(row=9,column=1)

lblCostperUnit1 = Label(LeftMidFrame, font =('arial',14, 'bold'), text="Cost per Unit",bd=10, width= 20 ,anchor='w')
lblCostperUnit1.grid(row=10,column=0)
lblCostperUnit2 = Label(LeftMidFrame, font =('arial',14, 'bold'), textvariable=CostperUnit,bd=10, width= 18,relief ='sunken' )
lblCostperUnit2.grid(row=10,column=1)


#========================Right Middle Frame==================



lblValidFrom1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="Valid From",bd=10, width= 15 ,anchor='w')
lblValidFrom1.grid(row=0,column=0)
lblValidFrom2 = Label(RightMidFrame, font =('arial',14, 'bold'), textvariable=Date1,bd=10, width= 14, relief ='sunken' )
lblValidFrom2.grid(row=0,column=1)

lblDateExpires1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="Date Expires",bd=10, width= 15 ,anchor='w')
lblDateExpires1.grid(row=0,column=2)
lblDateExpires2 = Label(RightMidFrame, font =('arial',14, 'bold'), textvariable=Date1,bd=10, width= 14, relief ='sunken' )
lblDateExpires2.grid(row=0,column=3)

lblRemainder1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="Remainder",bd=10, width= 15 ,anchor='w')
lblRemainder1.grid(row=1,column=0)
lblRemainder2 = Label(RightMidFrame, font =('arial',14, 'bold'), textvariable=Remainder,bd=10, width= 14, relief ='sunken' )
lblRemainder2.grid(row=1,column=1)

lblOnSales1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="On Sale",bd=10, width= 15 ,anchor='w')
lblOnSales1.grid(row=1,column=2)

cmbOnSale = ttk.Combobox(RightMidFrame , state='readonly', font =('arial',14, 'bold'), width= 15)
cmbOnSale['value']=('','Yes','No')
cmbOnSale.current (0)
cmbOnSale.grid(row=1,column=3)

lblOrderID1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="Order ID",bd=10, width= 15 ,anchor='w')
lblOrderID1.grid(row=2,column=0)

cmbOrderID = ttk.Combobox(RightMidFrame, state='readonly', font =('arial',14, 'bold'), width= 15)
cmbOrderID['value']=('','OID0091','OID0092','OID0093','OID0094','OID0095')
cmbOrderID.current (0)
cmbOrderID.grid(row=2,column=1)




lblDateOrdered1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="Date Ordered",bd=10, width= 15 ,anchor='w')
lblDateOrdered1.grid(row=2,column=2)
lblDateOrdered2 = Label(RightMidFrame, font =('arial',14, 'bold'), textvariable=Date1,bd=10, width= 14, relief ='sunken' )
lblDateOrdered2.grid(row=2,column=3)

lblCustomerID1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="Customer ID",bd=10, width= 15 ,anchor='w')
lblCustomerID1.grid(row=3,column=0)
cmbCustomerID = ttk.Combobox(RightMidFrame , state='readonly', font =('arial',14, 'bold'), width= 15)
cmbCustomerID['value']=('','CID0091','CID0092','CID0093','CID0094','CID0095')
cmbCustomerID.current (0)
cmbCustomerID.grid(row=3,column=1)


lblNoofItemOrd1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="No. of Item Ord",bd=10, width= 15 ,anchor='w')
lblNoofItemOrd1.grid(row=3,column=2)
lblNoofItemOrd2 = Label(RightMidFrame, font =('arial',14, 'bold'), textvariable=var7, bd=10, width= 14, relief ='sunken' )
lblNoofItemOrd2.grid(row=3,column=3)

lblFirstName1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="First Name",bd=2, width= 15 ,anchor='w')
lblFirstName1.grid(row=4,column=0)
txtFirstName2 = Entry(RightMidFrame, font =('arial',14, 'bold'),bd=10, width= 14 )
txtFirstName2.grid(row=4,column=1)

lblItemOdered1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="Item Odered",bd=10, width= 15 ,anchor='w')
lblItemOdered1.grid(row=4,column=2)
lblItemOdered2 = Label(RightMidFrame, font =('arial',14, 'bold'), textvariable=var2, bd=10, width= 14, relief ='sunken' )
lblItemOdered2.grid(row=4,column=3)

lblSurname1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="Surname",bd=10, width= 15 ,anchor='w')
lblSurname1.grid(row=5,column=0)
txtSurname2 = Entry(RightMidFrame, font =('arial',14, 'bold'), bd=10, width= 14 )
txtSurname2.grid(row=5,column=1)

lblPaymentMethod1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="Payment Method",bd=10, width= 15 ,anchor='w')
lblPaymentMethod1.grid(row=5,column=2)
cmbPaymentMethod = ttk.Combobox(RightMidFrame , state='readonly', font =('arial',14, 'bold'), width= 15)
cmbPaymentMethod['value']=('','Cash','Master Card','VISA Card','Debit Card')
cmbPaymentMethod.current (0)
cmbPaymentMethod.grid(row=5,column=3)



lblAddress1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="Address",bd=10, width= 15 ,anchor='w')
lblAddress1.grid(row=6,column=0)
txtAddress2 = Entry(RightMidFrame, font =('arial',14, 'bold'),bd=10, width= 50 )
txtAddress2.grid(row=6,column=1, columnspan=3)

lblAccountType1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="Account Type",bd=10, width= 15 ,anchor='w')
lblAccountType1.grid(row=7,column=0)
cmbAccountType = ttk.Combobox(RightMidFrame , state='readonly', font =('arial',14, 'bold'), width= 15)
cmbAccountType['value']=('','Credit Acct','Debit Acct','Customer Acct','Commercial Acct')
cmbAccountType.current (0)
cmbAccountType.grid(row=7,column=1)




lblVAT1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="VAT",bd=10, width= 15 ,anchor='w')
lblVAT1.grid(row=7,column=2)
cmbVAT1 = ttk.Combobox(RightMidFrame, textvariable =VAT , state='readonly', font =('arial',14, 'bold'), width= 14)
cmbVAT1['value']=('','Yes','No')
cmbVAT1.current (0)
cmbVAT1.grid(row=7,column=3)

lblTax1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="Tax",bd=10, width= 15 ,anchor='w')
lblTax1.grid(row=8,column=0)
lblTax2 = Label(RightMidFrame, font =('arial',14, 'bold'), textvariable=Tax,bd=10, width= 14, relief ='sunken' )
lblTax2.grid(row=8,column=1)

lblSubTotal1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="Sub Total",bd=10, width= 15 ,anchor='w')
lblSubTotal1.grid(row=8,column=2)
lblSubTotal2 = Label(RightMidFrame, font =('arial',14, 'bold'), textvariable=SubTotal,bd=10, width= 14, relief ='sunken' )
lblSubTotal2.grid(row=8,column=3)

lblTotal1 = Label(RightMidFrame, font =('arial',14, 'bold'), text="Total",bd=10, width= 15 ,anchor='w')
lblTotal1.grid(row=9,column=0)
lblTotal2 = Label(RightMidFrame, font =('arial',14, 'bold'), textvariable=Total,bd=10, width= 14, relief ='sunken' )
lblTotal2.grid(row=9,column=1)


btnTotal1 = Button(RightMidFrame, font =('arial',12, 'bold'), text="Total",bd=6, width=10, command= Product)
btnTotal1.grid(row=10,column=0)
lblReset = Button(RightMidFrame, font =('arial',12, 'bold'),  text="Reset",bd=6,width=10 , command= Reset)
lblReset.grid(row=10,column=1)
lblExit = Button(RightMidFrame, font =('arial',12, 'bold'),  text="Exit",bd=6, width=10, command= iExit )
lblExit.grid(row=10,column=3)




##============================Bottom Frame==================






root.mainloop()
