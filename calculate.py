from Tkinter import *
import tkMessageBox
import class_def

def basic_1():																	# For entering numbers into entry boxes 

	global basechar_list_entry_1, entry_list_number_1, entry_list_number_2, flag
	global entry_str_number_1, entry_str_number_2
	basechar_list_entry_1 = []
	entry_list_number_1 = []
	entry_list_number_2 = []
	flag=0 																		# Used to keep track of the kinds of errors raised

	basechar_str_entry_1 = basechar_entry_1.get()
	entry_str_number_1 = entry_number_1.get()
	entry_str_number_2 = entry_number_2.get()

	for i in basechar_str_entry_1:
		if(i not in basechar_list_entry_1):
			basechar_list_entry_1.append(i)
		else:
			flag = 1
			raise Exception
	for i in entry_str_number_1:
		if(i in basechar_list_entry_1):
			entry_list_number_1.append(i)
		else:
			flag = 2
			raise Exception

	for i in entry_str_number_2:
		if(i in basechar_list_entry_1):
			entry_list_number_2.append(i)
		else:
			flag = 3
			raise Exception

def basic_2():																	# Function used for error handling
	try:
		basic_1()
	except Exception as a:
		global flag
		if(flag == 1):
			tkMessageBox.showinfo("Error","Please check the input given as the base characters of number system\nIt seems certain characters are repeating")
		elif(flag == 2):
			tkMessageBox.showinfo("Error", "Certain digits of number 1 are not in the given base characters")
		elif(flag == 3):
			tkMessageBox.showinfo("Error", "Certain digits of number 2 are not in the given base characters")

def get_plus():																	# Function for addition operation

	basic_2()
	if(flag==0 and (len(basechar_list_entry_1)!=0 and len(entry_list_number_1)!=0 and len(entry_list_number_2)!=0)):
		obj_Calculate = class_def.Calculater(basechar_list_entry_1)
		num1 = obj_Calculate.convert_to_decimal(entry_list_number_1)
		num2 = obj_Calculate.convert_to_decimal(entry_list_number_2)
		tkMessageBox.showinfo("Answer",entry_str_number_1 + " + " + entry_str_number_2 + " = " + "".join(obj_Calculate.convert_to_base(num1 + num2)))

def get_minus():																# Function for subtraction operation

	basic_2()
	if(flag==0 and (len(basechar_list_entry_1)!=0 and len(entry_list_number_1)!=0 and len(entry_list_number_2)!=0)):
		obj_Calculate = class_def.Calculater(basechar_list_entry_1)
		num1 = obj_Calculate.convert_to_decimal(entry_list_number_1)
		num2 = obj_Calculate.convert_to_decimal(entry_list_number_2)
		if(num1 >= num2):
			tkMessageBox.showinfo("Answer",entry_str_number_1 + " - " + entry_str_number_2 + " = " + "".join(obj_Calculate.convert_to_base(num1 - num2)))
		else:
			tkMessageBox.showinfo("Answer",entry_str_number_1 + " - " + entry_str_number_2 + " = " + "<negative>"+"".join(obj_Calculate.convert_to_base(num2 - num1)))

def get_multiply():																# Function for multiplication operation

	basic_2()
	if(flag==0 and (len(basechar_list_entry_1)!=0 and len(entry_list_number_1)!=0 and len(entry_list_number_2)!=0)):
		obj_Calculate = class_def.Calculater(basechar_list_entry_1)
		num1 = obj_Calculate.convert_to_decimal(entry_list_number_1)
		num2 = obj_Calculate.convert_to_decimal(entry_list_number_2)
		tkMessageBox.showinfo("Answer",entry_str_number_1 + " * " + entry_str_number_2 + " = " + "".join(obj_Calculate.convert_to_base(num1 * num2)))

