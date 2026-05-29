from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XPathException"]

class XPathException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False)]
    printStackTrace = JavaMultipleMethod([("(Ljava/io/PrintWriter;)V", False, False), ("(Ljava/io/PrintStream;)V", False, False), ("()V", False, False)])
    getCause = JavaMethod("()Ljava/lang/Throwable;")