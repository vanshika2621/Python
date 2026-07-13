from tkinter import *

# Create window
root = Tk()

root.title("Student Percentage Calculator")
root.geometry("400x400")

# Function to calculate percentage
def calculate():

    # Get marks from entry boxes
    m1 = int(sub1_entry.get())
    m2 = int(sub2_entry.get())
    m3 = int(sub3_entry.get())

    # Calculate total and percentage
    total = m1 + m2 + m3
    percentage = total / 3

    # Display percentage in result textbox
    result_entry.delete(0, END)
    result_entry.insert(0, str(percentage) + "%")


# ---------------- Labels ----------------

Label(root, text="Student Details",
      font=("Arial", 18)).pack(pady=10)

# Name
Label(root, text="Enter Name").pack()

name_entry = Entry(root, width=30)
name_entry.pack(pady=5)

# Gender
Label(root, text="Select Gender").pack()

gender = StringVar()

Radiobutton(root, text="Male",
            variable=gender,
            value="Male").pack()

Radiobutton(root, text="Female",
            variable=gender,
            value="Female").pack()

# Subject 1
Label(root, text="Marks of Subject 1").pack()

sub1_entry = Entry(root, width=20)
sub1_entry.pack(pady=5)

# Subject 2
Label(root, text="Marks of Subject 2").pack()

sub2_entry = Entry(root, width=20)
sub2_entry.pack(pady=5)

# Subject 3
Label(root, text="Marks of Subject 3").pack()

sub3_entry = Entry(root, width=20)
sub3_entry.pack(pady=5)

# Calculate Button
Button(root,
       text="Calculate Percentage",
       command=calculate).pack(pady=15)

# Result
Label(root, text="Percentage").pack()

result_entry = Entry(root, width=20)
result_entry.pack(pady=5)

# Run window
root.mainloop()