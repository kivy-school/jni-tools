from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentUris"]

class ContentUris(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ContentUris"
    __javaconstructor__ = [("()V", False)]
    removeId = JavaStaticMethod("(Landroid/net/Uri;)Landroid/net/Uri;")
    parseId = JavaStaticMethod("(Landroid/net/Uri;)J")
    withAppendedId = JavaStaticMethod("(Landroid/net/Uri;J)Landroid/net/Uri;")
    appendId = JavaStaticMethod("(Landroid/net/Uri$Builder;J)Landroid/net/Uri$Builder;")