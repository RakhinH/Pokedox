import tkinter as tk 

window = tk.Tk()
window.title("Pokemon Menu")
window.configure(bg="#e6f7ff")



#window.geometry("300x300")

#pokemon_single_menu = tk.Button(#menu button, goes to the window which does a single pokemon 
    #text = "Click for a single pokemon!",
    #bg="beige",
    #fg="black",
#)
#pokemon_single_menu.bind("<Button-1>", pokemon_single)
#pokemon_single_menu.grid(row=1, column=0)

#pokemon_type_menu = tk.Button(
    #text="Click for the type of pokemon!"
#)
#pokemon_type_menu.grid(row=0, column=1)

#entry_pokemon_single = tk.Entry(fg="white", bg="#484848", width=10)
#entry_pokemon_single.grid(row=0, column=1, padx=1, pady=1)



#ability_label = tk.Label(
    #text="some text"
#)
#ability_label.grid(row=0, column=0)

#second_window = tk.Tk()
#second_window.title("Pokeodex")

def search_indivdual_tab():
    new_window = tk.Toplevel()
    new_window.geometry("100x100")

def search_group_tab():
    new_window = tk.Toplevel() 


frame1 = tk.Frame(master=window, relief = tk.GROOVE, borderwidth=3)
frame1.pack()

menu_search_indivdual = tk.Button(#first button, on the left, in the first window
    text="Search for a single pokemon.",
    fg="black",
    bg="#0099e6",
    command = search_indivdual_tab,
    master=frame1
)
menu_search_indivdual.grid(row=0, column=0, padx=0, pady=4)


menu_search_group = tk.Button(#second button, on the left, in the first window
    text="Search for a type of pokemon.",
    fg="black",
    bg="#33bbff",
    command = search_group_tab,
    master=frame1
)
menu_search_group.grid(row=0, column=1, padx=10, pady=4)


menu_search_saved_data = tk.Button(#third button, on the left, in the first window
    text="Search/View your saved Pokemons.",
    fg="black",
    bg="#66ccff",
    master=frame1
)
menu_search_saved_data.grid(row=0, column=2, padx=1, pady=4)



window.mainloop()