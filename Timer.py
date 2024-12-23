import tkinter as tk
import playsound as PS
import os

root = tk.Tk()
root.title("Timer")

# Function to validate and retrieve input
def get_input(entry):
    try:
        value = int(entry.get())
        return value
    except ValueError:
        return 0

# Timer
hourlabel = tk.Label(root, text="Hours: ")
hour = tk.Entry(root, width=30)
hourlabel.pack()
hour.pack()

minutelabel = tk.Label(root, text="Minutes: ")
minutelabel.pack()
minute = tk.Entry(root, width=30)
minute.pack()

secondlabel = tk.Label(root, text="Seconds: ")
secondlabel.pack()
second = tk.Entry(root, width=30)
second.pack()

def play_sound():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sound_path = os.path.join(script_dir, 'alarm.mp3')
    PS.playsound(sound_path)

def start_timer():
    hour_value = get_input(hour)
    minute_value = get_input(minute)
    second_value = get_input(second)
   
    total_seconds = hour_value * 3600 + minute_value * 60 + second_value
    if total_seconds > 0:
        root.after(total_seconds * 1000, play_sound)
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
    else:
        print("Please enter a valid time.")

def stop_timer():
    root.after_cancel(start_timer)
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    hour.delete(0, tk.END)
    minute.delete(0, tk.END)
    second.delete(0, tk.END)
    hour.insert(0, "0")
    minute.insert(0, "0")
    second.insert(0, "0")

start_button = tk.Button(root, text="Start timer!", command=start_timer)
start_button.pack()

stop_button = tk.Button(root, text="Stop timer", command=stop_timer, state=tk.DISABLED)
stop_button.pack()

root.mainloop()
