
import tkinter as tk
import wmi
import random


# =========================
# CPU TEMPERATURE
# =========================

def get_cpu_temp():
    """
    Read CPU temperature using the Windows WMI thermal zone interface.
    Returns temperature in Celsius or None if unavailable.
    """
    try:
        w = wmi.WMI(namespace="root\\wmi")
        temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]

        temp_c = (temperature_info.CurrentTemperature / 10.0) - 273.15
        return round(temp_c, 1)

    except Exception:
        return None


def get_simulated_temp():
    """
    Generate a simulated CPU temperature for testing.
    """
    return round(random.uniform(40.0, 70.0), 1)


# =========================
# GUI UPDATE
# =========================

def update_temp_label():
    if mode.get() == "Real WMI":
        temp = get_cpu_temp()

        if temp is not None:
            temp_label.config(
                text=f"CPU Temperature: {temp}°C"
            )
            status_label.config(
                text="Mode: Real WMI"
            )
        else:
            temp_label.config(
                text="Unable to read CPU temperature."
            )
            status_label.config(
                text="Mode: Real WMI - Sensor unavailable"
            )

    else:
        temp = get_simulated_temp()

        temp_label.config(
            text=f"CPU Temperature: {temp}°C"
        )
        status_label.config(
            text="Mode: Simulation"
        )

    root.after(2000, update_temp_label)


# =========================
# GUI
# =========================

root = tk.Tk()
root.title("CPU Temperature Monitor")
root.geometry("400x180")

temp_label = tk.Label(
    root,
    text="Reading temperature...",
    font=("Arial", 14)
)

temp_label.pack(pady=15)


mode = tk.StringVar(value="Real WMI")

mode_menu = tk.OptionMenu(
    root,
    mode,
    "Real WMI",
    "Simulation"
)

mode_menu.config(font=("Arial", 10))
mode_menu.pack()


status_label = tk.Label(
    root,
    text="Mode: Real WMI",
    font=("Arial", 10)
)

status_label.pack(pady=10)


update_temp_label()

root.mainloop()

