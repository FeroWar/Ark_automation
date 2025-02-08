import threading
import tkinter as tk
import customtkinter as ctk
import time
from ark import TribeLog, TribeLogMessage
from ark.Discord_Webhook import DiscordWebhook


class LogBotTab(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="#2B2B2B")
        self.pack(fill="both", expand=True)

        # Add top border
        border_top = tk.Frame(self, bg="#3800ff", height=4)
        border_top.pack(side="top", fill="x")

        # Add content below the border
        content_label = ctk.CTkLabel(self, text="Log Bot Control", font=("Arial", 16), fg_color="#333333",
                                     text_color="white")
        content_label.pack(pady=10)

        # Create Start and Stop buttons
        self.start_button = ctk.CTkButton(self, text="Start Log Bot", command=self.start_log_bot, fg_color="#00cc00")
        self.start_button.pack(side="left", padx=20, pady=20)

        self.stop_button = ctk.CTkButton(self, text="Stop Log Bot", command=self.stop_log_bot, fg_color="#cc0000")
        self.stop_button.pack(side="right", padx=20, pady=20)

        # Variables for the log bot loop
        self.bot_thread = None
        self.running = False  # Flag to control the bot loop

    def start_log_bot(self):
        if not self.running:  # Only start if not already running
            self.running = True
            self.bot_thread = threading.Thread(target=self.run_log_bot, daemon=True)
            self.bot_thread.start()
            print("Log Bot started.")
        else:
            print("Log Bot is already running.")

    def stop_log_bot(self):
        if self.running:
            self.running = False  # Stop the bot loop
            print("Stopping Log Bot...")
            if self.bot_thread:
                self.bot_thread.join()  # Wait for the thread to finish
            print("Log Bot stopped.")
        else:
            print("Log Bot is not running.")

    def run_log_bot(self):
        """Log Bot loop"""
        logs = TribeLog()
        discord = DiscordWebhook("https://discord.com/api/webhooks/1290639488388698114/NvupgLHjHQcv1Ft9Q0SWUp11EFkXVW84G4XUUZuCPmPNA913ZYaaupQKXf-MsY3NHLrB")

        time.sleep(1)
        while self.running:
            try:
                print("reading logs.")
                logs.open()
                log_events = logs.get_tribelog_events()

                # Only alert if there are logs, to avoid empty messages
                if log_events:
                    print("found logs to relay.")
                    discord.AlertDetection(log_events)

            except Exception as e:
                # Catch the exception and assign it to 'e'
                print(f"An error occurred: {e}")

            finally:
                # Will print in all cases, whether an exception occurred or not
                print("Finished processing.")
            time.sleep(10)


class ModMenu(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mod Menu")
        self.geometry("600x400")
        self.overrideredirect(True)  # Remove the default title bar
        self.attributes('-topmost', True)  # Always on top
        self.configure(fg_color="#2B2B2B")  # Set the background color

        # Create a frame for the draggable top bar with the close button
        title_bar = ctk.CTkFrame(self, height=30, fg_color="#2B2B2B", corner_radius=0)
        title_bar.pack(side="top", fill="x")

        close_button = ctk.CTkButton(title_bar, text="X", width=20, height=20, command=self.destroy,
                                     fg_color="red", hover_color="#cc0000", text_color="white", corner_radius=0)
        close_button.pack(side="right", padx=0, pady=0)

        title_bar.bind("<Button-1>", self.start_move)
        title_bar.bind("<B1-Motion>", self.do_move)

        # Create the tab container
        tab_container = ctk.CTkTabview(self, fg_color="#2B2B2B", border_width=0, segmented_button_selected_color="#2B2B2B", segmented_button_fg_color="#3800ff", segmented_button_unselected_color="#3800ff")
        tab_container.pack(side="top", fill="both", expand=True)

        tab_container.add("Log Bot")
        tab_container.set("Log Bot")

        self.create_tab_content(tab_container, "Log Bot", LogBotTab)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        x = (event.x_root - self.x)
        y = (event.y_root - self.y)
        self.geometry(f"+{x}+{y}")

    def create_tab_content(self, tab_container, tab_name, tab_class):
        tab = tab_container.tab(tab_name)
        tab.configure(fg_color="#333333")
        tab_class(tab)


if __name__ == "__main__":
    app = ModMenu()
    app.mainloop()
