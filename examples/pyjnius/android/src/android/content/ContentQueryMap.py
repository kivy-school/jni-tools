from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentQueryMap"]

class ContentQueryMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ContentQueryMap"
    __javaconstructor__ = [("(Landroid/database/Cursor;Ljava/lang/String;ZLandroid/os/Handler;)V", False)]
    close = JavaMethod("()V")
    requery = JavaMethod("()V")
    getValues = JavaMethod("(Ljava/lang/String;)Landroid/content/ContentValues;")
    getRows = JavaMethod("()Ljava/util/Map;")
    setKeepUpdated = JavaMethod("(Z)V")