
import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Stopwatch Display
        self.label = tk.Label(root, text="00:00:00", font=("Arial", 30))
        self.label.pack(pady=20, padx = 30)

        # Buttons
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side="left", padx=20)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side="left", padx=20)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side="left", padx=20)

    def update_display(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            time_str = time.strftime("%H:%M:%S", time.gmtime(self.elapsed_time))
            self.label.config(text=time_str)
            # Update the display every 1000 milliseconds (1 second)
            self.root.after(1000, self.update_display)

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_display()  # Start updating the display

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.label.config(text="00:00:00")  # Reset the display to initial time

root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()