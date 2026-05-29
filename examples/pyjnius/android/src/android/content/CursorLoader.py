from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CursorLoader"]

class CursorLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/CursorLoader"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)V", False)]
    loadInBackground = JavaMethod("()Landroid/database/Cursor;")
    cancelLoadInBackground = JavaMethod("()V")
    deliverResult = JavaMethod("(Landroid/database/Cursor;)V")
    onStartLoading = JavaMethod("()V")
    onStopLoading = JavaMethod("()V")
    onCanceled = JavaMethod("(Landroid/database/Cursor;)V")
    onReset = JavaMethod("()V")
    getUri = JavaMethod("()Landroid/net/Uri;")
    setUri = JavaMethod("(Landroid/net/Uri;)V")
    getProjection = JavaMethod("()[Ljava/lang/String;")
    setProjection = JavaMethod("([Ljava/lang/String;)V")
    getSelection = JavaMethod("()Ljava/lang/String;")
    setSelection = JavaMethod("(Ljava/lang/String;)V")
    getSelectionArgs = JavaMethod("()[Ljava/lang/String;")
    setSelectionArgs = JavaMethod("([Ljava/lang/String;)V")
    getSortOrder = JavaMethod("()Ljava/lang/String;")
    setSortOrder = JavaMethod("(Ljava/lang/String;)V")
    dump = JavaMethod("(Ljava/lang/String;Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")