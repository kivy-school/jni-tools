from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Attributes2Impl"]

class Attributes2Impl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/Attributes2Impl"
    __javaconstructor__ = [("()V", False), ("(Lorg/xml/sax/Attributes;)V", False)]
    isDeclared = JavaMultipleMethod([("(I)Z", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Z", False, False), ("(Ljava/lang/String;)Z", False, False)])
    isSpecified = JavaMultipleMethod([("(I)Z", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Z", False, False), ("(Ljava/lang/String;)Z", False, False)])
    setAttributes = JavaMethod("(Lorg/xml/sax/Attributes;)V")
    addAttribute = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    removeAttribute = JavaMethod("(I)V")
    setDeclared = JavaMethod("(IZ)V")
    setSpecified = JavaMethod("(IZ)V")