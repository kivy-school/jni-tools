from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocatorImpl"]

class LocatorImpl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/helpers/LocatorImpl"
    __javaconstructor__ = [("()V", False), ("(Lorg/xml/sax/Locator;)V", False)]
    getPublicId = JavaMethod("()Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    getLineNumber = JavaMethod("()I")
    getColumnNumber = JavaMethod("()I")
    setPublicId = JavaMethod("(Ljava/lang/String;)V")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    setLineNumber = JavaMethod("(I)V")
    setColumnNumber = JavaMethod("(I)V")