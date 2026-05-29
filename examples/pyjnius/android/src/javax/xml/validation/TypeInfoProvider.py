from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TypeInfoProvider"]

class TypeInfoProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/validation/TypeInfoProvider"
    getElementTypeInfo = JavaMethod("()Lorg/w3c/dom/TypeInfo;")
    getAttributeTypeInfo = JavaMethod("(I)Lorg/w3c/dom/TypeInfo;")
    isIdAttribute = JavaMethod("(I)Z")
    isSpecified = JavaMethod("(I)Z")