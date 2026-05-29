from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzev"]

class zzev(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzev"
    __javaconstructor__ = [("()V", False)]
    attachInfo = JavaMethod("(Landroid/content/Context;Landroid/content/pm/ProviderInfo;)V")
    onCreate = JavaMethod("()Z")
    query = JavaMethod("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;")
    getType = JavaMethod("(Landroid/net/Uri;)Ljava/lang/String;")
    insert = JavaMethod("(Landroid/net/Uri;Landroid/content/ContentValues;)Landroid/net/Uri;")
    delete = JavaMethod("(Landroid/net/Uri;Ljava/lang/String;[Ljava/lang/String;)I")
    update = JavaMethod("(Landroid/net/Uri;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I")