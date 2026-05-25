from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CloseHelper"]

class CloseHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/shortcutbadger/util/CloseHelper"
    __javaconstructor__ = [("()V", False)]
    close = JavaStaticMethod("(Landroid/database/Cursor;)V")
    closeQuietly = JavaStaticMethod("(Ljava/io/Closeable;)V")