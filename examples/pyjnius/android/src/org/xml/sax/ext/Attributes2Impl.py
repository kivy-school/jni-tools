from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Attributes2Impl"]

class Attributes2Impl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/Attributes2Impl"
    __javaconstructor__ = [("()V", False), ("(Lorg/xml/sax/Attributes;)V", False)]
    removeAttribute = JavaMethod("(I)V")
    setAttributes = JavaMethod("(Lorg/xml/sax/Attributes;)V")
    isSpecified = JavaMultipleMethod([("(Ljava/lang/String;)Z", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Z", False, False), ("(I)Z", False, False)])
    isDeclared = JavaMultipleMethod([("(I)Z", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Z", False, False), ("(Ljava/lang/String;)Z", False, False)])
    setDeclared = JavaMethod("(IZ)V")
    setSpecified = JavaMethod("(IZ)V")
    addAttribute = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")