def get_divide():																# Function for division operation

	basic_2()
	if(flag==0 and (len(basechar_list_entry_1)!=0 and len(entry_list_number_1)!=0 and len(entry_list_number_2)!=0)):
		obj_Calculate = class_def.Calculater(basechar_list_entry_1)
		num1 = obj_Calculate.convert_to_decimal(entry_list_number_1)
		num2 = obj_Calculate.convert_to_decimal(entry_list_number_2)
		try:																	# Implementation of exception handling
			result = num1 / num2
		except ZeroDivisionError:												# ZeroDivisionError is an inbuilt error
			tkMessageBox.showinfo("Error", "Division by zero not possible")
		else:
			tkMessageBox.showinfo("Answer",entry_str_number_1 + " / " + entry_str_number_2 + " = " + "".join(obj_Calculate.convert_to_base(num1 / num2)))

def get_remainder():															# Function for modulo division operation

	basic_2()
	if(flag==0 and (len(basechar_list_entry_1)!=0 and len(entry_list_number_1)!=0 and len(entry_list_number_2)!=0)):
		obj_Calculate = class_def.Calculater(basechar_list_entry_1)
		num1 = obj_Calculate.convert_to_decimal(entry_list_number_1)
		num2 = obj_Calculate.convert_to_decimal(entry_list_number_2)
		try:
			result = num1 % num2
		except ZeroDivisionError:
			tkMessageBox.showinfo("Error", "Division by zero not possible")
		else:
			tkMessageBox.showinfo("Answer",entry_str_number_1 + " % " + entry_str_number_2 + " = " + "".join(obj_Calculate.convert_to_base(num1 % num2)))

def get_exponent():																# Function for power operation

	basic_2()
	if(flag==0 and (len(basechar_list_entry_1)!=0 and len(entry_list_number_1)!=0 and len(entry_list_number_2)!=0)):
		obj_Calculate = class_def.Calculater(basechar_list_entry_1)
		num1 = obj_Calculate.convert_to_decimal(entry_list_number_1)
		num2 = obj_Calculate.convert_to_decimal(entry_list_number_2)
		tkMessageBox.showinfo("Answer",entry_str_number_1 + " ^ " + entry_str_number_2 + " = " + "".join(obj_Calculate.convert_to_base(num1 ** num2)))

def call_Calculate():															# GUI part for calculator

	app_Calculate = Tk()
	app_Calculate.wm_title("Calculator")
	frame_top = Frame(app_Calculate)
	frame_bottom = Frame(app_Calculate)
	frame_bottom_close = Frame(app_Calculate)
	frame_top.pack()
	frame_bottom_close.pack(side = BOTTOM)
	frame_bottom.pack(side = BOTTOM)

	global basechar_entry_1, entry_number_1, entry_number_2
	basechar_label_1 = Label(frame_top, text = "Enter the base characters of the number system")
	basechar_entry_1 = Entry(frame_top, bd = 10)
	basechar_entry_1.focus_set()

	label_number_1 = Label(frame_top, text = "Enter number 1")
	entry_number_1 = Entry(frame_top, bd = 10)

	label_number_2 = Label(frame_top, text = "Enter number 2")
	entry_number_2 = Entry(frame_top, bd = 10)

	b_plus = Button(frame_bottom, text = "+", command = get_plus, bg = "ivory")
	b_minus = Button(frame_bottom, text = "-", command = get_minus, bg = "ivory")
	b_multiply = Button(frame_bottom, text = "*", command = get_multiply, bg = "ivory")
	b_divide = Button(frame_bottom, text = "/", command = get_divide, bg = "ivory")
	b_remainder = Button(frame_bottom, text = "%", command = get_remainder, bg = "ivory")
	b_exponent = Button(frame_bottom, text = "^", command = get_exponent, bg = "ivory")
	b_close = Button(frame_bottom_close, text = "Close", command = app_Calculate.destroy, bg = "ivory")

	basechar_label_1.pack()
	basechar_entry_1.pack()
	label_number_1.pack()
	entry_number_1.pack()
	label_number_2.pack()
	entry_number_2.pack()
	b_plus.flash()
	b_minus.flash()
	b_multiply.flash()
	b_divide.flash()
	b_remainder.flash()
	b_exponent.flash()
	b_close.flash()
	b_plus.pack(side = LEFT)
	b_minus.pack(side = LEFT)
	b_multiply.pack(side = LEFT)
	b_divide.pack(side = LEFT)
	b_remainder.pack(side = LEFT)
	b_exponent.pack(side = LEFT)
	b_close.pack(side = BOTTOM)

	app_Calculate.mainloop()
