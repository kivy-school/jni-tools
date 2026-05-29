from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HttpRetryException"]

class HttpRetryException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/HttpRetryException"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False), ("(Ljava/lang/String;ILjava/lang/String;)V", False)]
    getLocation = JavaMethod("()Ljava/lang/String;")
    responseCode = JavaMethod("()I")
    getReason = JavaMethod("()Ljava/lang/String;")