import tkinter as tk

def start_quiz():
    playing = input("Möchten Sie spielen? ")
    if playing != "ja":
        root.destroy()
    else:
        label1.config(text="Okay! Wir fangen an :)")
        ergebnis = 0
        answer = input("Was bedeutet CPU? ").lower()
        answer_input = answer_entry.get().lower()
        if answer_input == "central processing unit":
            label2.config(text="Richtig!")
        else:
            label2.config(text="Falsch!")

root = tk.Tk()
root.geometry("250x200")
label1 = tk.Label(root, text="Willkommen beim Quiz")
label1.pack()
label2 = tk.Label(root, text="")
label2.pack()
answer_entry = tk.Entry(root)
answer_entry.pack()
play_button = tk.Button(root, text="Spielen", command=start_quiz)
play_button.pack()
root.mainloop()
