from fastapi import FastAPI
from uuid import UUID

app = FastAPI(
    title="The Boms Success Academy",
    description="We aim to be successful.",
)

# Temporary storage
students = []

# Registeration of student
@app.post("/students")
def add_student(name: str, age: int, classroom: str):
    student = {
        "id": len(students) + 1,
        "name": name,
        "age": age,
        "classroom": classroom
}
    students.append(student)
    return student 

# Getting Student
@app.get("/students/{students_id}")
def get_students(student_id: int):
    for student in students:
        if not students:
            return {"message": "You are not a student in Boms Academy"}
        return students


# Student update
@app.put("/students/{students_id}")
def update_student(
    id: int, name: str, age: int, classroom: str
):
    for student in students:
        if not student:
            return ("Error", "Student not found")

        student[id] = id
        student[name] = name
        student[age] = age
        student[classroom] = classroom

        return {"message": "Student List Update Successful", "data": student}


# Delete a student
@app.delete("/students/{students_id}")
def delete_student(student_id:str):
    for student in students:
        if not student:
            return {"Error": "Student Data Not Found"}
        del student_id
        return {"Message": "Student Data Successfully Deleted"}