from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import DateEntry

root = Tk()
root.title("Airline Ticket Booking System")
root.geometry("700x500")
root.config(bg="#87CEEB")

Label(root, text="AIRLINE TICKET BOOKING SYSTEM",
      font=("Helvetica", 20, "bold"),
      bg="#87CEEB",
      fg="dark blue").pack(pady=20)
Label(root,text="Book Your Dream Journey",
      font=("Arial",14,"italic"),
      bg="#87CEEB",
      fg="darkgreen").pack()


def open_search():
    search = Toplevel(root)
    search.title("Search Flights")
    search.geometry("500x400")
    search.config(bg="lightcyan")

    Label(search, text="Search Flights",
          font=("Helveyica", 20, "bold"),
          bg="lightcyan",
          fg="navy").pack(pady=15)

    Label(search, text="From").pack()
    from_entry = Combobox(search,
                       values=["Delhi","Mumbai","Bengaluru","Chennai","Kolkata"],
                       width=25)
    from_entry.pack()

    Label(search, text="To").pack()
    to_entry = Combobox(search,
                     values=["Delhi", "Mumbai", "Bengaluru", "Chennai", "Kolkata"],
                     width=25)
    to_entry.pack()

    Label(search, text="Journey Date").pack()


    date_entry = DateEntry(
        search,
        width=27,
        background="darkblue",
        foreground="white",
        borderwidth=2,
        date_pattern="dd-mm-yyyy"
    )
    date_entry.pack(pady=5)

    Label(search, text="Passengers").pack()
    passenger_entry = Entry(search, width=30)
    passenger_entry.pack()

    def search_flight():
        if (from_entry.get() == "" or to_entry.get() == "" or
                date_entry.get() == "" or passenger_entry.get() == ""):
            messagebox.showerror("Error", "Please fill all fields")
        else:
            select_flights()

    def select_flights():
        flight=Toplevel()
        flight.title("Select Flights")
        flight.geometry("500x400")
        flight.config(bg="lightyellow")

        Label(flight,text="Available Flights",
              font=("Arial",18,"bold"),
              bg="lightyellow").pack(pady=15)

        selected=StringVar()
        Radiobutton(flight,text="AIR INDIA 10:00 AM  Rs.5000",
                    variable=selected,
                    value="AIR INDIA").pack(anchor="w",padx=40)
        Radiobutton(flight,text="INDIGO 12:30 PM  RS.4500",
                    variable=selected,
                    value="INDIGO").pack(anchor="w",padx=40)
        Radiobutton(flight,text="AKASA AIR  4:00 PM  Rs.4700",
                    variable=selected,
                    value="AKASHA AIR").pack(anchor="w",padx=40)
        Button(flight,text="Next",
               bg="green",
               fg="white",
               command=seat_selection).pack(pady=20)

    def seat_selection():
        seat=Toplevel(root)
        seat.title("Seat Selection")
        seat.geometry("500x450")
        seat.config(bg="lightcyan")

        Label(seat,text="Choose Your Seat",
              font=("Arial",18,"bold"),
              bg="lightcyan").pack(pady=15)

        seat_no=StringVar()
        seats=["A1","A2","A3",
               "B1","B2","B3",
               "C1","C2","C3",
               "D1","D2","D3"]
        row=0
        col=0
        for s in seats:
            Radiobutton(seat,text=s,
                        variable=seat_no,
                        value=s,
                        bg="lightcyan",
                        font=("Arial",11)).place(x=80+col*90,y=70+row*40)
            col+=1
            if col==3:
                col=0
                row+=1

            Button(seat,text="Continue",
                   bg="green",
                   fg="white",
                   font=("Arial",12,"bold"),
                   command=passenger_details).place(x=190,y=280)

    def passenger_details():
        passenger=Toplevel(root)
        passenger.title("Passenger Details")
        passenger.geometry("450x450")
        passenger.config(bg="lavender")

        Label(passenger,text="Passenger Details",
              font=("Arial",18,"bold"),
              bg="lavender").pack(pady=15)
        Label(passenger,text="Passenger Name",
              font=("Arial",18),
              bg="lavender",
              width=30).pack()
        Label(passenger,text="Age",
              bg="lavender").pack()
        Entry(passenger,width=30).pack()
        Label(passenger,text="Gender",
              bg="lavender").pack()
        from  tkinter import ttk
        gender=ttk.Combobox(passenger,
                        values=["Male","Female","Other"],
                        width=27)
        gender.pack()

        Label(passenger,text="Mobile Number",
              bg="lavender").pack()
        Entry(passenger,width=30).pack()
        Button(passenger,text="Proceed To Payment",
               bg="green",
               fg="white",
               command=payment_page).pack(pady=20)

    def payment_page():
        payment = Toplevel(root)
        payment.title("Make Payment")
        payment.geometry("400x350")
        payment.config(bg="lavender")

        Label(payment, text="MAKE PAYMENT",
            font=("Helvetica", 18, "bold"),
              bg="lavender",
              fg="purple").pack(pady=15)

        Label(payment, text="Amount: ₹5000",
            font=("Arial", 14)).pack(pady=10)

        Label(payment, text="Card Number").pack(pady=10)
        card = Entry(payment, width=30)
        card.pack(pady=10)

        Label(payment, text="Card Holder Name").pack(pady=10)
        name = Entry(payment, width=30)
        name.pack(pady=10)


        def pay():
            if card.get() == "" or name.get() == "" :
                messagebox.showerror("Error", "Fill all details")
            else:
                messagebox.showinfo("Success", "Payment Successful!")
                generate_ticket()
                payment.destroy()

        def generate_ticket():

            ticket = Toplevel(root)
            ticket.title("Flight Ticket")
            ticket.geometry("500x400")
            ticket.config(bg="white")

            Label(ticket,
                  text="AIRLINE TICKET",
                  font=("Helvetica", 20, "bold"),
                  bg="white",
                  fg="darkgreen").pack(pady=15)

            Label(ticket,
                  text="Passenger Name : " + name.get(),
                  font=("Arial", 12)).pack(pady=5)

            Label(ticket,
                  text="From : " + from_entry.get(),
                  font=("Arial", 12)).pack(pady=5)

            Label(ticket,
                  text="To : " + to_entry.get(),
                  font=("Arial", 12)).pack(pady=5)

            Label(ticket,
                  text="Journey Date : " + date_entry.get(),
                  font=("Arial", 12)).pack(pady=5)

            Label(ticket,
                  text="Passengers : " + passenger_entry.get(),
                  font=("Arial", 12)).pack(pady=5)

            Label(ticket,
                  text="Payment Status : PAID",
                  fg="green",
                  font=("Arial", 12, "bold")).pack(pady=10)
            Label(ticket,text="Have A Safe Journey!",
                  font=("Arial",14,"bold"),
                  fg="blue",
                  bg="white").pack(pady=10)

            Button(ticket,
                   text="Close",
                   command=ticket.destroy).pack(pady=15)

        Button(payment,
                text="Pay Now",
                bg="green",
                fg="white",
                command=pay).pack(pady=20)


    Button(search,
           text="Search Flights",
           command=search_flight,
           bg="green",
           fg="white").pack(pady=20)

def view_history():
    history=Toplevel(root)
    history.title("Booking History")
    history.geometry("400x200")
    history.config(bg="light blue")

    Label(history,text="Booking History",
          font=("Arial",18,"bold"),
          bg="light blue",
          fg="navy").pack(pady=15)
    Label(history,text="NO Booking available",
          font=("Arial",18),
          bg="light blue").pack(pady=20)


Button(root,
       text="Search Flights",
       command=open_search,
       font=("Arial",13,"bold"),
       width=20,
       bg="#28a745",
       fg="white").pack(pady=10)

Button(root,
       text="View History",
       width=20,
       font=("Arial",13,"bold"),
       bg="#007bff",
       fg="white",
       command=view_history).pack(pady=10)

Button(root,
       text="Exit",
       command=root.destroy,
       font=("Arial",13,"bold"),
       width=20,
       bg="#dc3545",
       fg="white").pack(pady=10)

root.mainloop()