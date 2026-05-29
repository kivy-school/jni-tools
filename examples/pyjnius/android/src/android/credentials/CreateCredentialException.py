from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CreateCredentialException"]

class CreateCredentialException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/CreateCredentialException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False)]
    TYPE_INTERRUPTED = JavaStaticField("Ljava/lang/String;")
    TYPE_NO_CREATE_OPTIONS = JavaStaticField("Ljava/lang/String;")
    TYPE_UNKNOWN = JavaStaticField("Ljava/lang/String;")
    TYPE_USER_CANCELED = JavaStaticField("Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")