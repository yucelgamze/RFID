#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from tkinter import *
import time

FONT = ("didot",20,"bold")

class RFIDReader:
	def __init__(self, master):
		
		self.master = master
		master.title("RFID Tag Reader")
		
		self.label = Label(master, text = "Scan RFID Tag:", font=FONT, fg="black", bg="#02b9bf")
		self.label.pack(side="top", pady=10)
		
		
		self.scan_button = Button(master, text = "Scan", fg="#dcff05", bg="#17274c", font=FONT, command=self.scan_rfid)
		self.scan_button.pack(pady=30)
		
		
		self.tag_id_var = IntVar()
		self.tag_id_label = Label(master, fg="black", bg="white", font=FONT, textvariable=self.tag_id_var)
		self.tag_id_label.pack(pady=10)
		
		self.tag_text_var = StringVar()
		self.tag_text_label = Label(master, fg="black", bg="white", font=FONT, textvariable=self.tag_text_var)
		self.tag_text_label.pack(pady=10)

	def scan_rfid(self):
		
		reader = SimpleMFRC522()
		
		
		while  True:

			try: 
				tag_id, text = reader.read()
						
				def blink(pin):
					GPIO.output(pin, GPIO.HIGH)
					time.sleep(0.06)
					GPIO.output(pin, GPIO.LOW)
					time.sleep(0.06)
					return
					
				GPIO.setmode(GPIO.BOARD)
				GPIO.setup(11, GPIO.OUT)

				
				print(tag_id)
				print(text)
				self.tag_id_var.set(f"Tag ID: {tag_id}")
				self.tag_text_var.set(f"Text: {text}")
				
				for i in range(0, 10):
					blink(11)
					
			finally:

				GPIO.cleanup()
				
			if tag_id != None:
				break
				
if __name__=="__main__":
	
	window = Tk()
	window.geometry("500x500")
	window.config(background= "pink")
	frame = Frame(window)
	frame.pack(pady=20)
	app = RFIDReader(window)

	
	def close():
		window.destroy()
		#window.quit()
	
	global guit_button
	quit_button = Button(window, text="Close the window",bg="red", font=FONT, command=close).pack()
	window.mainloop()
