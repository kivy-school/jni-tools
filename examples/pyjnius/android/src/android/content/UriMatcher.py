from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UriMatcher"]

class UriMatcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/UriMatcher"
    __javaconstructor__ = [("(I)V", False)]
    NO_MATCH = JavaStaticField("I")
    match = JavaMethod("(Landroid/net/Uri;)I")
    addURI = JavaMethod("(Ljava/lang/String;Ljava/lang/String;I)V")