import requests
import json
import tkinter as tk
from tkinter import ttk, messagebox

def main(country, city):
    URL = f"https://api.aladhan.com/v1/timingsByCity/14-09-2023?city={city}&country={country}t&method=8"
    response = requests.get(URL)
    info = response.json()
    if "data" in info:
        timings = info["data"]["timings"]
        timings_con = json.loads(json.dumps(timings))
        return timings_con
    else:
        return None
###############################
def fetch_fun():
    city = city_entry.get()
    country = country_entry.get()
    if city and country:
        prayertiming = main(country,city)
        for i,j in prayertiming.items():
            result.insert(tk.END, f"{i}: {j}: ")
    else:
        messagebox.showerror("Error","enable fetch")
app = tk.Tk()
app.title("Times of prayer")
frame = ttk.Frame(app,padding="20")
frame.grid(row = 0, column=0)
city_label = ttk.Label(frame,text="City")
city_label.grid(row=0,column=0)
city_entry=ttk.Entry(frame,width=20)
city_entry.grid(row=0,column=1)
country_label = ttk.Label(frame,text="country")
country_label.grid(row=1,column=0,pady=5)
country_entry=ttk.Entry(frame,width=20)
country_entry.grid(row=1,column=1,pady=5)
fetch_button = ttk.Button(frame,text="Get time prayer",command=fetch_fun)
fetch_button.grid(row=2,column=0,columnspan=2,pady=10)
result = tk.Listbox(frame,width=30,height=11)
result.grid(row=4,column=0,columnspan=2,pady=5)


# # ##########################    

# city_2 =input("enter city: ")
# country_2 =input("enter country: ")
# if city_2 and country_2:
#     prayertiming = main(country_2,city_2)
#     print(prayertiming)
# else:
#     print ("unabble fetch")