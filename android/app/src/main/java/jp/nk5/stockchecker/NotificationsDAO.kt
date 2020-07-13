package jp.nk5.stockchecker

import android.content.ContentValues
import android.content.Context
import android.database.Cursor


class NotificationsDAO(context: Context) : DAO<MyNotification>(context) {

    @Throws(Exception::class)
    fun createNotification (notification: MyNotification)
    {
        create (notification, "notifications")
    }

    @Throws(Exception::class)
    fun getAll(): List<MyNotification>
    {
        return read("select * from notifications order by id DESC;", null)
    }

    @Throws(Exception::class)
    override fun transformCursorToEntity(cursor: Cursor): MyNotification {

        val id = cursor.getInt(cursor.getColumnIndex("id"))
        val date = cursor.getInt(cursor.getColumnIndex("date"))
        val message = cursor.getString(cursor.getColumnIndex("message"))

        return MyNotification(id, date, message)
    }

    override fun transformEntityToValues(entity: MyNotification): ContentValues {
        val values = ContentValues()
        values.put("date", entity.date)
        values.put("message", entity.message)
        return values
    }

    override fun updateEntityById(entity: MyNotification, rowId: Long) {
        entity.id = rowId.toInt()
    }
}