from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsyncQueryHandler"]

class AsyncQueryHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/AsyncQueryHandler"
    __javaconstructor__ = [("(Landroid/content/ContentResolver;)V", False)]
    createHandler = JavaMethod("(Landroid/os/Looper;)Landroid/os/Handler;")
    startQuery = JavaMethod("(ILjava/lang/Object;Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)V")
    cancelOperation = JavaMethod("(I)V")
    startInsert = JavaMethod("(ILjava/lang/Object;Landroid/net/Uri;Landroid/content/ContentValues;)V")
    startUpdate = JavaMethod("(ILjava/lang/Object;Landroid/net/Uri;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)V")
    startDelete = JavaMethod("(ILjava/lang/Object;Landroid/net/Uri;Ljava/lang/String;[Ljava/lang/String;)V")
    onQueryComplete = JavaMethod("(ILjava/lang/Object;Landroid/database/Cursor;)V")
    onInsertComplete = JavaMethod("(ILjava/lang/Object;Landroid/net/Uri;)V")
    onUpdateComplete = JavaMethod("(ILjava/lang/Object;I)V")
    onDeleteComplete = JavaMethod("(ILjava/lang/Object;I)V")
    handleMessage = JavaMethod("(Landroid/os/Message;)V")

    class WorkerArgs(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/AsyncQueryHandler/WorkerArgs"
        __javaconstructor__ = [("()V", False)]
        cookie = JavaField("Ljava/lang/Object;")
        handler = JavaField("Landroid/os/Handler;")
        orderBy = JavaField("Ljava/lang/String;")
        projection = JavaField("[Ljava/lang/String;")
        result = JavaField("Ljava/lang/Object;")
        selection = JavaField("Ljava/lang/String;")
        selectionArgs = JavaField("[Ljava/lang/String;")
        uri = JavaField("Landroid/net/Uri;")
        values = JavaField("Landroid/content/ContentValues;")

    class WorkerHandler(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/AsyncQueryHandler/WorkerHandler"
        __javaconstructor__ = [("(Landroid/content/AsyncQueryHandler;Landroid/os/Looper;)V", False)]
        handleMessage = JavaMethod("(Landroid/os/Message;)V")