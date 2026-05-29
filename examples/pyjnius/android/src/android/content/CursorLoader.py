from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CursorLoader"]

class CursorLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/CursorLoader"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)V", False)]
    dump = JavaMethod("(Ljava/lang/String;Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")
    setSelection = JavaMethod("(Ljava/lang/String;)V")
    getUri = JavaMethod("()Landroid/net/Uri;")
    getProjection = JavaMethod("()[Ljava/lang/String;")
    getSelection = JavaMethod("()Ljava/lang/String;")
    getSelectionArgs = JavaMethod("()[Ljava/lang/String;")
    getSortOrder = JavaMethod("()Ljava/lang/String;")
    setProjection = JavaMethod("([Ljava/lang/String;)V")
    setSelectionArgs = JavaMethod("([Ljava/lang/String;)V")
    setSortOrder = JavaMethod("(Ljava/lang/String;)V")
    setUri = JavaMethod("(Landroid/net/Uri;)V")
    loadInBackground = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/database/Cursor;", False, False)])
    cancelLoadInBackground = JavaMethod("()V")
    onCanceled = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Landroid/database/Cursor;)V", False, False)])
    deliverResult = JavaMultipleMethod([("(Landroid/database/Cursor;)V", False, False), ("(Ljava/lang/Object;)V", False, False)])