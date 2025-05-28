import tkinter as tk
import math

# Constants
G = 6.674e-11
M = 5.972e24
earth_radius = 6371

def orbital_speed():
    try:
        altitude_km = float(altitude_entry.get())
        r = (earth_radius + altitude_km) * 1000
        speed = math.sqrt(G * M / r)
        result_label.config(text=f"Orbital Speed: {speed:.2f} m/s")
    except ValueError:
        result_label.config(text="Please enter a valid number for altitude.")

def orbital_type():
    try:
        altitude_km = float(altitude_entry.get())
        if 100 <= altitude_km < 2000:
            orbit_type = "Low Earth Orbit or LEO"
        elif 2000 <= altitude_km < 35786:
            orbit_type = "Medium Earth Orbit or MEO"
        elif altitude_km == 35786:
            orbit_type = "Geostationary Orbit or GEO"
        elif altitude_km > 35786:
            orbit_type = "High Earth Orbit or HEO"
        else:
            orbit_type = "Below Orbit Threshold"
        orbit_type_label.config(text=f"Orbit Type: {orbit_type}")
    except ValueError:
        orbit_type_label.config(text=f"Please enter a valid number for altitude.")

def orbital_period():
    try:
        altitude_km = float(altitude_entry.get())
        r = (earth_radius + altitude_km) * 1000
        T = 2 * math.pi * math.sqrt(pow(r, 3) / (G * M))
        total_seconds = int(T)
        hours = total_seconds // 3600
        minutes = int((total_seconds % 3600) / 60)
        seconds = total_seconds % 60
        orbital_period_label.config(text=f"Orbital Period: {hours}:{minutes}:{seconds}")
    except ValueError:
        orbital_period_label.config(text=f"Please enter a valid number for altitude.")
        
def escape_velocity():
    try:
        altitude_km = float(altitude_entry.get())
        r = (altitude_km + earth_radius) * 1000
        v = math.sqrt((2 * G * M) / r)
        velocity_label.config(text=f"Escape Velocity: {v:.2f} m/s")
    except ValueError:
        velocity_label.config(text="Please enter a valid number for altitude.")

root = tk.Tk()
root.title("Orbital Calculator")
root.state('zoomed')
altitude_label = tk.Label(root, text="Enter the altitude of an object(km): ")
altitude_label.pack(pady=10)
altitude_entry = tk.Entry(root)
altitude_entry.pack(pady=5)
speed_button = tk.Button(root, text="Calculate Orbit Speed", command=orbital_speed)
speed_button.pack(pady=5)
orbit_button = tk.Button(root, text="Determine Orbital Type", command=orbital_type)
orbit_button.pack(pady=5)
period_button = tk.Button(root, text="Determine Orbital Period", command=orbital_period)
period_button.pack(pady=5)
velocity_btn = tk.Button(root, text="Determine Escape Velocity", command=escape_velocity)
velocity_btn.pack(pady=5)
result_label = tk.Label(root, text="Orbital Speed: ", font=("Arial", 14))
result_label.pack(pady=10)
orbit_type_label = tk.Label(root, text="Orbit Type: ", font=("Arial", 14))
orbit_type_label.pack(pady=10)
orbital_period_label = tk.Label(root, text="Orbital Period: ", font=("Arial", 14))
orbital_period_label.pack(pady=10)
velocity_label = tk.Label(root, text="Escape Velocity: ", font=("Arial", 14))
velocity_label.pack(pady=10)
root.mainloop()
