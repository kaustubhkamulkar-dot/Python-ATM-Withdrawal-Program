# Python ATM Withdrawal Program

## Project overview

This beginner-friendly command-line project models a few common ATM actions: sign in with a sample PIN, check a balance, withdraw cash, and review withdrawals made during the current run. It uses core Python features such as functions, loops, lists, conditionals, and exception handling.

> This program is for learning only. It is not connected to a bank or financial institution, and its sample PIN and balance are not real account information.

## Objectives

- Demonstrate a simple ATM workflow in Python.
- Require a correct PIN before displaying the menu, with up to three attempts.
- Show the current sample balance.
- Validate withdrawal amounts before changing the balance.
- Keep a list of successful withdrawals during the current session.
- Respond clearly to invalid input and menu selections.

## Features

### PIN check

The user must enter the sample PIN before accessing the ATM menu. Three unsuccessful attempts end the session.

### Balance inquiry

Displays the current balance. A successful withdrawal updates the balance shown by later inquiries.

### Cash withdrawal

The program accepts positive amounts in multiples of Rs. 100, provided the balance can cover the withdrawal. Invalid amounts leave the balance unchanged.

### Session transaction history

Each successful withdrawal is added to a numbered list. The program reports when the list is empty.

### Input handling

Non-numeric withdrawal values and menu selections are caught and reported without abruptly ending the session.

## Tools and Python concepts

- **Language:** Python 3
- **Libraries:** No external packages required
- **Editor:** Python IDLE, VS Code, or another Python editor
- **Version control:** Git and GitHub

| Concept | How the program uses it |
| --- | --- |
| Functions | Separates balance display, withdrawal, history, and program flow. |
| Conditionals | Checks PINs, withdrawal rules, and menu choices. |
| `for` loop | Limits login attempts and numbers the history entries. |
| `while` loop | Keeps the ATM menu available until the user exits. |
| Lists | Stores successful withdrawals for the current run. |
| `try-except` | Handles invalid numeric input with `ValueError`. |
| Arithmetic | Calculates the remaining balance and checks withdrawal amounts. |

## Requirements

- Python 3 installed
- A terminal or Python editor

No additional Python packages are needed.

## Run the program

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Start the program:

   ```bash
   python atm_withdrawal.py
   ```

   If your computer uses `python3`, run `python3 atm_withdrawal.py` instead.
4. Enter the demonstration PIN and choose an option from the menu.

## Demonstration values

| Item | Sample value |
| --- | --- |
| PIN | `1234` |
| Starting balance | Rs. 10,000 |
| Login attempts | 3 |

These values are defined in the source code. The PIN is hardcoded and is not secure; never use this program to protect real financial information.

## Example session

```text
===== WELCOME TO PYTHON ATM =====
Enter your 4-digit PIN: 1234

Login successful!

===== ATM MENU =====
1. Check Balance
2. Withdraw Money
3. Transaction History
4. Exit

Enter your choice: 2
Enter withdrawal amount: Rs. 2000
Please collect your cash.
Remaining balance: Rs. 8000.00

===== ATM MENU =====
1. Check Balance
2. Withdraw Money
3. Transaction History
4. Exit

Enter your choice: 4
Thank you for using Python ATM!
```

## Scenarios to try

| Scenario | Expected behavior |
| --- | --- |
| Enter the correct PIN | The ATM menu appears. |
| Enter an incorrect PIN three times | Access is denied and the program ends. |
| Check the balance | The current balance is displayed. |
| Withdraw Rs. 2,000 | The balance decreases by Rs. 2,000 and the withdrawal is recorded. |
| Request more than the available balance | The program reports insufficient balance. |
| Enter zero, a negative amount, or a non-multiple of Rs. 100 | The withdrawal is rejected. |
| Enter letters instead of an amount or menu number | An input error is displayed and the program continues. |
| Choose an option outside 1–4 | The program asks for a valid menu choice. |

## Files

```text
Python-ATM-Withdrawal-Program/
├── atm_withdrawal.py
└── README.md
```

## Limitations and possible extensions

The balance and PIN are fixed in the source, and transaction history exists only until the program exits. Possible next steps include saving records to a file, supporting several demo users, adding deposits, generating receipts, or building a graphical interface.

## Summary

This project brings together basic Python programming ideas in a familiar ATM-style workflow. It practices input validation and small, reusable functions while keeping the operations simple enough for a first programming project.

## Project information

- **Project:** ATM Withdrawal Program using Python
- **Type:** Python programming mini project
- **Students:** KAUSTUBH KAMULKAR and DRISHTY HATWALNE
- **College:** Pimpri Chinchwad University (PCU)
- **Subject:** Python Programming
- **GitHub repository:** [Python-ATM-Withdrawal-Program](https://github.com/kaustubhkamulkar-dot/Python-ATM-Withdrawal-Program)
