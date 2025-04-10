import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For handling images
import smtplib
import webbrowser

# Predefined credentials for Anushka
registered_email = "anuushkaaa1230@gmail.com"
registered_phone = "9820919318"

def login():
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    if email == registered_email and phone == registered_phone:
        messagebox.showinfo("Login Success", "Welcome, Anushka!")
        show_main_screen()

    
    else:
        messagebox.showerror("Login Failed", "Incorrect email or phone number.\nPlease try again.")

def show_login_screen():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()
        
    # Set a soothing background color
    root.configure(bg="#E0F7FA")

    # Create a centered frame to act as the login card
    login_frame = tk.Frame(root, bg="white", bd=2, relief="groove", padx=20, pady=20)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")
    
    title_label = tk.Label(login_frame, text="Women's Safety App", font=("Helvetica", 22, "bold"), fg="#00796B", bg="white")
    title_label.pack(pady=(0, 20))
    
    # Email input
    email_label = tk.Label(login_frame, text="Email ID:", font=("Helvetica", 12), bg="white")
    email_label.pack(anchor="w")
    global email_entry
    email_entry = tk.Entry(login_frame, font=("Helvetica", 12), width=30)
    email_entry.pack(pady=(0, 10))
    
    # Phone input
    phone_label = tk.Label(login_frame, text="Phone Number:", font=("Helvetica", 12), bg="white")
    phone_label.pack(anchor="w")
    global phone_entry
    phone_entry = tk.Entry(login_frame, font=("Helvetica", 12), width=30)
    phone_entry.pack(pady=(0, 20))
    
    login_button = tk.Button(login_frame, text="Login", font=("Helvetica", 14, "bold"), bg="#00796B", fg="white", width=20, command=login)
    login_button.pack()

def show_main_screen():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

        def sho-main():
            for widget in root.winfo_childern()
            widget.destroy()

            # atharva kesarkar
    
    # Header section with a modern background color
    header_frame = tk.Frame(root, bg="#00796B")
    header_frame.pack(fill="x")
    header_label = tk.Label(header_frame, text="Women's Safety App", font=("Helvetica", 24, "bold"),
                            fg="white", bg="#00796B", padx=20, pady=10)
    header_label.pack()
    
    # Main content frame with a light background
    content_frame = tk.Frame(root, bg="#E0F7FA")
    content_frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Display a banner image of a strong woman
    try:
        img = Image.open("woman_strong.png")  # Replace with your image path
        img = img.resize((320, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        image_label = tk.Label(content_frame, image=photo, bg="#E0F7FA")
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        print("Image load error:", )
        
    

    # Action frame for SOS and nearby searches
    action_frame = tk.Frame(content_frame, bg="white", bd=1, relief="ridge", padx=20, pady=20)
    action_frame.pack(pady=10)
    
    sos_button = tk.Button(action_frame, text="Send SOS", font=("Helvetica", 16, "bold"),
                           bg="#D32F2F", fg="white", width=20, command=send_sos)
    sos_button.pack(pady=10)
    
    nearby_label = tk.Label(action_frame, text="Find Nearby:", font=("Helvetica", 16, "bold"),
                             fg="#424242", bg="white")
    nearby_label.pack(pady=10)
    
    # Arranging nearby buttons in a grid layout
    buttons_frame = tk.Frame(action_frame, bg="white")
    buttons_frame.pack()
    
    hospital_button = tk.Button(buttons_frame, text="Hospitals", font=("Helvetica", 12),
                                bg="#00796B", fg="white", width=15,
                                command=lambda: find_nearby("hospitals"))
    hospital_button.grid(row=0, column=0, padx=10, pady=5)
    
    pharmacy_button = tk.Button(buttons_frame, text="Pharmacies", font=("Helvetica", 12),
                                bg="#00796B", fg="white", width=15,
                                command=lambda: find_nearby("pharmacies"))
    pharmacy_button.grid(row=0, column=1, padx=10, pady=5)
    
    police_button = tk.Button(buttons_frame, text="Police Stations", font=("Helvetica", 12),
                              bg="#00796B", fg="white", width=32,
                              command=lambda: find_nearby("police stations"))
    police_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
    
    # Result message area for the SOS message feedback
    global result_frame
    result_frame = tk.Frame(content_frame, bg="#E0F7FA", pady=10)
    result_frame.pack()

    atharva kesarkar is the were to be the known and the people this is called were to be the become and men can do anything for their passion and a
    
    # Footer message
    footer = tk.Label(root, text="Stay safe, help is always near!", font=("Helvetica", 10, "italic"),
                     bg="#E0F7FA", fg="#424242")
    footer.pack(side="bottom", fill="x", pady=(0, 10))

def send_sos():
    try:
        sender_email = "kesarkaratharva@gmail.com"
        sender_password = "1210"  # Consider using an app-specific password for Gmail
        guardian_email = "9820919318@sms.gateway"  # SMS Gateway placeholder
        police_email = "mumbaipolice@gmail.com"
        message = "SOS! I need immediate help.\nName: Anushka\nAddress: Dombivli"

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, guardian_email, message)
            server.sendmail(sender_email, police_email, message)
        result_message = "Message sent successfully!"
    except Exception as e:
        print("Error sending message:", e)
        # Even if there's an error, per your requirement, we show success.
        result_message = "Message sent successfully!"
    
    # Clear previous message area if any
    for widget in result_frame.winfo_children():
        widget.destroy()
    
    sent_message_label = tk.Label(result_frame,
                                  text=f"{result_message}\nTo Guardian: {guardian_email}\nTo Police Station: {police_email}",
                                  font=("Helvetica", 12), fg="#212121", bg="#E0F7FA",
                                  wraplength=400, justify="left")
    sent_message_label.pack()

def find_nearby(category):
    base_url = "https://www.google.com/maps/search/"
    webbrowser.open(base_url + category)

# Tkinter setup
root = tk.Tk()
root.title("Women's Safety App")
root.geometry("500x650")
root.configure(bg="#E0F7FA")

# Start with the login screen
show_login_screen()

root.mainloop()