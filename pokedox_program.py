import tkinter as tk 
import requests
#import datetime
#import json 
ability_ps = ""

def pokemon_type():
    pokemon_choice = input("Please type in a type of pokemon, in lowercase please.")
    url = "https://pokeapi.co/api/v2/type/"+ pokemon_choice +"/"
    response = requests.get(url)

    if response.status_code == 200:
        print("Request successful!")
        data =  response.json()
    else:
        print(f"Error: {response.status_code}")
        exit()

    for i in range(10):
        print(data['pokemon'][i]['pokemon']['name'].capitalize())

#--------------------------------------------------------------------

def pokemon_single(event):
    #pokemon_choice = input("Please type in a pokemon, in lowercase please.")
    pokemon_choice_ps = (entry_pokemon_single.get())
    url = "https://pokeapi.co/api/v2/pokemon/"+ pokemon_choice_ps +"/"
    response = requests.get(url)

    if response.status_code == 200:
        print("Request successful!")
        data = response.json()
    else:
        print(f"Error: {response.status_code}")#
        exit()

    for i in data['abilities']:
        #ability_ps = ability_ps + (i['ability']['name'])
        ability_label.config(text=(i['ability']['name']))
        
#--------------------------------------------------------------------
        
window = tk.Tk()
window.title("Pokemon Menu")
#window.geometry("300x300")

pokemon_single_menu = tk.Button(#menu button, goes to the window which does a single pokemon 
    text = "Click for a single pokemon!",
    bg="beige",
    fg="black",
)
pokemon_single_menu.bind("<Button-1>", pokemon_single)
pokemon_single_menu.grid(row=1, column=0)

pokemon_type_menu = tk.Button(
    text="Click for the type of pokemon!"
)
pokemon_type_menu.grid(row=0, column=1)

entry_pokemon_single = tk.Entry(fg="white", bg="#484848", width=10)
entry_pokemon_single.grid(row=0, column=1, padx=1, pady=1)



ability_label = tk.Label(
    text="some text"
)
ability_label.grid(row=0, column=0)

#second_window = tk.Tk()
#second_window.title("Pokeodex")



def pokemon_type():
    pokemon_choice = input("Please type in a type of pokemon, in lowercase please.")
    url = "https://pokeapi.co/api/v2/type/"+ pokemon_choice +"/"
    response = requests.get(url)

    if response.status_code == 200:
        print("Request successful!")
        data =  response.json()
    else:
        print(f"Error: {response.status_code}")
        exit()

    for i in range(10):
        print(data['pokemon'][i]['pokemon']['name'].capitalize())

#--------------------------------------------------------------------
        
#print("----MENU----\n")
#print("1: Search for Pokemon individually.")# Returns the first result
#print("2: Search for different Pokemon types.")# Returns the first ten results 
#menu_choice =  input("\n Which function do you want to do? Options shown above.")
#if menu_choice == "1":
#    pokemon_single()
#elif menu_choice == "2":
#    pokemon_type()

#--------------------------------------------------------------------

window.mainloop()