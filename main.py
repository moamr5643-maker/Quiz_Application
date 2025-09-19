from tkinter import *
from models import Quiz
from loader import load_questions

# -------------------------
# Data
# -------------------------
questions = load_questions()
quiz = Quiz(questions)

# -------------------------
# GUI
# -------------------------
window = Tk()
window.title("Quiz App")
window.geometry("500x400")

label_q = Label(window, text="", font=("Arial", 16))
label_q.pack(pady=10)

label_result = Label(window, text="", font=("Arial", 16))
label_result.pack(pady=10)

var = StringVar()
option_buttons = []
for i in range(4):
    button = Radiobutton(window, text="", variable=var, value="", font=("Arial", 14))
    button.pack(anchor="w")
    option_buttons.append(button)


def show_questions():
    if quiz.is_more():
        current_question = quiz.get_question()
        label_q.config(text=current_question.text)
        var.set("")
        for i, option in enumerate(current_question.options):
            option_buttons[i].config(text=option, value=option)
        label_result.config(text="")
    else:
        label_q.config(text=f"Quiz finished! Your score = {quiz.score}/{len(questions)}")
        for rb in option_buttons:
            rb.pack_forget()
        check_button.pack_forget()
        label_result.pack_forget()


def check_answer():
    choice = var.get()
    if choice == "":
        label_result.config(text="Choose something !!", fg="orange")
    else:
        current_q = quiz.get_question()
        is_correct = quiz.check_answer(choice)
        if is_correct:
            label_result.config(text="Correct Answer", fg="green")
        else:
            label_result.config(text=f"Wrong Answer, correct is {current_q.answer}", fg="red")
        window.after(2000, show_questions)


check_button = Button(window, text="Check", command=check_answer, bg="blue", font=("Arial", 14))
check_button.pack(pady=10)

show_questions()
window.mainloop()
