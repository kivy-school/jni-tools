from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Attr"]

class Attr(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/Attr"
    getName = JavaMethod("()Ljava/lang/String;")
    getSpecified = JavaMethod("()Z")
    getValue = JavaMethod("()Ljava/lang/String;")
    setValue = JavaMethod("(Ljava/lang/String;)V")
    getOwnerElement = JavaMethod("()Lorg/w3c/dom/Element;")
    getSchemaTypeInfo = JavaMethod("()Lorg/w3c/dom/TypeInfo;")
    isId = JavaMethod("()Z")