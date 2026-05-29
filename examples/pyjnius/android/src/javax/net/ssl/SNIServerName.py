from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SNIServerName"]

class SNIServerName(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SNIServerName"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getType = JavaMethod("()I")
    getEncoded = JavaMethod("()[B")