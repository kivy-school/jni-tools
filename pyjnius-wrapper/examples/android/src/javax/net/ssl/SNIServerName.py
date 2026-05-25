from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SNIServerName"]

class SNIServerName(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SNIServerName"
    __javaconstructor__ = [("(I[B)V", False)]
    getType = JavaMethod("()I")
    getEncoded = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")