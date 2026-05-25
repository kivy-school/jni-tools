from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OneSignalDb"]

class OneSignalDb(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OneSignalDb"
    query = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;", False, False), ("(Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;", False, False)])
    insert = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/content/ContentValues;)V")
    insertOrThrow = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/content/ContentValues;)V")
    update = JavaMethod("(Ljava/lang/String;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I")
    delete = JavaMethod("(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;)V")