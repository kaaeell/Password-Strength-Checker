# Password Strength Checker

A Python terminal application that analyzes the strength of a password using common security criteria. The program evaluates length, character variety, and symbol usage, then classifies the password as Weak, Medium, or Strong while providing clear, readable feedback.

## Why This Project

Password validation is a real-world problem used in almost every application. This project focuses on writing clean Python logic to analyze user input and return meaningful results, making it a practical beginner project with real use cases.

## Features

- Checks minimum password length
- Detects lowercase and uppercase letters
- Detects numeric characters
- Detects special characters
- Scores the password and classifies its strength
- Displays detailed feedback for each rule

## How It Works

The password is evaluated against five basic rules. Each rule adds one point to the total score.  
The final score determines the password strength:

- 0–2 points: Weak  
- 3–4 points: Medium  
- 5 points: Strong  

## Getting Started

Make sure Python 3 is installed on your system.

Run the program from the project directory:

```bash
python main.py
