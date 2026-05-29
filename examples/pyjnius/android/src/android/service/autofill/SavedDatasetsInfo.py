from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SavedDatasetsInfo"]

class SavedDatasetsInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/SavedDatasetsInfo"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False)]
    TYPE_OTHER = JavaStaticField("Ljava/lang/String;")
    TYPE_PASSWORDS = JavaStaticField("Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getCount = JavaMethod("()I")
    getType = JavaMethod("()Ljava/lang/String;")