from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TypeInfo"]

class TypeInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/TypeInfo"
    DERIVATION_RESTRICTION = JavaStaticField("I")
    DERIVATION_EXTENSION = JavaStaticField("I")
    DERIVATION_UNION = JavaStaticField("I")
    DERIVATION_LIST = JavaStaticField("I")
    getTypeName = JavaMethod("()Ljava/lang/String;")
    getTypeNamespace = JavaMethod("()Ljava/lang/String;")
    isDerivedFrom = JavaMethod("(Ljava/lang/String;Ljava/lang/String;I)Z")