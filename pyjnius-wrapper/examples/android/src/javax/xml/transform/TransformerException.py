from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransformerException"]

class TransformerException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/TransformerException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljavax/xml/transform/SourceLocator;)V", False), ("(Ljava/lang/String;Ljavax/xml/transform/SourceLocator;Ljava/lang/Throwable;)V", False)]
    getLocator = JavaMethod("()Ljavax/xml/transform/SourceLocator;")
    setLocator = JavaMethod("(Ljavax/xml/transform/SourceLocator;)V")
    getException = JavaMethod("()Ljava/lang/Throwable;")
    getCause = JavaMethod("()Ljava/lang/Throwable;")
    initCause = JavaMethod("(Ljava/lang/Throwable;)Ljava/lang/Throwable;")
    getMessageAndLocation = JavaMethod("()Ljava/lang/String;")
    getLocationAsString = JavaMethod("()Ljava/lang/String;")
    printStackTrace = JavaMultipleMethod([("()V", False, False), ("(Ljava/io/PrintStream;)V", False, False), ("(Ljava/io/PrintWriter;)V", False, False)])