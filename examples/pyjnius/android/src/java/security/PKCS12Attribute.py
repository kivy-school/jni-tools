from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PKCS12Attribute"]

class PKCS12Attribute(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PKCS12Attribute"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("([B)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getValue = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMethod("()[B")