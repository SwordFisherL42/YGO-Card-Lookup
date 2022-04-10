from ygolib.helpers import get_cached_data, get_cached_image, verify_download_directory
from tkinter import *
from PIL import ImageTk,Image


def button_action(*args):
    global main_image
    global name_label
    global desc_label
    global atk_def_label
    global entry_id
    global entry
    try:
        card_id = int(entry_id.get())
    except:
        print("Card ID must be a number")
        return
    card_data = get_cached_data(card_id)
    if card_data is None:
        return
    for data in card_data["data"]:
        level = data.get("level", None)
        atk = data.get("atk", None)
        defn = data.get("def", None)
        _name = f"Name: {data['name']}"
        _desc = f"Description: {data['desc']}"
        _level = f"Level: {'✪'*level}" if level else ""
        _atk = f"ATK/ {atk}" if atk else ""
        _def = f"DEF/ {defn}" if defn else ""
        for image in data["card_images"]:
            img_file = get_cached_image(image["image_url"])
            break
        print(f"{_name}\n{_desc}\n{_level}\n{_atk} {_def}\n")
        img = ImageTk.PhotoImage(Image.open(img_file))
        main_image.configure(image=img)
        main_image.image = img
        name_label.configure(text=data['name'], font=("Calibri", 25))
        desc_label.configure(text=data['desc'], font=("Calibri", 14, 'bold'))
        if level is not None:
            atk_def_label.configure(
                text=f"{_level}\n{_atk} {_def}", 
                font=("Calibri", 14))
        else:
            atk_def_label.configure(text="\t\n", font=("Calibri", 14))
        entry_id.set("")
        entry.focus()
        break


if __name__ == "__main__":
    verify_download_directory()
    default_card_id = 6983839
    # Define & Setup GUI components 
    root = Tk()
    root.iconbitmap('ico/eye-of-ra-sm.ico')
    root.title("Yu-Gi-Oh Card ID Lookup")
    canvas = Canvas(root, width = 950, height = 625)
    main_image = Label(root)
    name_label = Label(root)
    desc_label = Label(root, justify=LEFT, wraplength=400)
    atk_def_label = Label(root, justify=LEFT)
    entry_prompt = Label(root, text="Card ID: ", justify=RIGHT, width=6, font=("Calibri", 16, 'bold'))
    entry_id = StringVar()
    entry = Entry(root, textvariable=entry_id, justify=CENTER, width=20, font=("Calibri", 16))
    entry.bind('<Return>', button_action)
    main_button = Button(root, text="Get Info", command=button_action, width=19, justify=CENTER, font=("Calibri", 16))
    # Pack components
    canvas.pack()
    main_image.pack()
    name_label.pack()
    atk_def_label.pack()
    desc_label.pack()
    entry_prompt.pack()
    entry.pack()
    main_button.pack()
    # Place components
    main_image.place(x=0, y=0, anchor=NW)
    name_label.place(x=500, y=100, anchor=NW)
    atk_def_label.place(x=500, y=150, anchor=NW)
    desc_label.place(x=500, y=200, anchor=NW)
    entry_prompt.place(x=725, y=575, anchor=SE)
    entry.place(x=950, y=575, anchor=SE)
    main_button.place(x=950, y=625, anchor=SE)
    # Initialize window
    entry_id.set(str(default_card_id))
    entry.focus()
    root.mainloop()
