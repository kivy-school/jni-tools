from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransformerException"]

class TransformerException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/TransformerException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljavax/xml/transform/SourceLocator;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljavax/xml/transform/SourceLocator;)V", False)]
    printStackTrace = JavaMultipleMethod([("(Ljava/io/PrintStream;)V", False, False), ("(Ljava/io/PrintWriter;)V", False, False), ("()V", False, False)])
    getCause = JavaMethod("()Ljava/lang/Throwable;")
    initCause = JavaMethod("(Ljava/lang/Throwable;)Ljava/lang/Throwable;")
    getException = JavaMethod("()Ljava/lang/Throwable;")
    getLocationAsString = JavaMethod("()Ljava/lang/String;")
    getLocator = JavaMethod("()Ljavax/xml/transform/SourceLocator;")
    setLocator = JavaMethod("(Ljavax/xml/transform/SourceLocator;)V")
    getMessageAndLocation = JavaMethod("()Ljava/lang/String;")