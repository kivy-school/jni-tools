from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PKCS12Attribute"]

class PKCS12Attribute(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PKCS12Attribute"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("([B)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    getValue = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")