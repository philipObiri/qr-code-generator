from tkinter import *  # components for building the GUI
from PIL import ImageTk, Image  # for dynamically rendering the qrcode in png format
import segno  # for dynamically creating the qrcode


# A function to generate a qr code for a given link :
def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    if link_name:
        print("Enter a link name")
    elif link != "":
        # Generate a filename with a png extension
        filename = link_name + ".png"

        # Create QR Code with the link provided :
        qrcode = segno.make_qr(link)

        qrcode.save(filename, scale=8, dark="darkblue")

        # Generate a scannable qr coded image and save it as a png :
        generated_image = ImageTk.PhotoImage(Image.open(filename))
        image_label = Label(image=generated_image)
        image_label.image = generated_image

        # Render the image in the tkinter window :
        canvas.create_window(200, 450, window=image_label)
        message_label.config(
            text=f"QR Image Generated successfully for {link}",
            font=("EB Garamond,Arial, sans-serif", 16),
            fg="green",
        )

    else:
        message_label.config(
            text="Invalid Link", font=("EB Garamond,Arial, sans-serif", 16), fg="red"
        )
        # print("Invalid Link")


window = Tk()
window.title("Generate QR Code")
window.geometry("400x600")
window.resizable(False, False)
canvas = Canvas(window, width=400, height=600)
canvas.pack()

app_label = Label(
    window,
    text="QR Code Generator",
    fg="darkblue",
    font=("EB Garamond,Arial, sans-serif", 30),
)
canvas.create_window(200, 50, window=app_label)

name_label = Label(
    window, text="Link Name :", font=("EB Garamond,Arial, sans-serif", 20)
)
link_label = Label(window, text="Link : ", font=("EB Garamond,Arial, sans-serif", 20))

canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

name_entry = Entry(window, width=40)
link_entry = Entry(window, width=40)

canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)


message_label = Label(window)
canvas.create_window(200, 300, window=message_label)


button = Button(
    text="generate qr code",
    font=("EB Garamond,Arial, sans-serif", 18),
    padx=2,
    pady=2,
    command=generate,
)

canvas.create_window(200, 250, window=button)

window.mainloop()
