import class_def												# It has similarities to the calculate modulefrom Tkinter import *
import tkMessageBox
from Tkinter import * 

def basic_1():													# For entering numbers into entry box

	global flag, base_list_1, num_list_1, base_list_2, num_string_1
	base_list_1 = []
	base_list_2 = []
	num_list_1 = []
	flag=0

	base_string_1 = entry_input_base_characters_1.get()
	num_string_1 = entry_input_numbers_1.get()
	base_string_2 = entry_input_base_characters_2.get()

	for i in base_string_1:
		if(i not in base_list_1):
			base_list_1.append(i)
		else:
			flag=1
			raise Exception

	for i in num_string_1:
		if(i in base_list_1):
			num_list_1.append(i)
		else:
			flag=2
			raise Exception

	for i in base_string_2:
		if(i not in base_list_2):
			base_list_2.append(i)
		else:
			flag=3
			raise Exception

def get_values():												# It incorporates error handling.

	try:														# This makes a call to basic_1() and if we encounter any error we go to the exception part.
		basic_1()
		if((len(base_list_1)!=0 and len(num_list_1)!=0 and len(base_list_2)!=0) and flag==0):# Condition written for the case when the entry boxes are kept blank.It should throw up an error and not take the empty values as zero.
			obj_Convert = class_def.Converter(base_list_1, base_list_2)
			ans_str = "".join(obj_Convert.call_convert(num_list_1))
			tkMessageBox.showinfo("Answer", num_string_1 + " ---> " + ans_str)
	except Exception:
		if(flag==1):
			tkMessageBox.showinfo("Error", "Please check the input given as the base characters of number system 1\nIt seems certain characters are repeating")
		elif(flag==2):
			tkMessageBox.showinfo("Error", "It seems that there are certain characters that are not in the base characters of number system 1")
		elif(flag==3):
			tkMessageBox.showinfo("Error", "Please check the input given as the base characters of number system 2\nIt seems certain characters are repeating")

def call_Convert():												# GUI part for the Converter

	app_Convert = Tk()
	app_Convert.wm_title("Converter")
	global entry_input_base_characters_1, entry_input_numbers_1, entry_input_base_characters_2
	character_label_print_1 = Label(app_Convert, text = "Enter the base characters of number system 1")
	entry_input_base_characters_1 = Entry(app_Convert, bd = 10)
	entry_input_base_characters_1.focus_set()
	character_label_accept_1 = Label(app_Convert, text = "Enter the number in number system 1")
	entry_input_numbers_1 = Entry(app_Convert, bd = 10)

	character_label_print_2 = Label(app_Convert, text = "Enter the base characters of number system 2")
	entry_input_base_characters_2 = Entry(app_Convert, bd = 10)

	button_Convert = Button(app_Convert, text = "Convert", command = get_values, bg = "ivory")
	button_exit = Button(app_Convert, text = "Close", command = app_Convert.destroy, bg = "ivory")

	button_exit.flash()
	button_Convert.flash()
	character_label_print_1.pack()
	entry_input_base_characters_1.pack()
	character_label_accept_1.pack()
	entry_input_numbers_1.pack()
	character_label_print_2.pack()
	entry_input_base_characters_2.pack()
	button_Convert.pack()
	button_exit.pack()

	app_Convert.mainloop()