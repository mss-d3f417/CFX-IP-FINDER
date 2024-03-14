# Made By D3F417 - With Purple Heart
# Kidi Don't Copy This Code ! 
# GitHub : https://github.com/mss-d3f417
# Site : https://d3f417.site


from tkinter import *
from tkinter import messagebox
import requests
import pyperclip
import json

def search_ip():
    try:
        link = inf.get().strip()
        if not link:
            messagebox.showerror("ERROR!", "Link textbox can't be empty!")
        else:
            if not link.startswith("http"):
                link = "http://" + link
            response = requests.get(link)
            response.raise_for_status()
            ip = response.headers.get("X-Citizenfx-Url")
            if ip:
                ip_cut = ip.replace("http://", "").rstrip("/")
                pyperclip.copy(ip_cut)
                messagebox.showinfo("IP Found", f"IP: {ip_cut} copied to clipboard")
            else:
                messagebox.showwarning("Warning", "X-Citizenfx-Url header not found in the response.")
    except requests.ConnectionError:
        messagebox.showerror("ERROR!", "Connection error!")
    except requests.HTTPError as e:
        messagebox.showerror("HTTP Error", f"HTTP Error: {e}")

def get_player_info():
    try:
        link = inf.get().strip()
        if not link:
            messagebox.showerror("ERROR!", "Link textbox can't be empty!")
        else:
            if not link.startswith("http"):
                link = "http://" + link
            response = requests.get(link)
            response.raise_for_status()
            ip = response.headers.get("X-Citizenfx-Url")
            if ip:
                ip_cut = ip.replace("http://", "").rstrip("/")
                players_url = f"http://{ip_cut}/players.json"
                response_players = requests.get(players_url)
                response_players.raise_for_status()
                data = response_players.json()
                with open("Data/player-data.json", "w") as file:
                    json.dump(data, file, indent=4)
                messagebox.showinfo("Success", "Player data saved to player-data.json in Data folder!")
            else:
                messagebox.showwarning("Warning", "X-Citizenfx-Url header not found in the response.")
    except requests.ConnectionError:
        messagebox.showerror("ERROR!", "Connection error!")
    except requests.HTTPError as e:
        messagebox.showerror("HTTP Error", f"HTTP Error: {e}")
    except json.JSONDecodeError as e:
        messagebox.showerror("JSON Decode Error", f"Failed to decode JSON: {e}")

def get_player_data_with_id():
    try:
        id_value = id_entry.get().strip()
        if not id_value:
            messagebox.showerror("ERROR!", "ID textbox can't be empty!")
        else:
            try:
                with open("Data/player-data.json", "r") as file:
                    player_data = json.load(file)
                    id_found = False
                    for player in player_data:
                        if "id" in player and player["id"] == int(id_value):
                            id_found = True
                            pretty_data = json.dumps(player, indent=4)
                            messagebox.showinfo("Player Data", pretty_data)
                            break
                    if not id_found:
                        messagebox.showwarning("Warning", f"Player with ID {id_value} not found in player data!")
            except FileNotFoundError:
                messagebox.showwarning("Warning", "Player data file not found! Please fetch player data first.")
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Failed to decode JSON data from player-data.json!")
    except ValueError:
        messagebox.showerror("Error", "Invalid ID format. ID must be a number.")

gui = Tk(className="Find CFX IP - By D3F417")
gui.geometry("400x250")
gui.resizable(False, False)

bg_color = "#2B2B2B"
fg_color = "#FFFFFF"
entry_bg_color = "#8523db"
button_bg_color = "#5f84ce"

gui.config(bg=bg_color)
gui.tk_setPalette(background=bg_color, foreground=fg_color)

label1 = Label(gui, text="Provide cfx.re link:", bg=bg_color, fg=fg_color)
label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

inf = Entry(gui, borderwidth=2, relief="solid", bg=entry_bg_color, fg=fg_color)
inf.grid(row=0, column=1, padx=10, pady=10, sticky="we")

oki = Button(gui, text="Find IP", command=search_ip, bg=button_bg_color, fg=fg_color, relief=FLAT, width=10)
oki.grid(row=0, column=2, padx=10, pady=10)

player_button = Button(gui, text="Get Player Info", command=get_player_info, bg=button_bg_color, fg=fg_color, relief=FLAT, width=15)
player_button.grid(row=1, column=2, padx=10, pady=10)

id_label = Label(gui, text="Enter ID:", bg=bg_color, fg=fg_color)
id_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

id_entry = Entry(gui, borderwidth=2, relief="solid", bg=entry_bg_color, fg=fg_color)
id_entry.grid(row=2, column=1, padx=10, pady=10, sticky="we")

get_data_button = Button(gui, text="Get Data with ID", command=get_player_data_with_id, bg=button_bg_color, fg=fg_color, relief=FLAT, width=15)
get_data_button.grid(row=2, column=2, padx=10, pady=10)

gui.mainloop()
