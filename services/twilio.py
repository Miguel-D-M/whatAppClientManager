import app
from flask import request
import requests
from twilio.twiml.messaging_response import MessagingResponse

from services.bot import chatbot_response


@app.route('/twilio', methods=['POST'])
def bot():  # put application's code here
    incoming_msg = request.values.get('Body', '').lower()
    msg_sender = request.values.get('Sender', '')
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(chatbot_response(incoming_msg, msg_sender))
    return str(resp)

