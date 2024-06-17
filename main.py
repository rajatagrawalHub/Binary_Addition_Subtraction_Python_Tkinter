import customtkinter
import tkinter
from tkinter import  messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x400")
root.title("Signed Mag Addition or Subtaction")
root.resizable(False,False)

avf = False

#Conversion Of Number into its Binary Form
def convert_signed_magnitude_binary(intForm):
    if int(intForm)>0:
        binForm = '0'+str(bin(int(intForm)))[2:]
    else:
        binForm = '1' + str(bin(int(intForm)))[3:]

    return binForm

def same_length(originalVal, compOne,compTwo=0):
    originalVal = originalVal[0] + originalVal[1:].zfill(max(compOne-1,compTwo-1))
    return originalVal

def Decimal_Given(binForm):
    if(binForm[0]=='0'):
        return str(int(binForm[1:],2))
    else:
        return str(0-int(binForm[1:],2))

def Verify_input():
    try:
        value1 = int(entry1.get())
    except ValueError as e:
        messagebox.showinfo("Error","Invalid Input in Number 1")
        entry1.delete(0,customtkinter.END)
        try:
            value2 = int(entry2.get())
        except ValueError as e:
            messagebox.showinfo("Error", "Invalid Input in Number 2")
            entry2.delete(0, customtkinter.END)
        return 0


    try:
        value2 = int(entry2.get())
    except ValueError as e:
        messagebox.showinfo("Error", "Invalid Input in Number 2")
        entry2.delete(0, customtkinter.END)
        try:
            value1 = int(entry1.get())
        except ValueError as e:
            messagebox.showinfo("Error", "Invalid Input in Number 1")
            entry1.delete(0, customtkinter.END)
        return 0

    return 1



def addition(binform_a, binform_b):
    global avf
    if binform_a[0] == binform_b[0]:
        resultint = int(binform_a[1:],2)+int(binform_b[1:],2)
        binResult =  binform_a[0]+ convert_signed_magnitude_binary(resultint)[1:]
        binResult = same_length(binResult,len(binform_a))
        if(len(binResult)>len(binform_a)):
            avf = True
    else:
        avf = False
        if int(binform_a[1:],2)>int(binform_b[1:],2):
            resultint = int(binform_a[1:], 2) - int(binform_b[1:], 2)
            binResult = binform_a[0] + convert_signed_magnitude_binary(resultint)[1:]
            binResult = same_length(binResult, len(binform_a))
        elif int(binform_b[1:], 2) > int(binform_a[1:], 2):
            resultint = int(binform_b[1:], 2) - int(binform_a[1:], 2)
            binResult = binform_b[0] + convert_signed_magnitude_binary(resultint)[1:]
            binResult = same_length(binResult, len(binform_a))
        else:
            binResult = '0'*len(binform_a)

    return binResult


def subtraction(binForm_a,binForm_b):
    if(binForm_b[0]=='0'):
        neg_binForm_b = '1' + binForm_b[1:]
    else:
        neg_binForm_b = '0' + binForm_b[1:]

    binResult = addition(binForm_a,neg_binForm_b)
    return binResult


def acion_add():
    if Verify_input()==1:
        a = entry1.get()
        b = entry2.get()

        binform_a = convert_signed_magnitude_binary(a);
        binform_b = convert_signed_magnitude_binary(b);

        binform_a = same_length(binform_a,len(binform_a),len(binform_b))
        binform_b = same_length(binform_b,len(binform_a),len(binform_b))

        labelvaluebin1.configure(text=binform_a)
        labelvaluebin2.configure(text=binform_b)

        labelvaluebinRes.configure(text=addition(binform_a,binform_b))
        labelvaluedecRes.configure(text=Decimal_Given(addition(binform_a,binform_b)))
        labelvalueavf.configure(text=str(avf))

