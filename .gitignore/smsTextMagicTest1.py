import textmagic.rest.client

from textmagic.rest import TextmagicRestClient

username = "sandeepbhatnagar"
token = "V4CNiw2g624OIcV0ScT2vYgXEv8NCV"
client = textmagic.rest.client.TextmagicRestClient(username, token)
#name = client.contacts.name
name = client.user.name
print(name)

# Send a message and store its message id
result = client.messages.create(phones="19254138648, 14086485999, ", text="Hello from TextMagic -- finally got this working in python-- sandeep")
# Send a message and store its message id
#result = client.send(text="Hello, World!", phones="9254138648")
#    message_id = result['message_id'].keys()[0]

# Now you can retrieve the delivery status using the message id
#response = client.message_status(message_id)
#response = client.stats_messaging(message_id)
#status = response[message_id]['status']
##status = response[message_id]['status']