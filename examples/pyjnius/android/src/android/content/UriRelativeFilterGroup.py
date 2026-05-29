from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UriRelativeFilterGroup"]

class UriRelativeFilterGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/UriRelativeFilterGroup"
    __javaconstructor__ = [("(I)V", False)]
    ACTION_ALLOW = JavaStaticField("I")
    ACTION_BLOCK = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    matchData = JavaMethod("(Landroid/net/Uri;)Z")
    getAction = JavaMethod("()I")
    addUriRelativeFilter = JavaMethod("(Landroid/content/UriRelativeFilter;)V")
    getUriRelativeFilters = JavaMethod("()Ljava/util/Collection;")