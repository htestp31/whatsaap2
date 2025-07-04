from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get('Body').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "hi" in incoming_msg or "hello" in incoming_msg:
        msg.body(
            "👋 Hello! Welcome to G Tech Bot.\n"
            "Reply with:\n"
            "1 - 📆 Working Hours\n"
            "2 - 📞 Contact Info\n"
            "3 - 💼 Services\n"
            "exit - ❌ Exit"
        )
    elif incoming_msg == "1":
        msg.body("📅 Our working hours are:\nMonday to Saturday\n9:00 AM – 6:00 PM.")
    elif incoming_msg == "2":
        msg.body("📞 Contact us at:\nPhone: +91-9876543210\nEmail: support@gtech.in")
    elif incoming_msg == "3":
        msg.body("💼 We provide:\n- Diamond Cutting\n- Polishing\n- Grading & Inspection\nType 'hi' to go back.")
    elif incoming_msg == "exit":
        msg.body("👋 Thank you! Type 'hi' to start again.")
    else:
        msg.body("❓ I didn't get that. Please type 'hi' to begin or 'exit' to stop.")

    return str(resp)

if __name__ == "__main__":
    app.run()
