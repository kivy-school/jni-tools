from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URICertStoreParameters"]

class URICertStoreParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/URICertStoreParameters"
    __javaconstructor__ = [("(Ljava/net/URI;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Ljava/security/cert/URICertStoreParameters;", False, False), ("()Ljava/lang/Object;", False, False)])
    getURI = JavaMethod("()Ljava/net/URI;")