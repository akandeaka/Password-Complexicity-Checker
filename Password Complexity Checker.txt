# 🔐 Password Complexity Checker

A beginner-friendly Python tool that evaluates the strength of user passwords using scoring logic and regex pattern matching. It provides feedback and recommendations to help users build stronger, more secure passwords — perfect for cybersecurity learners, developers, and IT support professionals.

---

## 📌 Project Description

The **Password Complexity Checker** is a terminal-based script developed to demonstrate real-world password validation and evaluation. Built with Python and regular expressions, this tool analyzes password characteristics such as length, character variety, and repetition to generate a score and give feedback.

This project was created as part of my learning journey with **Prodigy InfoTech**, and it's particularly useful for anyone learning about:

- Password hygiene and security
- Python programming
- Cybersecurity best practices
- Real-world use of regular expressions (`re` module)

---

## 🚀 Features

✅ Checks for:
- Minimum and optimal password length  
- Use of uppercase and lowercase letters  
- Use of numbers and special characters  
- Repetitive character detection  

✅ Provides:
- Score (0–100)
- Strength level (`Very Weak` to `Very Strong`)
- Real-time, user-friendly feedback

✅ Additional:
- Runs in a loop for multiple tests  
- Easy-to-modify code for learners  
- Ideal for integration into authentication systems

---

## 🧠 Why Password Complexity Matters

Passwords are the first line of defense against unauthorized access. Weak passwords like `123456`, `admin`, or simple names are easy to guess and are often exploited in data breaches.

By enforcing complexity rules (especially in environments like **Privileged Access Management - PAM**), organizations can significantly reduce the risk of compromise.

This tool simulates such enforcement in a user-friendly way.

---

## 🛠️ How It Works

| Criterion                  | Impact on Score | Description                                      |
|---------------------------|------------------|--------------------------------------------------|
| Length                    | +0 to +30        | Encourages 12+ characters                        |
| Uppercase Letters         | +20              | Improves password entropy                        |
| Lowercase Letters         | +20              | Ensures case variety                             |
| Numbers                   | +20              | Adds numerical complexity                        |
| Special Characters        | +20              | Adds non-standard character patterns             |
| Repetition of Characters | -10              | Penalizes repeated characters like "aaa"         |

The total score determines the password's strength label:
- **Very Weak** (0–29)
- **Weak** (30–49)
- **Moderate** (50–69)
- **Strong** (70–89)
- **Very Strong** (90–100)

---

## 💻 How to Run the Script

1. Save the script as `password_strength.py`.
2. Open a terminal or command prompt.
3. Navigate to the file's directory.
4. Run the script:

```bash
python password_strength.py
