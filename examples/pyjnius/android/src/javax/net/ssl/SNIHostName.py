from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SNIHostName"]

class SNIHostName(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SNIHostName"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("([B)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getAsciiName = JavaMethod("()Ljava/lang/String;")
    createSNIMatcher = JavaStaticMethod("(Ljava/lang/String;)Ljavax/net/ssl/SNIMatcher;")