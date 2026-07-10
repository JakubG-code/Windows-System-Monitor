import tkinter as tk
import psutil
import wmi
import threading
import time

def get_cpu_temp():
    try:
        w = wmi.WMI(namespace="root\\wmi")
        temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]
        temp_c = (temperature_info.CurrentTemperature / 10.0) - 273.15
        return round(temp_c, 1)
    except:
        return None

def update_temp_label():
    temp = get_cpu_temp()
    if temp is not None:
        temp_label.config(text=f"Temperatura CPU: {temp}°C")
    else:
        temp_label.config(text="Nie można odczytać temperatury CPU.")
    # aktualizuj co 2 sekundy
    root.after(2000, update_temp_label)

# Tworzenie GUI
root = tk.Tk()
root.title("Monitor temperatury CPU")
root.geometry("300x100")

temp_label = tk.Label(root, text="Odczyt temperatury...", font=("Arial", 14))
temp_label.pack(pady=20)

# Start
update_temp_label()
root.mainloop()