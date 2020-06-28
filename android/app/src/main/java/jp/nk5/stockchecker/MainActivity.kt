package jp.nk5.stockchecker

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.EditText
import android.widget.ListView
import com.google.android.gms.tasks.OnCompleteListener
import com.google.firebase.iid.FirebaseInstanceId

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    override fun onStart() {
        super.onStart()

        FirebaseInstanceId.getInstance().instanceId
            .addOnCompleteListener(OnCompleteListener { task ->
                if (!task.isSuccessful) {
                    return@OnCompleteListener
                }

                // Get new Instance ID token
                val token = task.result?.token

                // Log and toast
                val messageView: EditText = findViewById(R.id.editText)
                messageView.setText(token)
            })

        val dao = NotificationsDAO(this)

        if (intent.getExtras() != null) {
            val date = intent.getExtras().getString("date").toInt()
            val message = intent.getExtras().getString("message")
            dao.createNotification(MyNotification(-1, date, message))
        }

        val messageList = dao.getAll()
        val listView: ListView = findViewById(R.id.listView)
        listView.adapter = MessageListAdapter(this, android.R.layout.simple_list_item_1, messageList.take(10))
    }

}
