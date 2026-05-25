from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["QName"]

class QName(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/namespace/QName"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False)]
    getNamespaceURI = JavaMethod("()Ljava/lang/String;")
    getLocalPart = JavaMethod("()Ljava/lang/String;")
    getPrefix = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljavax/xml/namespace/QName;")