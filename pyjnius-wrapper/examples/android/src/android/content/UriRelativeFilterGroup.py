from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UriRelativeFilterGroup"]

class UriRelativeFilterGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/UriRelativeFilterGroup"
    __javaconstructor__ = [("(I)V", False)]
    ACTION_ALLOW = JavaStaticField("I")
    ACTION_BLOCK = JavaStaticField("I")
    getAction = JavaMethod("()I")
    addUriRelativeFilter = JavaMethod("(Landroid/content/UriRelativeFilter;)V")
    getUriRelativeFilters = JavaMethod("()Ljava/util/Collection;")
    matchData = JavaMethod("(Landroid/net/Uri;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")