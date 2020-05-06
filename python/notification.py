import firebase_admin
from firebase_admin import messaging

default_app = firebase_admin.initialize_app()

# This registration token comes from the client FCM SDKs.
registration_token = 'token'

myNotification = messaging.Notification(title='Test', body='Hello, FCM from My Phthon Server!')

# See documentation on defining a message payload.
message = messaging.Message(
    data={
        'score': '850',
        'time': '2:45',
    },
    token=registration_token,
    notification=myNotification
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)