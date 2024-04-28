import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import credentials

def send_email(subject: str, body: str, to_email: str):
    host = 'smtp-mail.outlook.com'
    port = 587

    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(credentials.EMAIL, credentials.PASSWORD)

        message = MIMEMultipart()
        message['From'] = credentials.EMAIL
        message['To'] = to_email
        message['Subject'] = subject

        message.attach(MIMEText(body, 'plain'))

        server.sendmail(from_addr=credentials.EMAIL, to_addrs=to_email, msg=message.as_string())

        print(f'Email sent to {to_email}')

def send_reminder():
    subject = "Task Reminder"
    body = "Don't forget to complete your task!"
    to_email = recipient_email.get()
    send_email(subject, body, to_email)
    messagebox.showinfo("Reminder Sent", "Reminder email sent successfully.")

def schedule_reminder():
    reminder_time = reminder_time_entry.get()
    if not reminder_time:
        messagebox.showerror("Error", "Please enter reminder time.")
        return
    
    schedule.every().day.at(reminder_time).do(send_reminder)
    messagebox.showinfo("Reminder Scheduled", f"Reminder scheduled for {reminder_time}.")

    while True:
        schedule.run_pending()
        time.sleep(1)


root = tk.Tk()
root.title("Task Reminder")

reminder_time_label = tk.Label(root, text="Reminder Time (HH:MM):")
reminder_time_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
reminder_time_entry = tk.Entry(root, width=20)
reminder_time_entry.grid(row=0, column=1, padx=10, pady=5)

recipient_email_label = tk.Label(root, text="Recipient's Email:")
recipient_email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
recipient_email = tk.Entry(root, width=50)
recipient_email.grid(row=1, column=1, padx=10, pady=5)

schedule_button = tk.Button(root, text="Schedule Reminder", command=schedule_reminder)
schedule_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
