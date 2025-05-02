import tkinter as tk
from tkinter import ttk
from math import pi, sin, cos
from datetime import datetime
from tzlocal import get_localzone
from zoneinfo import ZoneInfo

class AnalogClock:

    def __init__(self, root):
        self.root = root
        self.root.title("Clock")

        self.centerX = 200
        self.centerY = 200
        self.radius = 100

        # Set default timezone (using system local timezone as default)
        self.default_timezone = self.get_local_timezone()
        try:
            self.current_timezone = ZoneInfo(self.default_timezone.key)
        except:
            self.current_timezone = ZoneInfo("Asia/Dubai")

        # Create GUI elements
        self.widgets()
        self.update_clock()

        
    def get_local_timezone(self):
        try:
            return get_localzone()
        except:
            return "UTC"
        
    def widgets(self):
        # Canvas for clock face
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='black')
        self.canvas.pack(pady=20)
        
        # Timezone selector - using common timezones
        self.timezones = ["Asia/Dubai", "UTC", "America/New_York", "Europe/London", "Asia/Tokyo", "Australia/Sydney"]
        self.tz_var = tk.StringVar(value=self.default_timezone)
        
        self.tz_selector = ttk.Combobox(
            self.root, 
            textvariable=self.tz_var,
            values=self.timezones,
            state="readonly",
            width=30
        )
        self.tz_selector.pack(pady=10)
        self.tz_selector.bind("<<ComboboxSelected>>", self.change_timezone)
        
        # Timezone display label
        self.tz_label = tk.Label(self.root, text=f"Timezone: {self.default_timezone}")
        self.tz_label.pack()
        
        # Draw static clock elements
        self.clockface()

    def change_timezone(self, event=None):
        try:
            self.current_timezone = ZoneInfo(self.tz_var.get())
            self.tz_label.config(text=f"Timezone: {self.tz_var.get()}")
        except:
            # Fallback to default if invalid timezone entered
            self.tz_var.set(self.default_timezone)
            self.current_timezone = ZoneInfo(self.default_timezone)
            self.tz_label.config(text=f"Timezone: {self.default_timezone}")
    
    def clockface(self):
        # Clock face
        self.canvas.create_oval( self.centerX - self.radius, self.centerY - self.radius, 
                            self.centerX + self.radius, self.centerY + self.radius, 
                            outline='white', width=2)
        # hour markers
        for hour in range(1, 13):
            angle = (hour/12) * 2*pi - pi/2
            x = self.centerX + cos(angle) * (self.radius - 20)
            y = self.centerY + sin(angle) * (self.radius - 20)
            self.canvas.create_text(x, y, text=str(hour), fill='white', font=('Arial', 14, 'bold'))

        self.am_pm_text = self.canvas.create_text(
        self.centerX,
        self.centerY + 60,
        text="AM",
        font=('Arial', 12, 'bold'),
        fill='white'
        )

    # Function to update the time
    def update_clock( self ):
        
        # Get current time in selected timezone
        now = datetime.now(self.current_timezone)
        hours = now.hour % 12
        minutes = now.minute
        seconds = now.second

        # Update digital AM/PM
        am_pm = "AM" if now.hour < 12 else "PM"
        self.canvas.itemconfig(self.am_pm_text, text=am_pm)
        
        # Calculate angles (convert to radians)
        sec_angle = (seconds / 60) * 2*pi - pi/2
        min_angle = (minutes / 60) * 2*pi + (seconds/60)*(pi/30) - pi/2
        hour_angle = (hours % 12 / 12) * 2*pi + (minutes/60)*(pi/6) - pi/2
        
        # Update hand positions
        self.canvas.delete('hands')  # Clear previous hands
        self.draw_hand(sec_angle, 100, 'red', 1)      # Second hand
        self.draw_hand(min_angle, 80, 'blue', 3)     # Minute hand
        self.draw_hand(hour_angle, 60, 'blue', 5)    # Hour hand
        
        self.root.after(1000, self.update_clock)  # Update every second

    def draw_hand(self, angle, length, color, width):
        # Calculate endpoint coordinates
        end_x = self.centerX + cos(angle) * length
        end_y = self.centerY + sin(angle) * length
        self.canvas.create_line(self.centerX, self.centerY, end_x, end_y, fill=color, width=width, tags='hands')



if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()