"""
Created on Wed Feb  8 06:20:55 2017

@author: kevinryan
"""

import twilio

print twilio.__version__


from twilio.rest import TwilioRestClient

account_sid = "ACfe7ef383b9126189023233973d5d3885" # Your Account SID from www.twilio.com/console
auth_token  = "b5604e88f36788e543dbfe1e9b5b3b8d"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+447789057451",    # Replace with your phone number
    from_="+441344567461") # Replace with your Twilio number

print(message.sid)