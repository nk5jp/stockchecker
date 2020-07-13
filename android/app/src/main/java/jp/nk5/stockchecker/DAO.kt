package jp.nk5.stockchecker

import android.content.ContentValues
import android.content.Context
import android.database.Cursor

import java.util.ArrayList

abstract class DAO<T> internal constructor(private val context: Context) {

    @Throws(Exception::class)
    internal fun create(entity: T, tableName: String) {
        val contentValues = transformEntityToValues(entity)

        DBHelper.getInstance(context).writableDatabase.use { db ->
            val rowId = db.insert(tableName, null, contentValues)
            if (rowId == -1L) {
                throw Exception()
            } else {
                updateEntityById(entity, rowId)
            }
        }
    }

    @Throws(Exception::class)
    internal fun read(selectQuery: String, args: Array<String>?): List<T> {
        val list = ArrayList<T>()

        DBHelper.getInstance(context).writableDatabase.use { db ->
            db.rawQuery(selectQuery, args).use { cursor ->
                if (cursor.moveToFirst()) {
                    do {
                        val entity = transformCursorToEntity(cursor)
                        list.add(entity)
                    } while (cursor.moveToNext())
                }
                return list
            }
        }
    }

    @Throws(Exception::class)
    internal fun update(entity: T, tableName: String, condition: String, args: Array<String>?) {
        val contentValues = transformEntityToValues(entity)
        DBHelper.getInstance(context).writableDatabase.use { db ->
            db.beginTransaction()
            val updateRow = db.update(tableName, contentValues, condition, args).toLong()
            if (updateRow == -1L) {
                throw Exception()
            } else {
                db.setTransactionSuccessful()
            }
            db.endTransaction()
        }
    }

    @Throws(Exception::class)
    fun delete(tableName: String, condition: String, args: Array<String>?) {
        DBHelper.getInstance(context).writableDatabase.use { db ->
            db.beginTransaction()
            val deleteRaw = db.delete(tableName, condition, args).toLong()
            if (deleteRaw == -1L) {
                throw Exception()
            } else {
                db.setTransactionSuccessful()
            }
            db.endTransaction()
        }
    }

    @Throws(Exception::class)
    internal abstract fun transformCursorToEntity(cursor: Cursor): T

    @Throws(Exception::class)
    internal abstract fun transformEntityToValues(entity: T): ContentValues

    @Throws(Exception::class)
    internal abstract fun updateEntityById(entity: T, rowId: Long)

}