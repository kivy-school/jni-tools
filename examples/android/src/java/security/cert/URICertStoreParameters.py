from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URICertStoreParameters"]

class URICertStoreParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/URICertStoreParameters"
    __javaconstructor__ = [("(Ljava/net/URI;)V", False)]
    getURI = JavaMethod("()Ljava/net/URI;")
    clone = JavaMethod("()Ljava/security/cert/URICertStoreParameters;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")