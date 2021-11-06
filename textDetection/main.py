import cv2
import pytesseract
from tkinter import *
from tkinter import filedialog as fd

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('images/textDetection.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))

imgFilePath = ""
imgProcessResult = ""

# # Karakterler
# hImg,wImg,_ = img.shape
# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#    #print(b)
#    b = b.split(' ')
#    #print(b)
#    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),2)
#    cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

# # Kelimeler
# hImg,wImg,_ = img.shape
# boxes = pytesseract.image_to_data(img)
# for x,b in enumerate(boxes.splitlines()):
#     #print(b)
#     if x!=0:
#         b = b.split()
#         print(b)
#         if len(b)==12:
#              x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#              cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
#              cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

# # Sayıların hepsini algılama
# hImg,wImg,_ = img.shape
# cong = r' --oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_data(img,config=cong)
# for x,b in enumerate(boxes.splitlines()):
#     #print(b)
#     if x!=0:
#         b = b.split()
#         print(b)
#         if len(b)==12:
#              x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#              cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
#              cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

#Sayıları teker teker alma
def sayilari_teker_teker_alma():
	hImg,wImg,_ = img.shape
	cong = r' --oem 3 --psm 6 outputbase digits'
	boxes = pytesseract.image_to_boxes(img,config=cong)
	for b in boxes.splitlines():
	   #print(b)
	   b = b.split(' ')
	   #print(b)
	   x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
	   cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),2)
	   cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)


	cv2.imshow('Result',img)
	cv2.waitKey(0)


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


