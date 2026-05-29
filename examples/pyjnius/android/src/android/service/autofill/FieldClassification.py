from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FieldClassification"]

class FieldClassification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/FieldClassification"
    getMatches = JavaMethod("()Ljava/util/List;")
    toString = JavaMethod("()Ljava/lang/String;")

    class Match(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/FieldClassification$Match"
        getCategoryId = JavaMethod("()Ljava/lang/String;")
        toString = JavaMethod("()Ljava/lang/String;")
        getScore = JavaMethod("()F")