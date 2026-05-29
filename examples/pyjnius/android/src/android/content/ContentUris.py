from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentUris"]

class ContentUris(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ContentUris"
    __javaconstructor__ = [("()V", False)]
    parseId = JavaStaticMethod("(Landroid/net/Uri;)J")
    appendId = JavaStaticMethod("(Landroid/net/Uri$Builder;J)Landroid/net/Uri$Builder;")
    withAppendedId = JavaStaticMethod("(Landroid/net/Uri;J)Landroid/net/Uri;")
    removeId = JavaStaticMethod("(Landroid/net/Uri;)Landroid/net/Uri;")