from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocatorImpl"]

class LocatorImpl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/helpers/LocatorImpl"
    __javaconstructor__ = [("(Lorg/xml/sax/Locator;)V", False), ("()V", False)]
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getColumnNumber = JavaMethod("()I")
    getPublicId = JavaMethod("()Ljava/lang/String;")
    setPublicId = JavaMethod("(Ljava/lang/String;)V")
    setColumnNumber = JavaMethod("(I)V")
    setLineNumber = JavaMethod("(I)V")
    getLineNumber = JavaMethod("()I")