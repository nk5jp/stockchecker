package jp.nk5.stockchecker

import com.google.firebase.messaging.FirebaseMessagingService
import android.util.Log
import androidx.constraintlayout.widget.Constraints.TAG
import com.google.firebase.messaging.RemoteMessage

class MyFirebaseMessagingService: FirebaseMessagingService() {

    override fun onNewToken(token: String) {
        Log.d(TAG, "Refreshed token: $token")

        // If you want to send messages to this application instance or
        // manage this apps subscriptions on the server side, send the
        // Instance ID token to your app server.
        //sendRegistrationToServer(token)
    }

    override fun onMessageReceived(p0: RemoteMessage) {
        super.onMessageReceived(p0)
        val date = p0.data["date"]!!.toInt()
        val message = p0.data["message"]!!

        val dao = NotificationsDAO(this)
        dao.createNotification(MyNotification(-1, date, message))
    }


}
