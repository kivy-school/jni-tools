from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentQueryMap"]

class ContentQueryMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ContentQueryMap"
    __javaconstructor__ = [("(Landroid/database/Cursor;Ljava/lang/String;ZLandroid/os/Handler;)V", False)]
    setKeepUpdated = JavaMethod("(Z)V")
    getValues = JavaMethod("(Ljava/lang/String;)Landroid/content/ContentValues;")
    requery = JavaMethod("()V")
    getRows = JavaMethod("()Ljava/util/Map;")
    close = JavaMethod("()V")
    finalize = JavaMethod("()V")