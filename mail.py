import tkinter as tk
from tkinter import messagebox

def send_mail():
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    # Code to send the email goes here
    # You can use libraries like smtplib to send emails

    messagebox.showinfo("Success", "Email sent successfully")

# Create the main window
window = tk.Tk()
window.title("Mail Application")

# Create labels and entry fields for recipient, subject, and message
recipient_label = tk.Label(window, text="Recipient:")
recipient_label.pack()
recipient_entry = tk.Entry(window)
recipient_entry.pack()

subject_label = tk.Label(window, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(window)
subject_entry.pack()

message_label = tk.Label(window, text="Message:")
message_label.pack()
message_text = tk.Text(window, height=10, width=50)
message_text.pack()

# Create the send button
send_button = tk.Button(window, text="Send", command=send_mail)
send_button.pack()

# Start the GUI main loop
window.mainloop()