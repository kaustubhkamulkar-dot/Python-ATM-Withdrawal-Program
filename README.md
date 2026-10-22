# Python ATM Withdrawal Program

A beginner-friendly, command-line ATM simulation written in Python. It demonstrates PIN verification, balance inquiry, validated withdrawals, and session transaction history.

> This is an educational simulation. It is not connected to a bank or payment system. The PIN and balance are sample values only.

## Features

- Requires a four-digit demonstration PIN before showing the ATM menu
- Allows up to three PIN attempts
- Displays the current balance
- Accepts withdrawals only when the amount is positive, a multiple of Rs. 100, and within the available balance
- Records successful withdrawals for the current session
- Handles invalid menu choices and non-numeric input

## Requirements

- Python 3
- No third-party packages

## Run

```bash
python atm_withdrawal.py
```

Use the sample PIN `1234` to sign in. The starting balance is Rs. 10,000.00.

## Menu

1. Check balance
2. Withdraw money
3. View transaction history
4. Exit

## Project information

- Students: **KAUSTUBH KAMULKAR** and **DRISHTI HATWALE**
- Subject: Python Programming
- Repository: [Python-ATM-Withdrawal-Program](https://github.com/kaustubhkamulkar-dot/Python-ATM-Withdrawal-Program)
