from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClearCredentialStateException"]

class ClearCredentialStateException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/ClearCredentialStateException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False)]
    TYPE_UNKNOWN = JavaStaticField("Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")