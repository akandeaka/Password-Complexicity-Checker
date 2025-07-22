import reimport tkinter as tkfrom tkinter import ttkimport argparse
def assess_password_strength(password):    score = 0    feedback = []
# Check length
length = len(password)
if length < 8:
    feedback.append("Password is too short (minimum 8 characters).")
elif length >= 8 and length < 12:
    score += 20
    feedback.append("Good length (8-11 characters).")
else:
    score += 30
    feedback.append("Excellent length (12+ characters).")

# Check for uppercase letters
if re.search(r'[A-Z]', password):
    score += 20
    feedback.append("Contains uppercase letters: Good!")
else:
    feedback.append("Add uppercase letters for better strength.")

# Check for lowercase letters
if re.search(r'[a-z]', password):
    score += 20
    feedback.append("Contains lowercase letters: Good!")
else:
    feedback.append("Add lowercase letters for better strength.")

# Check for numbers
if re.search(r'\d', password):
    score += 20
    feedback.append("Contains numbers: Good!")
else:
    feedback.append("Add numbers for better strength.")

# Check for special characters
if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    score += 20
    feedback.append("Contains special characters: Good!")
else:
    feedback.append("Add special characters for better strength.")

# Check for common patterns to avoid
if re.search(r'(.)\1{2,}', password):
    score -= 10
    feedback.append("Warning: Avoid repeating characters more than twice.")

# Determine strength level
if score >= 90:
    strength = "Very Strong"
    color = "green"
elif score >= 70:
    strength = "Strong"
    color = "darkgreen"
elif score >= 50:
    strength = "Moderate"
    color = "orange"
elif score >= 30:
    strength = "Weak"
    color = "red"
else:
    strength = "Very Weak"
    color = "darkred"

return {
    "strength": strength,
    "score": score,
    "feedback": feedback,
    "color": color
}

def console_mode():    while True:        password = input("Enter a password to assess (or 'quit' to exit): ")        if password.lower() == 'quit':            break
    result = assess_password_strength(password)
    
    print("\nPassword Strength Assessment:")
    print(f"Strength: {result['strength']}")
    print(f"Score: {result['score']}/100")
    print("\nFeedback:")
    for comment in result['feedback']:
        print(f"- {comment}")
    print()

def gui_mode():    def update_assessment(event=None):        password = entry_password.get()        result = assess_password_strength(password)
    label_strength.config(text=f"Strength: {result['strength']}", foreground=result['color'])
    label_score.config(text=f"Score: {result['score']}/100")
    
    text_feedback.delete(1.0, tk.END)
    for comment in result['feedback']:
        text_feedback.insert(tk.END, f"- {comment}\n")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x500")
root.resizable(False, False)

# Create and place widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Password label and entry
label_password = ttk.Label(frame, text="Enter Password:")
label_password.grid(row=0, column=0, sticky=tk.W, pady=5)

entry_password = ttk.Entry(frame, show="*")
entry_password.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
entry_password.bind("<KeyRelease>", update_assessment)

# Strength label
label_strength = ttk.Label(frame, text="Strength: ", font=("Arial", 12, "bold"))
label_strength.grid(row=2, column=0, sticky=tk.W, pady=10)

# Score label
label_score = ttk.Label(frame, text="Score: 0/100", font=("Arial", 12))
label_score.grid(row=3, column=0, sticky=tk.W, pady=5)

# Feedback label and text area
label_feedback = ttk.Label(frame, text="Feedback:")
label_feedback.grid(row=4, column=0, sticky=tk.W, pady=5)

text_feedback = tk.Text(frame, height=10, width=40, wrap=tk.WORD)
text_feedback.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=5)

# Scrollbar for feedback
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text_feedback.yview)
scrollbar.grid(row=5, column=1, sticky=(tk.N, tk.S))
text_feedback['yscrollcommand'] = scrollbar.set

# Run initial assessment
update_assessment()

# Start the main loop
root.mainloop()

def main():    parser = argparse.ArgumentParser(description="Password Strength Checker")    parser.add_argument('--gui', action='store_true', help="Run in GUI mode")    args = parser.parse_args()
if args.gui:
    gui_mode()
else:
    console_mode()

if name == "main":    main()