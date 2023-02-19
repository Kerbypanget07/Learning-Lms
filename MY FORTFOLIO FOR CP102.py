import time
import datetime
import re
import hashlib
import tkinter as tk

true = True
false = False


def ld():
    c = "Now Loading"
    print(c, end="")
    for a in "...":
        time.sleep(0.5)
        print(a, end="")


ld()

time.sleep(1)


def wlc():
    for d in "\nGreetings, Welcome to Learning LMS! ver 1.1":
        time.sleep(0.1)
        print(d, end="")


wlc()


def pgm(answer):
    if answer == "Y" or answer == "y":
        return ("Welcome!")
    elif answer == "N" or answer == "n":
        return ("Goodbye.")
    return ("Please input Y or N only.")


while True:

    v = "\nWould you like to launch the program?"
    print(v)

    v1 = "\nY or N?"
    print(v1)

    try:
        a2 = input("Response? (Y/N): ")
        if a2 == "N" or a2 == "n":
            print(pgm(a2))
            exit()
        elif a2 == "Y" or a2 == "y":
            break
        else:
            print("Please input Y or N only.")
            exit()
    except ValueError:
        print("Please enter just letters.")
        exit()
    break
    time.sleep(1)

ld()

print()

f2 = {}


def signup():
    print("Personal Details: (Sign-In)")

    while True:
        email = input("Provide email address: ")
        match = re.match(r"^[a-zA-Z0-9._%+-]+@(gmail|yahoo|protonmail|outlook|aol|zoho|iCloud|yahoo!|gmx)\.[a-zA-Z]{2,}$", email)

        if match:
            print("Your email is Saved")
            break

        else:
            print("Invalid email address. Please enter another valid email.")

    while True:
        password = input("Enter a strong password (Should be at least 8 characters): ")
        match = re.search(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$', password)

        if match:
            print("Your password is saved")
            print()
            time.sleep(1)
            print("Login to Continue")
            print()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            f2[email] = hashed_password
            break

        else:
            print("Invalid password. Please enter a valid password.")


def home():
    time.sleep(1)

    print()

    def wlc2():
        for d in "Welcome to Learning Lms! \nFirst in Cyberlms in the whole country!":
            time.sleep(0.1)
            print(d, end="")

    wlc2()
    n = datetime.datetime.now()
    time.sleep(1)
    v = ("\nDate and time as of right now:")
    print(v, n)


    while True:
        time.sleep (1)
        ch = "\n1: Lesson Materials \n2: Personal Information \n3: Calculator \n4: Exit"
        print(ch)
        g = int(input("\nPlease choose any action (1-4): "))

        def ld2():
            g1 = f"{g} is loading"
            print(g1, end="")
            for a in "...":
                time.sleep(0.5)
                print(a, end="")

        if g == 1:
            ld2()

            window = tk.Tk()

            window.title("Subject Description")

            window.geometry("1920x1080")

            label1 = tk.Label(window, text="LEARNING LMS VER 1.1 \nBY KERBY MADDAGAN\nSimply enter the subjects' names")
            label1.pack()

            label3 = tk.Label(window,
                              text="SUBJECTS LIST \n Mathematics \n Science  \n Geography \n English \n Filipino")
            label3.pack()

            entry2 = tk.Entry(window)
            entry2.pack()

            def show_description():
                subject = entry2.get()
                desc = s.get(subject, "Subject not found.")
                label4.config(text=desc)

            button1 = tk.Button(window, text="Get Description", command=show_description)
            button1.pack()

            label4 = tk.Label(window)
            label4.pack()

            button2 = tk.Button(window, text="Exit", command=window.destroy)
            button2.pack()

            s = {
                "Mathematics": "Mathematics is essential for developing problem-solving and critical-thinking skills. It is also the foundation for many fields, including science, technology, engineering, and mathematics (STEM).\nOTHER LEARNING MATERIALS ARE AVAILABLE SOON!",
                "Science": "Science is important for understanding the natural world and making informed decisions. It helps develop critical-thinking and problem-solving skills, and is essential for many careers in STEM fields.\nOTHER LEARNING MATERIALS ARE AVAILABLE SOON!",
                "Geography": "Geography is important for understanding the physical and cultural features of the world. It helps students develop a global perspective and appreciate diversity.\nOTHER LEARNING MATERIALS ARE AVAILABLE SOON!",
                "English": "English is essential for effective communication, both written and verbal. It is important for many careers, including journalism, law, and business.\nOTHER LEARNING MATERIALS ARE AVAILABLE SOON!",
                "Filipino": "Filipino is important for understanding the language, culture, and history of the Philippines. It helps develop a sense of national identity and pride.\nOTHER LEARNING MATERIALS ARE AVAILABLE SOON!"
            }

            window.mainloop()

        elif g == 2:
            ld2()
            time.sleep (1)
            print ()
            h = ("\nPlease Login in order for your credentials to be saved:")
            print (h)
            name = input("\nPlease enter your Full name: ")
            age = input("Please enter your Current age: ")
            address = input("Please enter your Full address: ")
            print(f"\nName: {name}\nAge: {age}\nAddress: {address}")
            time.sleep (1)
            print ("Saving...")
            time.sleep (1)
            print ()
            print ("Login Credentials Saved!")

        elif g == 3:
            ld2()
            print ()
            i = ("\nWelcome to Calculator 1.1!")
            print (i)
            print ()
            num1 = eval(input("Please enter the first Digit: "))
            num2 = eval(input("Please type in the second Digit: "))
            op = input("Please choose an operation sign (+, -, *, /): ")

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2
            print ()
            print ("Calculating...")
            time.sleep(1)
            print(f"{num1} {op} {num2} = {result} is the answer.")

        elif g == 4:
            print("Goodbye.")
            exit()
            break


        else:
            print("Invalid input")

def login():
    e = input("Re-Enter your email address: ")
    p = input("Re-Enter password: ")
    h_p = hashlib.sha256(p.encode()).hexdigest()

    if e in f2 and f2[e] == h_p:
        print("Login Credentials Accepted.")
        home()
    else:
        print("Invalid email or password. Please try again.")

while True:
    time.sleep(1)
    v = ("Choose an option: (1-3)")
    print(v)
    print("\n 1: Sign up \n 2: Login \n 3: Exit")
    print()
    c = input("Enter an Option: ")
    print()
    if c == "1" or c == "Sign up":
        signup()
    elif c == "2" or c == "Login":
        login()
    elif c == "3" or c == "Exit":
        print("Goodbye.")
        exit()
    else:
        print("Invalid Option!")

while True:
    print("Y or N?")
    try:

        r = input("Response? (Y/N): ")
        if r == "N" or r == "n":
            print(program(r))
            exit()
        elif r == "Y" or r == "y":
            print(program(r))
            loading()
        else:
            print("Please input Y or N only.")
    except ValueError:
        print("Please enter just letters.")
        exit()