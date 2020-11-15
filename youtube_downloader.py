from tkinter import *
from pytube import YouTube
from PIL import ImageTk, Image 


root = Tk()

#size the window
root.geometry('500x200')
#allow the resizing of the window
root.resizable(0, 0)
#create title of the window
root.title('Youtube Video Downloader')
#create icon (icon has to be in 'iso' format)
root.iconbitmap('Graphics-Vibe-Classic-3d-Social-Youtube.ico')

#load the image onto the screen
logo_image = Image.open('youtube_image.jpg')
photo = ImageTk.PhotoImage(logo_image)
label = Label(image=photo)
label.pack()

#create StringVar for link input
link = StringVar()
#create label that will be displayed at top of box
Label(root, text='Paste Link Below: ', font='arial 20 bold').place(x=135, y=10)
#Entry for the link
enter_link = Entry(root, width=70, text=link).place(x=35, y=135)



def downloader():
	"""function to download the youtube video"""
	url = YouTube(str(link.get()))
	video = url.streams.first().download()
	Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=158)


#create a download button
Button(root, text='DOWNLOAD', font='arial 15 bold', bg='red2', command=downloader).place(x=180, y=158)



root.mainloop()