def action_sub():
    if Verify_input() ==1:
        a = entry1.get()
        b = entry2.get()

        binform_a = convert_signed_magnitude_binary(a);
        binform_b = convert_signed_magnitude_binary(b);

        binform_a = same_length(binform_a, len(binform_a), len(binform_b))
        binform_b = same_length(binform_b, len(binform_a), len(binform_b))

        labelvaluebin1.configure(text=binform_a)
        labelvaluebin2.configure(text=binform_b)

        labelvaluebinRes.configure(text=subtraction(binform_a, binform_b))
        labelvaluedecRes.configure(text=Decimal_Given(subtraction(binform_a, binform_b)))
        labelvalueavf.configure(text=str(avf))


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady = 26,padx = 33, fill = "both",expand = True)

label1 = customtkinter.CTkLabel(master=frame,text="Number 1", font=("Roboto",24),text_color="#FFFFFF")
label1.place(x= 69,y = 20)

entry1 = customtkinter.CTkEntry(master=frame,width=151,border_width=2,border_color="#6D73FF")
entry1.place(x = 193, y = 20)


label2 = customtkinter.CTkLabel(master=frame,text="Number 2", font=("Roboto",24),text_color="#FFFFFF")
label2.place(x= 69,y = 80)

entry2 = customtkinter.CTkEntry(master=frame,width=151,border_width=2,border_color="#6D73FF")
entry2.place(x = 193, y = 80)

button1 = customtkinter.CTkButton(master=frame,width=88,height=31,bg_color="#0852AA",text="Addtion",text_color="#FFF7F7",font=("Roboto",12),command=acion_add)
button1.place(x= 150,y = 138)

button2 = customtkinter.CTkButton(master=frame,width=88,height=31,bg_color="#0852AA",text="Subtraction",text_color="#FFF7F7",font=("Roboto",12),command=action_sub)
button2.place(x= 255,y = 138)

frame2 = customtkinter.CTkFrame(master=frame,width=500,height=30,fg_color="White")
frame2.place(x=-30,y=190)

label = customtkinter.CTkLabel(master=frame2,text="Result",text_color="#2F2F2F",font=("Roboto",18))
label.place(x=220,y=1)

labelbin1 = customtkinter.CTkLabel(master=frame,text="Number 1 Binary:",text_color="#FFFFFF",font=("Roboto",12))
labelbin1.place(x= 40,y=242)

labelvaluebin1 = customtkinter.CTkLabel(master=frame,text="000000",text_color="#FFFFFF",font=("Roboto",12))
labelvaluebin1.place(x=150,y=242)

labelbin2 = customtkinter.CTkLabel(master=frame,text="Number 2 Binary:",text_color="#FFFFFF",font=("Roboto",12))
labelbin2.place(x= 40,y=267)

labelvaluebin2 = customtkinter.CTkLabel(master=frame,text="000000",text_color="#FFFFFF",font=("Roboto",12))
labelvaluebin2.place(x=150,y=267)

labelbinRes = customtkinter.CTkLabel(master=frame,text="Result:",text_color="#FFFFFF",font=("Roboto",12))
labelbinRes.place(x= 40,y=292)

labelvaluebinRes = customtkinter.CTkLabel(master=frame,text="000000",text_color="#FFFFFF",font=("Roboto",12))
labelvaluebinRes.place(x=150,y=292)

labeldecRes = customtkinter.CTkLabel(master=frame,text="Decimal Result:",text_color="#FFFFFF",font=("Roboto",12))
labeldecRes.place(x= 250,y=267)

labelvaluedecRes = customtkinter.CTkLabel(master=frame,text="000000",text_color="#FFFFFF",font=("Roboto",12))
labelvaluedecRes.place(x=360,y=267)

labelavfState = customtkinter.CTkLabel(master=frame,text="AVF:",text_color="#FFFFFF",font=("Roboto",12))
labelavfState.place(x= 250,y=292)

labelvalueavf = customtkinter.CTkLabel(master=frame,text="False",text_color="#FFFFFF",font=("Roboto",12))
labelvalueavf.place(x=360,y=292)


root.mainloop()
