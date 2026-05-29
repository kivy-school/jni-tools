from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TypeInfo"]

class TypeInfo(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/TypeInfo"
    DERIVATION_EXTENSION = JavaStaticField("I")
    DERIVATION_LIST = JavaStaticField("I")
    DERIVATION_RESTRICTION = JavaStaticField("I")
    DERIVATION_UNION = JavaStaticField("I")
    getTypeName = JavaMethod("()Ljava/lang/String;")
    getTypeNamespace = JavaMethod("()Ljava/lang/String;")
    isDerivedFrom = JavaMethod("(Ljava/lang/String;Ljava/lang/String;I)Z")