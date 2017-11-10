from Tkinter import *
import calculate
import convert
import scientific_calc

def main():
	main_app = Tk()
	main_app.wm_title("Home")
	frame_top = Frame(main_app)
	frame_top.pack()
	frame_bottom = Frame(main_app)
	frame_bottom.pack(side = BOTTOM)
	Calculate_b = Button(frame_top, text = "Calculate", command = calculate.call_Calculate, bg = "ivory")
	Convert_b = Button(frame_top, text = "Convert", command = convert.call_Convert, bg = "ivory")
	Scientific_b = Button(frame_top, text = "Scientific", command = scientific_calc.sci_calc, bg = "ivory")
	Exit_b = Button(frame_bottom, text = "Close", command = main_app.destroy, bg = "ivory")
	Calculate_b.flash()
	Convert_b.flash()
	Scientific_b.flash()
	Exit_b.flash()
	Calculate_b.pack(side = LEFT)
	Convert_b.pack(side = LEFT)
	Scientific_b.pack(side = LEFT)
	Exit_b.pack(side = BOTTOM)
	main_app.mainloop()

if __name__ == '__main__':
	main()