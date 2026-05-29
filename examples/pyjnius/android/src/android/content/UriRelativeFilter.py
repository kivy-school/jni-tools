from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UriRelativeFilter"]

class UriRelativeFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/UriRelativeFilter"
    __javaconstructor__ = [("(IILjava/lang/String;)V", False)]
    FRAGMENT = JavaStaticField("I")
    PATH = JavaStaticField("I")
    QUERY = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getUriPart = JavaMethod("()I")
    getPatternType = JavaMethod("()I")
    matchData = JavaMethod("(Landroid/net/Uri;)Z")
    getFilter = JavaMethod("()Ljava/lang/String;")