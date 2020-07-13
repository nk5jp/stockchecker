package jp.nk5.stockchecker

import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper


class DBHelper private constructor(context: Context) : SQLiteOpenHelper(context, DB_NAME, null, DB_VERSION) {

    override fun onCreate(sqLiteDatabase: SQLiteDatabase) {
        sqLiteDatabase.execSQL(CREATE_NOTIFICATIONS_TABLE)
    }

    override fun onUpgrade(sqLiteDatabase: SQLiteDatabase, i: Int, i1: Int) {
        sqLiteDatabase.execSQL(DROP_NOTIFICATIONS_TABLE)
        sqLiteDatabase.execSQL(CREATE_NOTIFICATIONS_TABLE)
    }

    companion object {

        private var instance: DBHelper? = null
        private const val DB_NAME = "nk5_stockchecker.db"
        private const val DB_VERSION = 1

        private const val CREATE_NOTIFICATIONS_TABLE = "create table notifications ( " +
                "id integer primary key autoincrement, " +
                "date integer not null, " +
                "message text not null);"

        private const val DROP_NOTIFICATIONS_TABLE = "drop table notifications;"

        fun getInstance(context: Context): DBHelper {
            return instance ?: DBHelper(context)
        }
    }

}