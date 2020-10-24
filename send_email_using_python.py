import tkinter as tk
import smtplib

if __name__ == "__main__":
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("semder_email_id","sender_email_id_password")
    messgae="Email sending through python"
    s.sendmail("sender_email_id","receiver_email_id",messgae)
    s.quit()
