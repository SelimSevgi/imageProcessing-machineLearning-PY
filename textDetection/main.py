import cv2 as cv
import pytesseract
from tkinter import *
from tkinter import filedialog as fd

#pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#img = cv2.imread('images/textDetection.png')
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))

imgFilePath = ""
imgProcessResult = ""

# display image
def displayImage(name, img):
	cv.imshow(name, img)
	cv.waitKey(0)


def openFileDialog():
	filetypes = (
		('png files', '.png'),
	    )
	global imgFilePath
	imgFilePath = fd.askopenfilename(
		title='Open a file',
		initialdir='/',
		filetypes=filetypes)
	
	print("Selected image path : ", imgFilePath)


def detect_strings_on_image():
	global imgFilePath
	global imgProcessResult
	imgProcessResult = pytesseract.image_to_string(imgFilePath)
	print("Image processing result : ", imgProcessResult)



window = Tk()
window.title("Image Processing")
window.geometry("400x300")

# button to add image
add_image_btn =  Button (
		window,
		text='Add Image',
		command=openFileDialog
		)
add_image_btn.pack(expand=True)

# button to image processing
start_image_process_btn = Button(
		window,
		text='Start Image Process',
		command=detect_strings_on_image
		)
start_image_process_btn.pack(expand=True)


window.mainloop()


