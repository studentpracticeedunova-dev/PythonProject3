# from tkinter import *
# from tkinter import messagebox
# from tkinter.ttk import Combobox
# from tkcalendar import DateEntry
#
#
# booking_history=[]
#
# root = Tk()
# root.title("Airline Ticket Booking System")
# root.geometry("950x650")
# root.config(bg="#0B1F3A")
#
#
#
#
# Label(root, text="AIRLINE TICKET BOOKING SYSTEM",
#       font=("Segoe UI", 30, "bold"),
#       bg="#0B1F3A",
#       fg="dark blue").pack(pady=20)
# Label(root,text="Book Your Dream Journey Around the World",
#       font=("Segoe UI",16,"italic"),
#       bg="#0B1F3A",
#       fg="#FFD700").pack()
#
#
# def open_search():
#     search = Toplevel(root)
#     search.title("Search Flights")
#     search.geometry("700x500")
#     search.config(bg="lightcyan")
#
#
#
#     Label(search, text="Search Flights",
#           font=("Segoe UI", 20, "bold"),
#           bg="lightcyan",
#           fg="navy").pack(pady=15)
#
#     Label(search, text="From",
#           bg="light cyan").pack()
#     from_entry = Combobox(search,
#                        values=["Delhi","Mumbai","Bengaluru","Chennai","Kolkata"],
#                        width=25,
#                           state="readonly")
#     from_entry.pack()
#
#     Label(search, text="To").pack()
#     to_entry = Combobox(search,
#                      values=["Delhi", "Mumbai", "Bengaluru", "Chennai", "Kolkata"],
#                      width=25,
#                         state="readonly")
#     to_entry.pack()
#
#     Label(search, text="Journey Date",bg="light cyan").pack()
#
#
#     date_entry = DateEntry(
#         search,
#         width=27,
#         borderwidth=2,
#         date_pattern="dd-mm-yyyy"
#     )
#     date_entry.pack(pady=5)
#
#     Label(search, text="Passengers",bg="light cyan").pack()
#     passenger_entry = Entry(search, width=30)
#     passenger_entry.pack()
#
#     def search_flight():
#         from_city=from_entry.get()
#         to_city=to_entry.get()
#         journey_date=date_entry.get()
#         passenger_text=passenger_entry.get().strip()
#
#
#         if from_city == to_city:
#             messagebox.showerror(
#                 "Error",
#                 "From and To cities cannot be the same."
#             )
#             return
#
#         if not passenger_text.isdigit() or int(passenger_text) <= 0:
#             messagebox.showerror(
#                 "Error",
#                 "Enter a valid number of passengers."
#             )
#             return
#
#         passengers = int(passenger_text)
#
#         if passengers > 10:
#             messagebox.showerror(
#                 "Error",
#                 "Maximum 10 passengers are allowed."
#             )
#             return
#
#         search.destroy()
#         select_flights(
#             from_city,
#             to_city,
#             journey_date,
#             passengers
#         )
#
#
#     def select_flights(from_city,to_city,journey_date,passengers):
#         route=(from_city,to_city)
#
#         flight=Toplevel(root)
#         flight.title("Select Flights")
#         flight.geometry("700x500")
#         flight.config(bg="lightyellow")
#
#
#
#         flight_data = {
#             ("Delhi", "Mumbai"): [
#                 "AIR INDIA - 08:00 AM - Rs.5000",
#                 "INDIGO - 12:30 PM - Rs.4500",
#                 "AKASA AIR - 05:00 PM - Rs.4700"
#             ],
#
#             ("Delhi", "Chennai"): [
#                 "AIR INDIA - 09:15 AM - Rs.6200",
#                 "INDIGO - 02:00 PM - Rs.5800",
#                 "AKASA AIR - 07:00 PM - Rs.6500"
#             ],
#
#             ("Mumbai", "Delhi"): [
#                 "INDIGO - 07:00 AM - Rs.4600",
#                 "AIR INDIA - 01:00 PM - Rs.5100",
#                 "AKASA AIR - 06:30 PM - Rs.4900"
#             ],
#
#             ("Mumbai", "Bengaluru"): [
#                 "AKASA AIR - 08:30 AM - Rs.4200",
#                 "INDIGO - 11:45 AM - Rs.4000",
#                 "AIR INDIA - 08:00 PM - Rs.4500"
#             ],
#
#             ("Chennai", "Kolkata"): [
#                 "INDIGO - 09:30 AM - Rs.5200",
#                 "AIR INDIA - 03:00 PM - Rs.5600",
#                 "AKASA AIR - 07:45 PM - Rs.5400"]}
#
#
#
#         if route not in flight_data:
#             messagebox.showerror(
#                 "No Flights",
#                 "Sorry! No flights available for this route."
#             )
#             flight.destroy()
#             return
#
#
#         Label(flight,
#               text="Available Flights",
#               font=("Segoe UI", 18, "bold"),
#               bg="lightyellow").pack(pady=15)
#
#         selected = StringVar()
#
#         for flight_name in flight_data[route]:
#             Radiobutton(
#                 flight,
#                 text=flight_name,
#                 variable=selected,
#                 value=flight_name,
#                 bg="lightyellow",
#                 font=("Segoe UI",15,"bold")
#             ).pack(pady=10)
#
#
#         def next_page():
#             if not selected.get():
#                 messagebox.showerror(
#                     "Error",
#                     "Please select a flight."
#                 )
#                 return
#
#             flight.destroy()
#             seat_selection(
#                 from_city,
#                 to_city,
#                 journey_date,
#                 passengers,
#                 selected.get()
#             )
#
#         Button(
#             flight,
#             text="Next",
#             command=next_page,
#             bg="green",
#             fg="white"
#         ).pack(pady=20)
#
#
#
#     def seat_selection(from_city,
#                        to_city,
#                        journey_date,
#                        passengers,
#                        selected_flight):
#         seat = Toplevel(root)
#         seat.title("Seat Selection")
#         seat.geometry("900x650")
#         seat.config(bg="lightcyan")
#
#         Label(
#             seat,
#             text="Select Your Seats",
#             font=("Segoe UI", 20, "bold"),
#             bg="lightcyan",
#             fg="navy"
#         ).pack(pady=10)
#
#         seat_vars = []
#
#         seats = [
#             "A1", "A2", "A3", "A4",
#             "B1", "B2", "B3", "B4",
#             "C1", "C2", "C3", "C4",
#             "D1", "D2", "D3", "D4"
#         ]
#
#
#         for i in range(passengers):
#
#             Label(
#                 seat,
#                 text=f"Passenger {i+1}",
#                 font=("Arial", 12, "bold"),
#                 bg="lightcyan"
#             ).pack()
#
#             var = StringVar()
#             seat_vars.append(var)
#
#             frame = Frame(seat, bg="lightcyan")
#             frame.pack()
#
#
#
#             for seat_name in seats:
#                 Radiobutton(
#                     frame,
#                     text=seat_name,
#                     variable=var,
#                     value=seat_name,
#                     bg="lightcyan",
#                     font=("Segoe UI", 12, "bold")
#                 ).pack(side=LEFT, padx=5)
#
#             frame.pack_configure(pady=7)
#
#         def next_page():
#
#             selected = []
#
#             for var in seat_vars:
#
#                 if var.get() == "":
#                     messagebox.showerror(
#                         "Error",
#                         "Select seat for every passenger."
#                     )
#                     return
#
#                 selected.append(var.get())
#
#             # Check duplicate seats
#             if len(selected) != len(set(selected)):
#                 messagebox.showerror(
#                     "Error",
#                     "Seats cannot be repeated."
#                 )
#                 return
#
#             seat.destroy()
#
#             passenger_details(
#                 from_city,
#                 to_city,
#                 journey_date,
#                 passengers,
#                 selected,
#                 selected_flight
#             )
#
#         Button(
#             seat,
#             text="Next",
#             bg="green",
#             fg="white",
#             command=next_page
#         ).pack(pady=20)
#
#
#
#     def passenger_details(
#             from_city,
#             to_city,
#             journey_date,
#             passengers,
#             seats,
#             selected_flight
#     ):
#
#         passenger = Toplevel(root)
#         passenger.title("Passenger Details")
#         passenger.geometry("700x500")
#         passenger.config(bg="white")
#
#         canvas = Canvas(passenger)
#         scrollbar = Scrollbar(
#             passenger,
#             orient="vertical",
#             command=canvas.yview
#         )
#
#         frame = Frame(
#             canvas,
#             width=650,
#             bg="white"
#         )
#
#         canvas.configure(yscrollcommand=scrollbar.set)
#
#         scrollbar.pack(side=RIGHT, fill=Y)
#         canvas.pack(side=LEFT, fill=BOTH, expand=True)
#
#         canvas.create_window(
#             (325, 0),
#             window=frame,
#             anchor="n"
#         )
#
#         frame.bind(
#             "<Configure>",
#             lambda e: canvas.configure(
#                 scrollregion=canvas.bbox("all")
#             )
#         )
#
#         entries = []
#
#         for i in range(passengers):
#             Label(
#                 frame,
#                 text=f"Passenger {i + 1}",
#                 font=("Segoe UI", 15, "bold")
#             ).pack(pady=10)
#
#             Label(frame, text="Name").pack()
#             name = Entry(frame)
#             name.pack()
#
#             Label(frame, text="Age").pack()
#             age = Entry(frame)
#             age.pack()
#
#             Label(frame, text="Gender").pack()
#             gender = Combobox(frame,
#                               values=["Male", "Female", "Other"],
#                               state="readonly",
#                               )
#             gender.pack()
#
#             Label(frame, text=f"Seat : {seats[i]}").pack()
#
#             entries.append((name, age, gender))
#
#         def proceed():
#
#             passenger_list = []
#
#             for name, age, gender in entries:
#
#                 passenger_name = name.get().strip()
#                 passenger_age = age.get().strip()
#                 passenger_gender = gender.get().strip()
#
#                 # Check empty fields
#                 if not passenger_name or not passenger_age or not passenger_gender:
#                     messagebox.showerror(
#                         "Error",
#                         "Fill all passenger details."
#                     )
#                     return
#
#                 # Check name
#                 if not passenger_name.replace(" ", "").isalpha():
#                     messagebox.showerror(
#                         "Error",
#                         "Enter a valid passenger name."
#                     )
#                     return
#
#                 # Check age
#                 if not passenger_age.isdigit() or not (
#                         1 <= int(passenger_age) <= 120
#                 ):
#                     messagebox.showerror(
#                         "Error",
#                         "Enter a valid age."
#                     )
#                     return
#
#                 passenger_list.append({
#                     "name": passenger_name,
#                     "age": passenger_age,
#                     "gender": passenger_gender
#                 })
#
#             passenger.destroy()
#
#             payment_page(
#                 passenger_list,
#                 from_city,
#                 to_city,
#                 journey_date,
#                 passengers,
#                 seats,
#                 selected_flight
#             )
#
#         Button(
#             frame,
#             text="Proceed To Payment",
#             bg="green",
#             fg="white",
#             command=proceed
#         ).pack(pady=20)
#
#
#     def payment_page(
#             passenger_list,
#             from_city,
#             to_city,
#             journey_date,
#             passengers,
#             seats,
#             selected_flight):
#         payment = Toplevel(root)
#         payment.title("Make Payment")
#         payment.geometry("700x500")
#         payment.config(bg="lavender")
#
#         Label(
#             payment,
#             text="MAKE PAYMENT",
#             font=("Segoe UI", 18, "bold"),
#             bg="lavender",
#             fg="purple").pack(pady=15)
#
#         Label(payment,text="Card number",bg="lavender").pack(pady=10)
#         card=Entry(payment,width=30)
#         card.pack(pady=5)
#
#
#         Label(
#             payment,
#             text="Card Holder Name",
#             bg="lavender").pack(pady=10)
#
#         card_holder = Entry(payment, width=30)
#         card_holder.pack(pady=5)
#
#         def restart_booking(ticket):
#             ticket.destroy()
#             open_search()
#
#         def generate_ticket():
#
#             ticket = Toplevel(root)
#             ticket.title("Flight Ticket")
#             ticket.geometry("700x500")
#             ticket.config(bg="white")
#
#             Label(ticket,
#                   text="LAKRA AIRLINES",
#                   font=("Segoe UI",15,"bold"),
#                   fg="darkgreen",
#                   bg="white").pack(pady=5)
#
#             Label(ticket,
#                   text="BOARDING PASS",
#                   font=("Segoe UI", 22, "bold"),
#                   bg="white",
#                   fg="NAVY").pack(pady=15)
#             Label(
#                 ticket,
#                 text=f"Flight: {selected_flight}",
#                 font=("Segoe UI", 11, "bold"),
#                 bg="white"
#             ).pack(pady=5)
#             Label(ticket,
#                   text=f"From : {from_city}",
#                   font=("Segoe UI", 12),
#                   bg="white").pack()
#
#             Label(ticket,
#                   text=f"To : {to_city}",
#                   font=("Segoe UI", 12)).pack()
#
#             Label(ticket,
#                   text=f"Journey Date : {journey_date}",
#                   font=("Segoe UI", 12),
#                   bg="white").pack()
#
#             Label(ticket,
#                   text="Payment Status : PAID",
#                   fg="green",
#                   bg="white",
#                   font=("Segoe UI", 12, "bold")).pack(pady=10)
#             save_ticket_to_file(
#                 passenger_list,
#                 from_city,
#                 to_city,
#                 journey_date,
#                 selected_flight,
#                 seats
#             )
#
#             for i in range(passengers):
#                 passenger=passenger_list[i]
#
#                 Label(
#                     ticket,
#                     text=(f"{i + 1}. {passenger_list[i]['name']}    "
#                          f"Seat: {seats[i]}"),
#                     font=("Segoe UI", 12),
#                     bg="white"
#                 ).pack(pady=3)
#
#                 booking_history.append(
#                     f"{passenger['name']} | "
#                     f"{from_city} -> {to_city} | "
#                     f"{journey_date} | "
#                     f"{selected_flight} | "
#                     f"Seat {seats[i]}"
#                 )
#
#             Button(
#                 ticket,
#                 text="Book Another Ticket",
#                 bg="#00A8E8",
#                 fg="white",
#                 font=("Segoe UI", 11, "bold"),
#                 command=lambda: restart_booking(ticket)
#             ).pack(pady=10)
#
#             Button(
#                 ticket,
#                 text="Close",
#                 bg="#E63946",
#                 fg="white",
#                 font=("Segoe UI", 11, "bold"),
#                 command=ticket.destroy
#             ).pack(pady=5)
#
#         def save_ticket_to_file(
#                 passenger_list,
#                 from_city,
#                 to_city,
#                 journey_date,
#                 selected_flight,
#                 seats
#         ):
#             with open("booking_history.txt", "a", encoding="utf-8") as file:
#                 file.write("\n")
#                 file.write("=" * 70 + "\n")
#                 file.write("              LAKRA AIRLINES\n")
#                 file.write("                BOARDING PASS\n")
#                 file.write("=" * 70 + "\n")
#
#                 file.write(f"From       : {from_city}\n")
#                 file.write(f"To         : {to_city}\n")
#                 file.write(f"Date       : {journey_date}\n")
#                 file.write(f"Flight     : {selected_flight}\n")
#                 file.write("Payment    : PAID\n")
#
#                 file.write("-" * 70 + "\n")
#
#                 for i, passenger in enumerate(passenger_list):
#                     file.write(
#                         f"Passenger {i + 1}\n"
#                         f"Name       : {passenger['name']}\n"
#                         f"Age        : {passenger['age']}\n"
#                         f"Gender     : {passenger['gender']}\n"
#                         f"Seat       : {seats[i]}\n"
#                     )
#                     file.write("-" * 70 + "\n")
#
#                 file.write("=" * 70 + "\n")
#
#         def pay():
#             card_number = card.get().strip()
#             holder_name = card_holder.get().strip()
#
#             if not card_number or not holder_name:
#                 messagebox.showerror(
#                     "Error",
#                     "Fill all payment details."
#                 )
#                 return
#
#             if len(card_number) != 16 or not card_number.isdigit():
#                 messagebox.showerror(
#                     "Error",
#                     "Enter a valid 16-digit card number."
#                 )
#                 return
#
#             if not holder_name.replace(" ", "").isalpha():
#                 messagebox.showerror(
#                     "Error",
#                     "Enter a valid card holder name."
#                 )
#                 return
#
#             payment.destroy()
#             generate_ticket()
#
#         Button(payment,
#                 text="Pay Now",
#                 bg="green",
#                 fg="white",
#                 command=pay).pack(pady=20)
#
#
#     Button(search,
#            text="Search Flights",
#            command=search_flight,
#            bg="green",
#            fg="white").pack(pady=20)
#
# def view_file_history():
#     try:
#         with open("booking_history.txt", "r", encoding="utf-8") as file:
#             history = file.read()
#
#         if not history.strip():
#             messagebox.showinfo(
#                 "History",
#                 "No booking history available."
#             )
#             return
#
#         history_window = Toplevel(root)
#         history_window.title("File Booking History")
#         history_window.geometry("850x600")
#         history_window.config(bg="#081A2B")
#
#         Label(
#             history_window,
#             text="BOOKING HISTORY",
#             font=("Segoe UI", 22, "bold"),
#             bg="#081A2B",
#             fg="#FFD166"
#         ).pack(pady=15)
#
#         text_box = Text(
#             history_window,
#             width=95,
#             height=30,
#             font=("Consolas", 10),
#             bg="white",
#             fg="#16324F"
#         )
#         text_box.pack(
#             padx=20,
#             pady=10,
#             fill=BOTH,
#             expand=True
#         )
#
#         text_box.insert("1.0", history)
#         text_box.config(state=DISABLED)
#
#     except FileNotFoundError:
#         messagebox.showinfo(
#             "History",
#             "No booking history file found."
#         )
#
# def view_history():
#     history=Toplevel(root)
#     history.title("Booking History")
#     history.geometry("700x500")
#     history.config(bg="light blue")
#
#     if booking_history:
#         for booking in booking_history:
#             Label(history,text=booking,
#                   bg="light blue",
#                   font=("Segoe UI",12,"bold"),
#                   wraplength=750).pack(pady=5)
#     else:
#         Label(history,
#               text="No Booking Available",
#               bg="light blue",
#               font=("Segoe UI",12,"bold")).pack(pady=20)
#
# button_frame=Frame(root,bg="#0B1F3A")
# button_frame.pack(pady=40)
#
# Button(button_frame,
#        text="Search Flights",
#        command=open_search,
#        font=("Segoe UI",15,"bold"),
#        width=20,
#        height=2,
#        relief="flat",
#        cursor="hand2",
#        bg="#00A8E8",
#        fg="white").pack(pady=13)
#
# Button(
#     button_frame,
#     text="View History",
#     command=view_history,
#     width=20,
#     height=2,
#     relief="flat",
#     cursor="hand2",
#     bg="#E63946",
#     fg="white"
# ).pack(pady=13)
#
# Button(button_frame,
#        text="Exit",
#        command=root.destroy,
#        width=20,
#        height=2,
#        relief="flat",
#        cursor="hand2",
#        bg="#28A745",
#        fg="white").pack(pady=13)
# root.mainloop()