from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class QName(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/namespace/QName"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljavax/xml/namespace/QName;")
    getPrefix = JavaMethod("()Ljava/lang/String;")
    getNamespaceURI = JavaMethod("()Ljava/lang/String;")
    getLocalPart = JavaMethod("()Ljava/lang/String;")

class NamespaceContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/namespace/NamespaceContext"
    getPrefixes = JavaMethod("(Ljava/lang/String;)Ljava/util/Iterator;")
    getPrefix = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getNamespaceURI = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")