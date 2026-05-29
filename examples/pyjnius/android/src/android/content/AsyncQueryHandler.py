from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsyncQueryHandler"]

class AsyncQueryHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/AsyncQueryHandler"
    __javaconstructor__ = [("(Landroid/content/ContentResolver;)V", False)]
    cancelOperation = JavaMethod("(I)V")
    startDelete = JavaMethod("(ILjava/lang/Object;Landroid/net/Uri;Ljava/lang/String;[Ljava/lang/String;)V")
    startInsert = JavaMethod("(ILjava/lang/Object;Landroid/net/Uri;Landroid/content/ContentValues;)V")
    startQuery = JavaMethod("(ILjava/lang/Object;Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)V")
    startUpdate = JavaMethod("(ILjava/lang/Object;Landroid/net/Uri;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)V")
    handleMessage = JavaMethod("(Landroid/os/Message;)V")