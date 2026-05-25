from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UriRelativeFilter"]

class UriRelativeFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/UriRelativeFilter"
    __javaconstructor__ = [("(IILjava/lang/String;)V", False)]
    FRAGMENT = JavaStaticField("I")
    PATH = JavaStaticField("I")
    QUERY = JavaStaticField("I")
    getUriPart = JavaMethod("()I")
    getPatternType = JavaMethod("()I")
    getFilter = JavaMethod("()Ljava/lang/String;")
    matchData = JavaMethod("(Landroid/net/Uri;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")