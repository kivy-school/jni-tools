from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Locator2Impl"]

class Locator2Impl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/Locator2Impl"
    __javaconstructor__ = [("()V", False), ("(Lorg/xml/sax/Locator;)V", False)]
    getXMLVersion = JavaMethod("()Ljava/lang/String;")
    getEncoding = JavaMethod("()Ljava/lang/String;")
    setXMLVersion = JavaMethod("(Ljava/lang/String;)V")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")