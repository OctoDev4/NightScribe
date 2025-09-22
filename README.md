
<img width="1000" height="500" alt="Image" src="https://github.com/user-attachments/assets/90adca25-668d-4ca7-bed9-81f8eb0afbd9" /> 

A simple Python keylogger that records keystrokes and periodically sends the logs to an email address using Gmail's SMTP server.

---

## 🚨 Disclaimer
This project was created **for educational purposes only**.  
Using this software on someone else’s computer **without explicit permission** is illegal and may lead to **criminal charges**.  

---

## 📌 Features
- Captures all keyboard input.
- Detects special keys (e.g., space, enter, shift).
- Sends logs to an email address at configurable time intervals.
- Uses `smtplib` for email and `pynput` for keyboard listening.
- Runs in the background until stopped.

---

## 🛠️ Requirements
- Python 3.6+
- Python packages:
  ``bash
  pip install pynput
  ``
  ⚙️ Configuration

Edit the variables at the end of the file keylogger.py:

EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
TO_EMAIL = "recipient_email@gmail.com"


EMAIL_ADDRESS: The sender Gmail address.

EMAIL_PASSWORD: Gmail app password.

TO_EMAIL: The recipient email address where logs will be sent.


▶️ How to Run

Clone this repository or copy the main.py file.

Install dependencies:
``
pip install pynput
``

Run the script:
``
python main.py
``
