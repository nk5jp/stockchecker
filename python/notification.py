import firebase_admin
from firebase_admin import messaging

def sendMessage(inputData):

    default_app = firebase_admin.initialize_app()

    registration_token = 'token'

    body = 'I have a message.'
    myNotification = messaging.Notification('stockChecker', body)

    # See documentation on defining a message payload.
    message = messaging.Message(
        data=inputData,
        token=registration_token,
        notification=myNotification
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)