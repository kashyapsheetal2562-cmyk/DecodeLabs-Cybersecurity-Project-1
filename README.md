# 🔐 DecodeLabs Cybersecurity Project 1
## Password Strength Checker

A Python-based Password Strength Checker developed as part of the DecodeLabs Cybersecurity Internship.

## 📌 Project Overview

This project evaluates the strength of a password using fundamental cybersecurity validation techniques.

The program classifies passwords into three categories:

- Weak
- Medium
- Strong

## 🎯 Requirements Covered

The program checks:

- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Commonly used passwords

## 🚀 Features

### Password Length Check
Checks whether the password contains at least 8 characters.

### Character Variety
Checks for uppercase letters, lowercase letters, numbers and special characters.

### Common Password Detection
Detects commonly used passwords such as:

- password
- 123456
- qwerty
- admin123

### Security Recommendations
The program provides suggestions when a password does not meet security requirements.

### Secure Input
Python's `getpass` module is used so that the password is not displayed while being entered.

## 🛠️ Technologies Used

- Python 3
- Regular Expressions
- String Handling
- Conditional Logic
- Input Validation
- `getpass`

## 📂 Project Structure

```text
DecodeLabs-Cybersecurity-Project-1/
│
├── password_checker.py
├── README.md
├── requirements.txt
├── .gitignore
└── screenshots/
