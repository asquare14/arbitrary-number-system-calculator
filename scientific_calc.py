import math
from Tkinter import *
import tkMessageBox
import class_def

def basic_1():																	# Function to take input from the user

	global flag, basechar_str, basechar_list, num_list
	global num_str, base
	basechar_list = []
	num_list = []
	flag=0
	basechar_str = Entry_basechar.get()
	num_str = Entry_num.get()
	base = len(basechar_str)
	for i in basechar_str:
		if(i not in basechar_list):
			basechar_list.append(i)
		else:
			flag = 1															# To keep track of which error to be raised
	for i in num_str:
		if(i in basechar_list):
			num_list.append(i)
		else:
			flag = 2

def basic_2(ans_int_val, obj_Scientific):										# Function which performs the mathematical operations
																				# Performing operation on the integer part
	global ans_str																# The number is operated in two seperate parts
	ans_str = ''																# 1. Integer part
																				# 2. Decimal part
	if(ans_int_val>=0):															# Deals with positive floating point numbers
		integer_part = "".join(obj_Scientific.convert_to_base(int(ans_int_val))) 
		ans_str += integer_part													
		ans_str += '.'															
		float_var = ans_int_val - int(ans_int_val)								
		if( float_var > 0):														# If the fractional part is non - zero
			ctr=0
			while(float_var == 0 or ctr<12):									# Math library returns the number with 12 decimal place accuracy
				float_var *= base
				ctr+=1															# Performing operation on decimal part
				ans_str += "".join(obj_Scientific.convert_to_base(int(float_var)))
				float_var -= int(float_var)
		else:		
			ans_str += obj_Scientific.N2[0]										# If the fractional part is zero
	else:																		# Deals with negative floating point numbers
		ans_str = '-'															
		ans_int_val *= -1
		integer_part = "".join(obj_Scientific.convert_to_base(int(ans_int_val)))
		ans_str += integer_part
		ans_str += '.'
		float_var = ans_int_val - int(ans_int_val)
		if( float_var > 0):														# If the fractional part is non - zero
			ctr=0
			while(float_var == 0 or ctr<12):									# Math library returns the number with 12 decimal place accuracy
				float_var *= base;
				ctr+=1															# Performing operation on decimal part
				ans_str += "".join(obj_Scientific.convert_to_base(int(float_var)))
				float_var -= int(float_var)
		else:		
			ans_str += obj_Scientific.N2[0]										# If the fractional part is zero

def prompt():																	# Function to generate error message

	if(flag==1):
		tkMessageBox.showinfo("Error", "Please check the input given as the base characters of number system\nIt seems certain characters are repeating")
	elif(flag==2):
		tkMessageBox.showinfo("Error", "Certain digits of number are not in the given base characters")					

def get_sin():																	# Computes the sin of the required value

	basic_1()
	if(flag==0 and len(basechar_str)!=0 and len(num_str)!=0):
		obj_Scientific = class_def.Calculater(basechar_list)
		num1 = obj_Scientific.convert_to_decimal(num_list)
		ans_int_val = math.sin(math.radians(num1))
		basic_2(ans_int_val, obj_Scientific)
		tkMessageBox.showinfo("Answer","sin("+num_str+") = "+ans_str)
	prompt()			

def get_cos():																	# Computes the cos of the required value
	
	basic_1()
	if(flag==0 and len(basechar_str)!=0 and len(num_str)!=0):
		obj_Scientific = class_def.Calculater(basechar_list)
		num1 = obj_Scientific.convert_to_decimal(num_list)
		ans_int_val = math.cos(math.radians(num1))
		basic_2(ans_int_val, obj_Scientific)
		tkMessageBox.showinfo("Answer","cos("+num_str+") = "+ans_str)
	prompt()

def get_tan():																	# Computes the tan of the required value

	basic_1()
	if(flag==0 and len(basechar_str)!=0 and len(num_str)!=0):
		obj_Scientific = class_def.Calculater(basechar_list)
		num1 = obj_Scientific.convert_to_decimal(num_list)
		tmp = num1
		x = tmp/90
		if(((num1 % 90) == 0) and (x%2 == 1)):	
			tkMessageBox.showinfo("Error","Not Defined")
		elif((num1 % 90 == 0) and (x % 2 == 0)):								# Math library returns a very large negative number (modulus of the value is very small) 
			ans_int_val = 0														# To prevent that we have decided to treat this as a corner case
			basic_2(ans_int_val, obj_Scientific)
			tkMessageBox.showinfo("Answer","tan("+num_str+") = "+ans_str)
		else:
			ans_int_val = math.tan(math.radians(num1))
			basic_2(ans_int_val, obj_Scientific)
			tkMessageBox.showinfo("Answer","tan("+num_str+") = "+ans_str)

	prompt()

