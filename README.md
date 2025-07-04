# WhatsApp Bot (100% Free)

This is a simple, rule-based WhatsApp chatbot using Twilio Sandbox and Flask.

## 🚀 How to Run

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Start the Flask app:
    ```
    python app.py
    ```

3. Expose it using ngrok:
    ```
    ngrok http 5000
    ```

4. Set the ngrok URL as webhook in your Twilio Sandbox:
    ```
    https://xxxx.ngrok.io/whatsapp
    ```

5. Test it by sending "hi" to the Twilio Sandbox number from your WhatsApp.

Enjoy your free WhatsApp bot!
