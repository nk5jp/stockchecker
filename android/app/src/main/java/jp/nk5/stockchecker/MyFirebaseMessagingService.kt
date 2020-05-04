package jp.nk5.stockchecker

import com.google.firebase.messaging.FirebaseMessagingService
import android.util.Log
import androidx.constraintlayout.widget.Constraints.TAG

class MyFirebaseMessagingService: FirebaseMessagingService() {

    override fun onNewToken(token: String) {
        Log.d(TAG, "Refreshed token: $token")

        // If you want to send messages to this application instance or
        // manage this apps subscriptions on the server side, send the
        // Instance ID token to your app server.
        //sendRegistrationToServer(token)
    }

}
