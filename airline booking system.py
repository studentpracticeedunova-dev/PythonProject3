from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
import mysql.connector
import smtplib
from email.message import EmailMessage
import random

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root@123"
MYSQL_DATABASE = "airline_booking"

BG = "#071A2B"
CARD = "#0D2B45"
CARD2 = "#123A59"
BLUE = "#00A8E8"
BLUE2 = "#0077B6"
WHITE = "#FFFFFF"
TEXT = "#DDEAF2"
GOLD = "#FFD166"
GREEN = "#2EC4B6"
RED = "#E63946"
LIGHT = "#F4F8FB"
DARK_TEXT = "#16324F"


booking_history = []

def setup_database():

    try:

        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )

        cursor = connection.cursor()

        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE}"
        )

        cursor.close()
        connection.close()

        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (

                booking_id INT AUTO_INCREMENT PRIMARY KEY,

                passenger_name VARCHAR(100) NOT NULL,

                age INT NOT NULL,

                age_group VARCHAR(20) NOT NULL,

                gender VARCHAR(20) NOT NULL,

                travel_class VARCHAR(30) NOT NULL,

                from_city VARCHAR(50) NOT NULL,

                to_city VARCHAR(50) NOT NULL,

                journey_date VARCHAR(20) NOT NULL,

                flight VARCHAR(150) NOT NULL,

                seat VARCHAR(10) NOT NULL,

                payment_status VARCHAR(20)
                DEFAULT 'PAID',

                booking_date TIMESTAMP
                DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.commit()

        cursor.execute("SHOW COLUMNS FROM bookings")
        columns = [row[0] for row in cursor.fetchall()]

        if "age_group" not in columns:

            cursor.execute("""
                ALTER TABLE bookings
                ADD COLUMN age_group VARCHAR(20)
                AFTER age
            """)

        if "travel_class" not in columns:

            cursor.execute("""
                ALTER TABLE bookings
                ADD COLUMN travel_class VARCHAR(30)
                AFTER gender
            """)

        connection.commit()

        cursor.close()
        connection.close()

        return True

    except mysql.connector.Error as error:

        messagebox.showerror(
            "Database Error",
            f"Could not setup MySQL database.\n\n{error}"
        )

        return False

def connect_database():

    try:

        return mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )

    except mysql.connector.Error as error:

        messagebox.showerror(
            "Database Error",
            f"Could not connect to MySQL.\n\n{error}"
        )

        return None

def save_booking_to_database(
    passenger_list,
    from_city,
    to_city,
    journey_date,
    selected_flight,
    seats
):

    connection = connect_database()

    if connection is None:
        return False

    cursor = None

    try:

        cursor = connection.cursor()

        query = """
            INSERT INTO bookings
            (
                passenger_name,
                age,
                age_group,
                gender,
                travel_class,
                from_city,
                to_city,
                journey_date,
                flight,
                seat,
                payment_status
            )
            VALUES
            (
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s
            )
        """

        for i, passenger in enumerate(passenger_list):

            values = (
                passenger["name"],
                int(passenger["age"]),
                passenger["age_group"],
                passenger["gender"],
                passenger["travel_class"],
                from_city,
                to_city,
                journey_date,
                selected_flight,
                seats[i],
                "PAID"
            )

            cursor.execute(query, values)

        connection.commit()

        return True

    except mysql.connector.Error as error:

        connection.rollback()

        messagebox.showerror(
            "Database Error",
            f"Booking could not be saved.\n\n{error}"
        )

        return False

    finally:

        if cursor:
            cursor.close()

        connection.close()

sender_email="development.edunova@gmail.com"
app_password="yfmq aamr widr zfzu"



class OTPVerificationApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Lakra Airlines | OTP Verification")
        self.root.geometry("700x630")
        self.root.config(bg=BG)



        self.otp = None
        self.email = None

        Label(
            root,
            text="✈  LAKRA AIRLINES",
            font=("Segoe UI", 25, "bold"),
            bg=BG,
            fg=WHITE
        ).pack(pady=(35, 5))

        Label(
            root,
            text="Secure Email Verification",
            font=("Segoe UI", 12),
            bg=BG,
            fg=TEXT
        ).pack()

        card = Frame(
            root,
            bg=CARD,
            highlightbackground="#1B4D6D",
            highlightthickness=1
        )

        card.pack(
            padx=50,
            pady=30,
            fill=BOTH,
            expand=True
        )

        Label(
            card,
            text="Verify Your Email",
            font=("Segoe UI", 18, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(pady=(25, 8))

        Label(
            card,
            text="Enter your email to receive a verification OTP",
            font=("Segoe UI", 10),
            bg=CARD,
            fg=TEXT
        ).pack(pady=(0, 18))

        self.entry_email = Entry(
            card,
            font=("Segoe UI", 12),
            width=35,
            bd=0,
            relief="flat"
        )

        self.entry_email.pack(
            ipady=8,
            pady=5
        )

        Button(
            card,
            text="SEND OTP",
            command=self.send_otp,
            font=("Segoe UI", 11, "bold"),
            width=25,
            height=2,
            bg=BLUE,
            fg=WHITE,
            activebackground=BLUE2,
            activeforeground=WHITE,
            relief="flat",
            cursor="hand2"
        ).pack(pady=15)


        self.entry_otp = Entry(
            card,
            font=("Segoe UI", 12),
            width=20,
            justify="center",
            bd=0,
            relief="flat"
        )

        self.entry_otp.pack(
            ipady=8,
            pady=5
        )


        Button(
            card,
            text="VERIFY OTP",
            command=self.verify_otp,
            font=("Segoe UI", 11, "bold"),
            width=25,
            height=2,
            bg=GREEN,
            fg=WHITE,
            activebackground="#239E91",
            activeforeground=WHITE,
            relief="flat",
            cursor="hand2"
        ).pack(pady=15)

    def send_otp(self):

        email = self.entry_email.get().strip()

        if not email:

            messagebox.showerror(
                "Missing Email",
                "Please enter your email address.",
                parent=self.root
            )

            return

        if "@" not in email or "." not in email:

            messagebox.showerror(
                "Invalid Email",
                "Please enter a valid email address.",
                parent=self.root
            )

            return

        self.email = email

        self.otp = str(
            random.randint(100000, 999999)
        )

        try:

            msg = EmailMessage()

            msg["Subject"] = "Lakra Airlines - OTP Verification"
            msg["From"] = sender_email
            msg["To"] = email

            msg.set_content(
                f"""
Hello,

Your Lakra Airlines verification OTP is:

{self.otp}

Please enter this OTP in the application.

Do not share this OTP with anyone.

Regards,
Lakra Airlines
"""
            )

            with smtplib.SMTP_SSL(
                "smtp.gmail.com",
                465
            ) as server:

                server.login(
                    sender_email,
                    app_password
                )

                server.send_message(msg)

            messagebox.showinfo(
                "OTP Sent",
                f"OTP has been sent to:\n{email}",
                parent=self.root
            )

        except Exception as error:

            messagebox.showerror(
                "Email Error",
                f"Could not send OTP.\n\n{error}",
                parent=self.root
            )

    def verify_otp(self):

        entered_otp = self.entry_otp.get().strip()

        if not self.otp:

            messagebox.showwarning(
                "OTP Required",
                "Please click SEND OTP first.",
                parent=self.root
            )

            return

        if not entered_otp:

            messagebox.showwarning(
                "OTP Required",
                "Please enter the OTP.",
                parent=self.root
            )

            return

        if entered_otp == self.otp:
            messagebox.showinfo(
                "Verification Successful",
                "Email verified successfully!",
                parent=self.root
            )

            self.root.destroy()

            root.deiconify()

def style_button(parent, text, command, bg=BLUE, width=20):

    button = Button(
        parent,
        text=text,
        command=command,
        font=("Segoe UI", 12, "bold"),
        width=width,
        height=2,
        bg=bg,
        fg=WHITE,
        activebackground=BLUE2,
        activeforeground=WHITE,
        relief="flat",
        bd=0,
        cursor="hand2"
    )

    def on_enter(event):
        button.config(bg=BLUE2)

    def on_leave(event):
        button.config(bg=bg)

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    return button

def view_history():

    connection = connect_database()

    if connection is None:
        return

    cursor = None

    try:

        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                booking_id,
                passenger_name,
                age,
                age_group,
                gender,
                travel_class,
                from_city,
                to_city,
                journey_date,
                flight,
                seat,
                payment_status,
                booking_date
            FROM bookings
            ORDER BY booking_id DESC
        """)

        records = cursor.fetchall()

    except mysql.connector.Error as error:

        messagebox.showerror(
            "Database Error",
            f"Could not load booking history.\n\n{error}"
        )

        return

    finally:

        if cursor:
            cursor.close()

        connection.close()

    history = Toplevel(root)

    history.title("Lakra Airlines | Booking History")
    history.geometry("1450x700")
    history.config(bg=BG)

    header = Frame(
        history,
        bg=BG,
        height=120
    )

    header.pack(fill=X)
    header.pack_propagate(False)

    Label(
        header,
        text="▤  BOOKING HISTORY",
        font=("Segoe UI", 26, "bold"),
        bg=BG,
        fg=WHITE
    ).pack(pady=(20, 3))

    Label(
        header,
        text="All bookings stored in MySQL database",
        font=("Segoe UI", 11),
        bg=BG,
        fg=TEXT
    ).pack()

    if not records:

        Label(
            history,
            text="✈",
            font=("Segoe UI", 50),
            bg=BG,
            fg=BLUE
        ).pack(pady=(90, 10))

        Label(
            history,
            text="No Booking Available",
            font=("Segoe UI", 17, "bold"),
            bg=BG,
            fg=WHITE
        ).pack()

        return

    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "Lakra.Treeview",
        background=CARD,
        foreground=WHITE,
        fieldbackground=CARD,
        rowheight=40,
        font=("Segoe UI", 10)
    )

    style.configure(
        "Lakra.Treeview.Heading",
        background=CARD2,
        foreground=GOLD,
        font=("Segoe UI", 10, "bold"),
        padding=10
    )

    style.map(
        "Lakra.Treeview",
        background=[("selected", BLUE)],
        foreground=[("selected", WHITE)]
    )

    table_card = Frame(
        history,
        bg=CARD,
        highlightbackground="#1B4D6D",
        highlightthickness=1
    )

    table_card.pack(
        fill=BOTH,
        expand=True,
        padx=25,
        pady=20
    )

    columns = (
        "ID",
        "Passenger",
        "Age",
        "Age Group",
        "Gender",
        "Class",
        "From",
        "To",
        "Journey Date",
        "Flight",
        "Seat",
        "Payment",
        "Booking Date"
    )

    tree = ttk.Treeview(
        table_card,
        columns=columns,
        show="headings",
        style="Lakra.Treeview"
    )

    for column in columns:

        tree.heading(
            column,
            text=column
        )

    widths = {
        "ID": 50,
        "Passenger": 140,
        "Age": 60,
        "Age Group": 100,
        "Gender": 80,
        "Class": 120,
        "From": 90,
        "To": 90,
        "Journey Date": 110,
        "Flight": 250,
        "Seat": 60,
        "Payment": 90,
        "Booking Date": 150
    }

    for column, width in widths.items():

        tree.column(
            column,
            width=width,
            minwidth=50
        )

    vertical_scroll = Scrollbar(
        table_card,
        orient=VERTICAL,
        command=tree.yview
    )

    horizontal_scroll = Scrollbar(
        table_card,
        orient=HORIZONTAL,
        command=tree.xview
    )

    tree.configure(
        yscrollcommand=vertical_scroll.set,
        xscrollcommand=horizontal_scroll.set
    )

    vertical_scroll.pack(
        side=RIGHT,
        fill=Y
    )

    horizontal_scroll.pack(
        side=BOTTOM,
        fill=X
    )

    tree.pack(
        side=LEFT,
        fill=BOTH,
        expand=True
    )

    for record in records:

        tree.insert(
            "",
            END,
            values=record
        )

    style_button(
        history,
        "CLOSE",
        history.destroy,
        RED,
        15
    ).pack(pady=(0, 15))




def open_search():

    search = Toplevel(root)

    search.title("Lakra Airlines | Search Flights")
    search.geometry("750x620")
    search.config(bg=BG)
    search.resizable(False, False)

    header = Frame(
        search,
        bg=BG,
        height=100
    )

    header.pack(fill=X)
    header.pack_propagate(False)

    Label(
        header,
        text="✈  SEARCH FLIGHTS",
        font=("Segoe UI", 23, "bold"),
        bg=BG,
        fg=WHITE
    ).pack(pady=(18, 2))

    Label(
        header,
        text="Find the perfect flight for your journey",
        font=("Segoe UI", 10),
        bg=BG,
        fg=TEXT
    ).pack()

    card = Frame(
        search,
        bg=CARD,
        highlightbackground="#D5E2EA",
        highlightthickness=1
    )

    card.pack(
        padx=45,
        pady=30,
        fill=BOTH,
        expand=True
    )

    Label(
        card,
        text="Journey Details",
        font=("Segoe UI", 18, "bold"),
        bg=CARD,
        fg=WHITE
    ).pack(pady=(25, 20))

    # FROM

    Label(
        card,
        text="FROM",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg="#637381"
    ).pack()

    from_entry = Combobox(
        card,
        values=[
            "Delhi",
            "Mumbai",
            "Bengaluru",
            "Chennai",
            "Kolkata"
        ],
        width=35,
        state="readonly",
        font=("Segoe UI", 11)
    )

    from_entry.pack(pady=(5, 15))

    # TO

    Label(
        card,
        text="TO",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg="#637381"
    ).pack()

    to_entry = Combobox(
        card,
        values=[
            "Delhi",
            "Mumbai",
            "Bengaluru",
            "Chennai",
            "Kolkata"
        ],
        width=35,
        state="readonly",
        font=("Segoe UI", 11)
    )

    to_entry.pack(pady=(5, 15))

    Label(
        card,
        text="JOURNEY DATE",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg="#637381"
    ).pack()

    date_entry = DateEntry(
        card,
        width=33,
        borderwidth=2,
        date_pattern="dd-mm-yyyy",
        font=("Segoe UI", 11)
    )

    date_entry.pack(pady=(5, 15))

    Label(
        card,
        text="PASSENGERS",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg="#637381"
    ).pack()

    passenger_entry = Entry(
        card,
        width=37,
        font=("Segoe UI", 11),
        bd=1,
        relief="solid"
    )

    passenger_entry.pack(pady=(5, 20))

    def search_flight():

        from_city = from_entry.get()
        to_city = to_entry.get()
        journey_date = date_entry.get()
        passenger_text = passenger_entry.get().strip()

        if not from_city or not to_city:

            messagebox.showerror(
                "Missing Information",
                "Please select From and To cities.",
                parent=search
            )

            return

        if from_city == to_city:

            messagebox.showerror(
                "Invalid Route",
                "From and To cities cannot be the same.",
                parent=search
            )

            return

        if (
            not passenger_text.isdigit()
            or int(passenger_text) <= 0
        ):

            messagebox.showerror(
                "Invalid Passengers",
                "Enter a valid number of passengers.",
                parent=search
            )

            return

        passengers = int(passenger_text)

        if passengers > 10:

            messagebox.showerror(
                "Passenger Limit",
                "Maximum 10 passengers are allowed.",
                parent=search
            )

            return

        search.destroy()

        select_flights(
            from_city,
            to_city,
            journey_date,
            passengers
        )

    style_button(
        card,
        "SEARCH FLIGHTS  →",
        search_flight,
        BLUE,
        25
    ).pack(pady=10)

def select_flights(
    from_city,
    to_city,
    journey_date,
    passengers
):

    flight = Toplevel(root)

    flight.title("Lakra Airlines | Select Flight")
    flight.geometry("850x650")
    flight.config(bg=BG)
    flight.resizable(False, False)

    header = Frame(
        flight,
        bg=BG,
        height=110
    )

    header.pack(fill=X)
    header.pack_propagate(False)

    Label(
        header,
        text="AVAILABLE FLIGHTS",
        font=("Segoe UI", 24, "bold"),
        bg=BG,
        fg=WHITE
    ).pack(pady=(18, 2))

    Label(
        header,
        text=f"{from_city}  ✈  {to_city}   |   {journey_date}",
        font=("Segoe UI", 11),
        bg=BG,
        fg=GOLD
    ).pack()

    flight_data = {

        ("Delhi", "Mumbai"): [
            "AIR INDIA - 08:00 AM - Rs.5000",
            "INDIGO - 12:30 PM - Rs.4500",
            "AKASA AIR - 05:00 PM - Rs.4700"
        ],

        ("Delhi", "Chennai"): [
            "AIR INDIA - 09:15 AM - Rs.6200",
            "INDIGO - 02:00 PM - Rs.5800",
            "AKASA AIR - 07:00 PM - Rs.6500"
        ],

        ("Mumbai", "Delhi"): [
            "INDIGO - 07:00 AM - Rs.4600",
            "AIR INDIA - 01:00 PM - Rs.5100",
            "AKASA AIR - 06:30 PM - Rs.4900"
        ],

        ("Mumbai", "Bengaluru"): [
            "AKASA AIR - 08:30 AM - Rs.4200",
            "INDIGO - 11:45 AM - Rs.4000",
            "AIR INDIA - 08:00 PM - Rs.4500"
        ],

        ("Chennai", "Kolkata"): [
            "INDIGO - 09:30 AM - Rs.5200",
            "AIR INDIA - 03:00 PM - Rs.5600",
            "AKASA AIR - 07:45 PM - Rs.5400"
        ],

        ("Delhi", "Bengaluru"): [
            "INDIGO - 08:00 AM - Rs.5500",
            "AIR INDIA - 01:30 PM - Rs.5800",
            "AKASA AIR - 07:00 PM - Rs.5300"
        ],

        ("Delhi", "Kolkata"): [
            "INDIGO - 09:00 AM - Rs.4800",
            "AIR INDIA - 02:30 PM - Rs.5100",
            "AKASA AIR - 08:00 PM - Rs.4900"
        ],

        ("Mumbai", "Chennai"): [
            "INDIGO - 07:30 AM - Rs.5000",
            "AIR INDIA - 01:00 PM - Rs.5400",
            "AKASA AIR - 06:00 PM - Rs.4800"
        ],

        ("Bengaluru", "Mumbai"): [
            "INDIGO - 08:30 AM - Rs.4100",
            "AIR INDIA - 02:00 PM - Rs.4500",
            "AKASA AIR - 07:00 PM - Rs.4300"
        ],

        ("Bengaluru", "Delhi"): [
            "INDIGO - 06:30 AM - Rs.5200",
            "AIR INDIA - 12:00 PM - Rs.5600",
            "AKASA AIR - 06:30 PM - Rs.5000"
        ]
    }

    route = (from_city, to_city)

    if route not in flight_data:

        messagebox.showerror(
            "No Flights",
            "Sorry! No flights available for this route.",
            parent=flight
        )

        flight.destroy()
        return

    selected = StringVar()

    container = Frame(
        flight,
        bg=LIGHT
    )

    container.pack(
        fill=BOTH,
        expand=True,
        padx=40,
        pady=20
    )

    for flight_name in flight_data[route]:

        card = Frame(
            container,
            bg=WHITE,
            highlightbackground="#D5E2EA",
            highlightthickness=1
        )

        card.pack(
            fill=X,
            pady=8
        )

        Radiobutton(
            card,
            text="✈",
            variable=selected,
            value=flight_name,
            bg=WHITE,
            activebackground=WHITE,
            fg=BLUE,
            font=("Segoe UI", 20)
        ).pack(
            side=LEFT,
            padx=15
        )

        Label(
            card,
            text=flight_name,
            font=("Segoe UI", 13, "bold"),
            bg=WHITE,
            fg=DARK_TEXT
        ).pack(
            side=LEFT,
            pady=18
        )

    def next_page():

        if not selected.get():

            messagebox.showerror(
                "Flight Required",
                "Please select a flight.",
                parent=flight
            )

            return

        selected_flight = selected.get()

        flight.destroy()

        seat_selection(
            from_city,
            to_city,
            journey_date,
            passengers,
            selected_flight
        )

    style_button(
        flight,
        "CONTINUE TO SEAT SELECTION  →",
        next_page,
        BLUE,
        30
    ).pack(pady=15)

def seat_selection(
    from_city,
    to_city,
    journey_date,
    passengers,
    selected_flight
):

    seat_window = Toplevel(root)

    seat_window.title("Lakra Airlines | Seat Selection")
    seat_window.geometry("750x650")
    seat_window.config(bg=BG)
    seat_window.resizable(False, False)

    header = Frame(
        seat_window,
        bg=BG,
        height=120
    )

    header.pack(fill=X)
    header.pack_propagate(False)

    Label(
        header,
        text="✈  SELECT YOUR SEATS",
        font=("Segoe UI", 25, "bold"),
        bg=BG,
        fg=WHITE
    ).pack(pady=(20, 3))

    Label(
        header,
        text="Choose one seat for each passenger",
        font=("Segoe UI", 11),
        bg=BG,
        fg=TEXT
    ).pack()

    card = Frame(
        seat_window,
        bg=CARD,
        highlightbackground="#1B4D6D",
        highlightthickness=1
    )

    card.pack(
        padx=70,
        pady=30,
        fill=BOTH,
        expand=True
    )

    Label(
        card,
        text=f"{from_city}  ✈  {to_city}",
        font=("Segoe UI", 18, "bold"),
        bg=CARD,
        fg=WHITE
    ).pack(pady=(25, 3))

    Label(
        card,
        text=f"{journey_date}   |   {selected_flight}",
        font=("Segoe UI", 10),
        bg=CARD,
        fg=GOLD
    ).pack(pady=(0, 20))

    seats = [
        "A1", "A2", "A3", "A4",
        "B1", "B2", "B3", "B4",
        "C1", "C2", "C3", "C4",
        "D1", "D2", "D3", "D4"
    ]

    seat_vars = []

    for i in range(passengers):

        passenger_frame = Frame(
            card,
            bg=CARD2
        )

        passenger_frame.pack(
            fill=X,
            padx=35,
            pady=8
        )

        Label(
            passenger_frame,
            text=f"Passenger {i + 1}",
            font=("Segoe UI", 12, "bold"),
            bg=CARD2,
            fg=WHITE
        ).pack(
            side=LEFT,
            padx=15,
            pady=12
        )

        var = StringVar()
        seat_vars.append(var)

        Combobox(
            passenger_frame,
            textvariable=var,
            values=seats,
            state="readonly",
            width=15,
            font=("Segoe UI", 11)
        ).pack(
            side=RIGHT,
            padx=15,
            pady=8
        )

    def next_page():

        selected_seats = []

        for var in seat_vars:

            if not var.get():

                messagebox.showerror(
                    "Seat Required",
                    "Please select a seat for every passenger.",
                    parent=seat_window
                )

                return

            selected_seats.append(var.get())

        if len(selected_seats) != len(set(selected_seats)):

            messagebox.showerror(
                "Duplicate Seat",
                "One seat cannot be assigned to multiple passengers.",
                parent=seat_window
            )

            return

        seat_window.destroy()

        passenger_details(
            from_city,
            to_city,
            journey_date,
            passengers,
            selected_seats,
            selected_flight
        )

    style_button(
        card,
        "CONTINUE  →",
        next_page,
        BLUE,
        20
    ).pack(pady=20)

def passenger_details(
    from_city,
    to_city,
    journey_date,
    passengers,
    seats,
    selected_flight
):

    passenger_window = Toplevel(root)

    passenger_window.title(
        "Lakra Airlines | Passenger Details"
    )

    passenger_window.geometry(
        "800x700"
    )

    passenger_window.config(bg=BG)
    passenger_window.resizable(False, False)

    header = Frame(
        passenger_window,
        bg=BG,
        height=120
    )

    header.pack(fill=X)
    header.pack_propagate(False)

    Label(
        header,
        text="✈  PASSENGER DETAILS",
        font=("Segoe UI", 25, "bold"),
        bg=BG,
        fg=WHITE
    ).pack(pady=(20, 3))

    Label(
        header,
        text="Enter details for all passengers",
        font=("Segoe UI", 11),
        bg=BG,
        fg=TEXT
    ).pack()

    main_card = Frame(
        passenger_window,
        bg=CARD,
        highlightbackground="#1B4D6D",
        highlightthickness=1
    )

    main_card.pack(
        padx=40,
        pady=20,
        fill=BOTH,
        expand=True
    )

    Label(
        main_card,
        text=f"{from_city}  ✈  {to_city}",
        font=("Segoe UI", 18, "bold"),
        bg=CARD,
        fg=WHITE
    ).pack(pady=(15, 3))

    Label(
        main_card,
        text=f"{journey_date}   |   {selected_flight}",
        font=("Segoe UI", 10),
        bg=CARD,
        fg=GOLD
    ).pack(pady=(0, 10))

    container = Frame(
        main_card,
        bg=CARD
    )

    container.pack(
        fill=BOTH,
        expand=True,
        padx=15
    )

    canvas = Canvas(
        container,
        bg=CARD,
        highlightthickness=0
    )

    scrollbar = Scrollbar(
        container,
        orient=VERTICAL,
        command=canvas.yview
    )

    frame = Frame(
        canvas,
        bg=CARD
    )

    canvas_window = canvas.create_window(
        (0, 0),
        window=frame,
        anchor="nw"
    )

    canvas.configure(
        yscrollcommand=scrollbar.set
    )

    scrollbar.pack(
        side=RIGHT,
        fill=Y
    )

    canvas.pack(
        side=LEFT,
        fill=BOTH,
        expand=True
    )

    def update_width(event):

        canvas.itemconfig(
            canvas_window,
            width=event.width
        )

    canvas.bind(
        "<Configure>",
        update_width
    )

    frame.bind(
        "<Configure>",
        lambda event:
        canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    entries = []

    for i in range(passengers):

        passenger_card = Frame(
            frame,
            bg=CARD2,
            highlightbackground="#1B4D6D",
            highlightthickness=1
        )

        passenger_card.pack(
            fill=X,
            padx=10,
            pady=8
        )

        Label(
            passenger_card,
            text=f"PASSENGER {i + 1}",
            font=("Segoe UI", 13, "bold"),
            bg=CARD2,
            fg=WHITE
        ).pack(pady=(12, 3))

        Label(
            passenger_card,
            text=f"Assigned Seat: {seats[i]}",
            font=("Segoe UI", 10, "bold"),
            bg=CARD2,
            fg=GOLD
        ).pack(pady=(0, 12))

        # NAME

        Label(
            passenger_card,
            text="FULL NAME",
            font=("Segoe UI", 9, "bold"),
            bg=CARD2,
            fg=TEXT
        ).pack()

        name = Entry(
            passenger_card,
            width=42,
            font=("Segoe UI", 11),
            bg=WHITE,
            fg=DARK_TEXT,
            relief="flat"
        )

        name.pack(
            pady=(5, 10),
            ipady=5
        )

        # AGE

        Label(
            passenger_card,
            text="AGE",
            font=("Segoe UI", 9, "bold"),
            bg=CARD2,
            fg=TEXT
        ).pack()

        age = Entry(
            passenger_card,
            width=42,
            font=("Segoe UI", 11),
            bg=WHITE,
            fg=DARK_TEXT,
            relief="flat"
        )

        age.pack(
            pady=(5, 10),
            ipady=5
        )

        # AGE GROUP

        Label(
            passenger_card,
            text="AGE GROUP",
            font=("Segoe UI", 9, "bold"),
            bg=CARD2,
            fg=TEXT
        ).pack()

        age_group = Combobox(
            passenger_card,
            values=[
                "Child",
                "Adult",
                "Old Age"
            ],
            state="readonly",
            width=39,
            font=("Segoe UI", 10)
        )

        age_group.pack(
            pady=(5, 10)
        )

        # GENDER

        Label(
            passenger_card,
            text="GENDER",
            font=("Segoe UI", 9, "bold"),
            bg=CARD2,
            fg=TEXT
        ).pack()

        gender = Combobox(
            passenger_card,
            values=[
                "Male",
                "Female",
                "Other"
            ],
            state="readonly",
            width=39,
            font=("Segoe UI", 10)
        )

        gender.pack(
            pady=(5, 10)
        )

        # TRAVEL CLASS

        Label(
            passenger_card,
            text="TRAVEL CLASS",
            font=("Segoe UI", 9, "bold"),
            bg=CARD2,
            fg=TEXT
        ).pack()

        travel_class = Combobox(
            passenger_card,
            values=[
                "Economy Class",
                "Premium Economy",
                "Business Class",
                "First Class"
            ],
            state="readonly",
            width=39,
            font=("Segoe UI", 10)
        )

        travel_class.pack(
            pady=(5, 15)
        )

        entries.append(
            (
                name,
                age,
                age_group,
                gender,
                travel_class
            ))

    def proceed():

        passenger_list = []

        for (
            name,
            age,
            age_group,
            gender,
            travel_class
        ) in entries:

            passenger_name = name.get().strip()
            passenger_age = age.get().strip()
            selected_age_group = age_group.get().strip()
            passenger_gender = gender.get().strip()
            selected_class = travel_class.get().strip()

            # CHECK EMPTY

            if (
                not passenger_name
                or not passenger_age
                or not selected_age_group
                or not passenger_gender
                or not selected_class
            ):

                messagebox.showerror(
                    "Missing Details",
                    "Please fill all passenger details.",
                    parent=passenger_window
                )

                return

            # NAME

            if not passenger_name.replace(
                " ",
                ""
            ).isalpha():

                messagebox.showerror(
                    "Invalid Name",
                    "Please enter a valid passenger name.",
                    parent=passenger_window
                )

                return

            # AGE

            if (
                not passenger_age.isdigit()
                or not (
                    1 <= int(passenger_age) <= 120
                )
            ):

                messagebox.showerror(
                    "Invalid Age",
                    "Please enter an age between 1 and 120.",
                    parent=passenger_window
                )

                return

            actual_age = int(passenger_age)

            if selected_age_group == "Child":

                if actual_age > 17:

                    messagebox.showerror(
                        "Age Group Error",
                        "Child age should be between 1 and 17.",
                        parent=passenger_window
                    )

                    return

            elif selected_age_group == "Adult":

                if actual_age < 18 or actual_age > 59:

                    messagebox.showerror(
                        "Age Group Error",
                        "Adult age should be between 18 and 59.",
                        parent=passenger_window
                    )

                    return

            elif selected_age_group == "Old Age":

                if actual_age < 60:

                    messagebox.showerror(
                        "Age Group Error",
                        "Old Age passenger should be 60 or above.",
                        parent=passenger_window
                    )

                    return

            passenger_list.append(
                {
                    "name": passenger_name,
                    "age": passenger_age,
                    "age_group": selected_age_group,
                    "gender": passenger_gender,
                    "travel_class": selected_class
                }
            )

        passenger_window.destroy()

        payment_page(
            passenger_list,
            from_city,
            to_city,
            journey_date,
            passengers,
            seats,
            selected_flight
        )

    style_button(
        passenger_window,
        "PROCEED TO PAYMENT  →",
        proceed,
        GREEN,
        25
    ).pack(pady=12)

def payment_page(
    passenger_list,
    from_city,
    to_city,
    journey_date,
    passengers,
    seats,
    selected_flight
):

    payment = Toplevel(root)

    payment.title("Lakra Airlines | Payment")
    payment.geometry("700x600")
    payment.config(bg=BG)
    payment.resizable(False, False)

    header = Frame(
        payment,
        bg=BG,
        height=120
    )

    header.pack(fill=X)
    header.pack_propagate(False)

    Label(
        header,
        text="💳  SECURE PAYMENT",
        font=("Segoe UI", 25, "bold"),
        bg=BG,
        fg=WHITE
    ).pack(pady=(20, 3))

    Label(
        header,
        text="Complete your payment securely",
        font=("Segoe UI", 11),
        bg=BG,
        fg=TEXT
    ).pack()

    card = Frame(
        payment,
        bg=CARD,
        highlightbackground="#1B4D6D",
        highlightthickness=1
    )

    card.pack(
        padx=55,
        pady=25,
        fill=BOTH,
        expand=True
    )

    Label(
        card,
        text=f"{from_city}  ✈  {to_city}",
        font=("Segoe UI", 18, "bold"),
        bg=CARD,
        fg=WHITE
    ).pack(pady=(20, 3))

    Label(
        card,
        text=f"{journey_date}   |   {selected_flight}",
        font=("Segoe UI", 10),
        bg=CARD,
        fg=GOLD
    ).pack(pady=(0, 18))

    Label(
        card,
        text="CARD PAYMENT",
        font=("Segoe UI", 18, "bold"),
        bg=CARD,
        fg=WHITE
    ).pack(pady=(5, 18))

    Label(
        card,
        text="CARD NUMBER",
        font=("Segoe UI", 9, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack()

    card_number = Entry(
        card,
        width=40,
        font=("Segoe UI", 11),
        bg=WHITE,
        fg=DARK_TEXT,
        relief="flat"
    )

    card_number.pack(
        pady=(5, 18),
        ipady=6
    )

    Label(
        card,
        text="CARD HOLDER NAME",
        font=("Segoe UI", 9, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack()

    card_holder = Entry(
        card,
        width=40,
        font=("Segoe UI", 11),
        bg=WHITE,
        fg=DARK_TEXT,
        relief="flat"
    )

    card_holder.pack(
        pady=(5, 20),
        ipady=6
    )

    Label(
        card,
        text="🔒  Your payment information is secure",
        font=("Segoe UI", 10),
        bg=CARD,
        fg=GREEN
    ).pack(pady=(0, 15))

    def generate_ticket():

        ticket = Toplevel(root)

        ticket.title(
            "Lakra Airlines | Boarding Pass"
        )

        ticket.geometry(
            "900x700"
        )

        ticket.config(bg=BG)
        ticket.resizable(False, False)

        header = Frame(
            ticket,
            bg=BG,
            height=120
        )

        header.pack(fill=X)
        header.pack_propagate(False)

        Label(
            header,
            text="✈  LAKRA AIRLINES",
            font=("Segoe UI", 26, "bold"),
            bg=BG,
            fg=WHITE
        ).pack(pady=(20, 2))

        Label(
            header,
            text="BOARDING PASS",
            font=("Segoe UI", 11, "bold"),
            bg=BG,
            fg=GOLD
        ).pack()

        ticket_card = Frame(
            ticket,
            bg=CARD,
            highlightbackground="#1B4D6D",
            highlightthickness=1
        )

        ticket_card.pack(
            padx=50,
            pady=20,
            fill=BOTH,
            expand=True
        )

        Label(
            ticket_card,
            text=f"{from_city.upper()}   ✈   {to_city.upper()}",
            font=("Segoe UI", 23, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(pady=(20, 5))

        Label(
            ticket_card,
            text=f"Flight: {selected_flight}",
            font=("Segoe UI", 11, "bold"),
            bg=CARD,
            fg=GOLD
        ).pack(pady=5)

        info = Frame(
            ticket_card,
            bg=CARD2
        )

        info.pack(
            fill=X,
            padx=30,
            pady=15
        )

        Label(
            info,
            text=f"JOURNEY DATE\n{journey_date}",
            font=("Segoe UI", 10, "bold"),
            bg=CARD2,
            fg=WHITE,
            width=20
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=12
        )

        Label(
            info,
            text="PAYMENT STATUS\nPAID",
            font=("Segoe UI", 10, "bold"),
            bg=CARD2,
            fg=GREEN,
            width=20
        ).grid(
            row=0,
            column=1,
            padx=5,
            pady=12
        )

        Label(
            info,
            text=f"PASSENGERS\n{passengers}",
            font=("Segoe UI", 10, "bold"),
            bg=CARD2,
            fg=WHITE,
            width=20
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=12
        )

        Label(
            ticket_card,
            text="PASSENGER DETAILS",
            font=("Segoe UI", 14, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(pady=(8, 5))

        for i, passenger_data in enumerate(passenger_list):

            passenger_frame = Frame(
                ticket_card,
                bg=CARD2
            )

            passenger_frame.pack(
                fill=X,
                padx=30,
                pady=4
            )

            Label(
                passenger_frame,
                text=(
                    f"{i + 1}. "
                    f"{passenger_data['name']}   |   "
                    f"Age: {passenger_data['age']}   |   "
                    f"{passenger_data['age_group']}   |   "
                    f"{passenger_data['gender']}   |   "
                    f"{passenger_data['travel_class']}   |   "
                    f"Seat: {seats[i]}"
                ),
                font=("Segoe UI", 9),
                bg=CARD2,
                fg=TEXT
            ).pack(
                anchor="w",
                padx=12,
                pady=9
            )

        button_area = Frame(
            ticket_card,
            bg=CARD
        )

        button_area.pack(pady=15)

        def restart_booking():

            ticket.destroy()
            open_search()

        style_button(
            button_area,
            "BOOK ANOTHER",
            restart_booking,
            BLUE,
            18
        ).pack(
            side=LEFT,
            padx=8
        )

        style_button(
            button_area,
            "CLOSE",
            ticket.destroy,
            RED,
            12
        ).pack(
            side=LEFT,
            padx=8
        )

    def pay():

        card_num = card_number.get().strip()
        holder_name = card_holder.get().strip()

        if not card_num or not holder_name:

            messagebox.showerror(
                "Payment Error",
                "Please fill all payment details.",
                parent=payment
            )

            return

        if (
            len(card_num) != 16
            or not card_num.isdigit()
        ):

            messagebox.showerror(
                "Invalid Card",
                "Please enter a valid 16-digit card number.",
                parent=payment
            )

            return

        if not holder_name.replace(
            " ",
            ""
        ).isalpha():

            messagebox.showerror(
                "Invalid Name",
                "Please enter a valid card holder name.",
                parent=payment
            )

            return

        saved = save_booking_to_database(
            passenger_list,
            from_city,
            to_city,
            journey_date,
            selected_flight,
            seats
        )

        if not saved:
            return

        for i, passenger_data in enumerate(passenger_list):

            booking_history.append(
                f"{passenger_data['name']} | "
                f"{passenger_data['age_group']} | "
                f"{passenger_data['travel_class']} | "
                f"{from_city} -> {to_city} | "
                f"{journey_date} | "
                f"Seat {seats[i]}"
            )

        payment.destroy()

        messagebox.showinfo(
            "Payment Successful",
            "Payment completed successfully!\n\n"
            "Booking has been saved to MySQL."
        )

        generate_ticket()

    style_button(
        card,
        "PAY NOW  ✓",
        pay,
        GREEN,
        20
    ).pack(pady=10)

root = Tk()

root.withdraw()

root.title(
    "Lakra Airlines | Ticket Booking System"
)

root.geometry(
    "1100x700"
)

root.minsize(
    950,
    650
)

root.config(bg=BG)

header = Frame(
    root,
    bg=BG,
    height=150
)

header.pack(fill=X)
header.pack_propagate(False)

Label(
    header,
    text="✈  LAKRA AIRLINES",
    font=("Segoe UI", 32, "bold"),
    bg=BG,
    fg=WHITE
).pack(pady=(25, 2))

Label(
    header,
    text="AIRLINE TICKET BOOKING SYSTEM",
    font=("Segoe UI", 13, "bold"),
    bg=BG,
    fg=GOLD
).pack()


Label(
    root,
    text="Book your dream journey around the world",
    font=("Segoe UI", 13, "italic"),
    bg=BG,
    fg=TEXT
).pack(pady=18)

dashboard = Frame(
    root,
    bg=BG,
    highlightbackground="#1B4D6D",
    highlightthickness=1
)

dashboard.pack(
    padx=100,
    pady=15,
    fill=X
)

Label(
    dashboard,
    text="BOOK YOUR JOURNEY",
    font=("Segoe UI", 20, "bold"),
    bg=CARD,
    fg=WHITE
).pack(pady=(25, 5))

Label(
    dashboard,
    text="Search flights, select your seat and complete your booking.",
    font=("Segoe UI", 10),
    bg=CARD,
    fg=TEXT
).pack(pady=(0, 20))


style_button(
    dashboard,
    "✈  SEARCH FLIGHTS",
    open_search,
    BLUE,
    25
).pack(pady=8)


style_button(
    dashboard,
    "▤  VIEW BOOKING HISTORY",
    view_history,
    CARD2,
    25
).pack(pady=8)


style_button(
    dashboard,
    "EXIT",
    root.destroy,
    RED,
    25
).pack(pady=(8, 25))


Label(
    root,
    text="Secure Booking  •  Easy Payments  •  MySQL Database",
    font=("Segoe UI", 10),
    bg=BG,
    fg="#7FA4BA"
).pack(pady=18)

if __name__ == "__main__":

    if setup_database():


        otp_window = Toplevel(root)

        OTPVerificationApp(otp_window)

        root.mainloop()