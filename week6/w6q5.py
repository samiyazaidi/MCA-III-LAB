def save_student_details(filename):
    with open(filename, "w") as file:
        num_students = int(input("Enter the number of students: "))
        
        for i in range(num_students):
            roll_no = input(f"Enter Roll Number for student {i+1}: ")
            name = input(f"Enter Name for student {i+1}: ")
            marks = input(f"Enter Marks for student {i+1}: ")
            
            file.write(f"Roll Number: {roll_no}, Name: {name}, Marks: {marks}\n")
            
        print(f"Student details have been saved to {filename}.")

save_student_details("Marks.data")
