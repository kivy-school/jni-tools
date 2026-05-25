from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SNIHostName"]

class SNIHostName(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SNIHostName"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("([B)V", False)]
    getAsciiName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    createSNIMatcher = JavaStaticMethod("(Ljava/lang/String;)Ljavax/net/ssl/SNIMatcher;")