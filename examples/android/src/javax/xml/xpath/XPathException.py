from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XPathException"]

class XPathException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False)]
    getCause = JavaMethod("()Ljava/lang/Throwable;")
    printStackTrace = JavaMultipleMethod([("(Ljava/io/PrintStream;)V", False, False), ("()V", False, False), ("(Ljava/io/PrintWriter;)V", False, False)])