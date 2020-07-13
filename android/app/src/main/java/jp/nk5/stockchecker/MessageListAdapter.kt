package jp.nk5.stockchecker

import android.content.Context
import android.view.ViewGroup
import android.view.LayoutInflater
import android.view.View
import android.widget.ArrayAdapter
import android.widget.TextView
import java.util.*


class MessageListAdapter(context: Context, resource: Int, objects: List<MyNotification>) :
    ArrayAdapter<MyNotification>(context, resource, objects) {

    private var layoutInflater : LayoutInflater? = context.getSystemService(Context.LAYOUT_INFLATER_SERVICE) as LayoutInflater?

    override fun getView(position: Int, view: View?, parent: ViewGroup): View? {
        var view: View? = view
        if (view == null) {
            view = layoutInflater!!.inflate(android.R.layout.simple_list_item_1, null)
        }

        val notification = getItem(position)
        if (notification != null) {
            val textView: TextView = view!!.findViewById(android.R.id.text1)
            textView.text = String.format(
                    Locale.JAPAN,
                    "%d : %s (%d)",
                    notification.id,
                    notification.message,
                    notification.date
                )
        }
        return view
    }
}