def get_arcsin():																# Computes the arcsin of the required value

	basic_1()
	if(flag==0 and len(basechar_str)!=0 and len(num_str)!=0):
		obj_Scientific = class_def.Calculater(basechar_list)
		num1 = obj_Scientific.convert_to_decimal(num_list)	
		if(num1 <=1 and num1 >=-1):
			ans_int_val = math.asin(num1)
			basic_2(ans_int_val, obj_Scientific)
			tkMessageBox.showinfo("Answer","asin("+num_str+") = "+ans_str)
		else:
			tkMessageBox.showinfo("Error", "Not defined")	
	prompt()

def get_arccos():																# Computes the arccos of the required value

	basic_1()
	if(flag==0 and len(basechar_str)!=0 and len(num_str)!=0):
		obj_Scientific = class_def.Calculater(basechar_list)
		num1 = obj_Scientific.convert_to_decimal(num_list)	
		if(num1 <=1 and num1 >=-1):	
			ans_int_val = math.acos(num1)
			basic_2(ans_int_val, obj_Scientific)
			tkMessageBox.showinfo("Answer","acos("+num_str+") = "+ans_str)
		else:
			tkMessageBox.showinfo("Error", "Not defined")
	prompt()	

def get_arctan():																# Computes the arctan of the required value

	basic_1()
	if(flag==0 and len(basechar_str)!=0 and len(num_str)!=0):
		obj_Scientific = class_def.Calculater(basechar_list)
		num1 = obj_Scientific.convert_to_decimal(num_list)	
		ans_int_val = math.atan(num1)
		basic_2(ans_int_val, obj_Scientific)
		tkMessageBox.showinfo("Answer","atan("+num_str+") = "+ans_str)
	prompt()	

def sci_calc():																	# Provides the GUI interface for the scientific calculator

	app_scientific = Tk()
	app_scientific.wm_title("Scientific Calculator")
	frame_top = Frame(app_scientific)
	frame_top.pack(side = TOP)
	frame_bottom_close = Frame(app_scientific)
	frame_bottom_close.pack(side = BOTTOM)
	frame_bottom_inverse = Frame(app_scientific)
	frame_bottom_inverse.pack(side = BOTTOM)
	frame_bottom = Frame(app_scientific)
	frame_bottom.pack(side = BOTTOM)

	global Entry_basechar,Entry_num
	Label_basechar = Label(frame_top, text = "Enter the base characters of the number system")
	Entry_basechar = Entry(frame_top, bd =10)
	Entry_basechar.focus_set()
	Label_num_input = Label(frame_top, text = "Enter the number in the number system")
	Entry_num = Entry(frame_top, bd =10)

	Label_basechar.pack()
	Entry_basechar.pack()
	Label_num_input.pack()
	Entry_num.pack()	

	sin_b = Button(frame_bottom, text = "sin", command = get_sin, bg = "ivory")
	cos_b = Button(frame_bottom, text = "cos", command = get_cos, bg = "ivory")
	tan_b = Button(frame_bottom, text = "tan", command = get_tan, bg = "ivory")

	asin_b = Button(frame_bottom_inverse, text = "asin", command = get_arcsin, bg = "ivory")
	acos_b = Button(frame_bottom_inverse, text = "acos", command = get_arccos, bg = "ivory")
	atan_b = Button(frame_bottom_inverse, text = "atan", command = get_arctan, bg = "ivory")
	close_b = Button(frame_bottom_close, text = "Close", command = app_scientific.destroy, bg = "ivory")
	
	sin_b.flash()
	cos_b.flash()
	tan_b.flash()
	asin_b.flash()
	acos_b.flash()
	atan_b.flash()
	close_b.flash()
	
	sin_b.pack(side = LEFT)
	cos_b.pack(side = LEFT)
	tan_b.pack(side = LEFT)
	asin_b.pack(side = LEFT)
	acos_b.pack(side = LEFT)
	atan_b.pack(side = LEFT)
	close_b.pack(side = BOTTOM)
	
	app_scientific.mainloop()