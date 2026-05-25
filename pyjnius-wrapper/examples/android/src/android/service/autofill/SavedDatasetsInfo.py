from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SavedDatasetsInfo"]

class SavedDatasetsInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/SavedDatasetsInfo"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False)]
    TYPE_OTHER = JavaStaticField("Ljava/lang/String;")
    TYPE_PASSWORDS = JavaStaticField("Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")
    getCount = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")