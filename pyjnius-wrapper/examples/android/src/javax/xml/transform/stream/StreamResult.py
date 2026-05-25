from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamResult"]

class StreamResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/stream/StreamResult"
    __javaconstructor__ = [("()V", False), ("(Ljava/io/OutputStream;)V", False), ("(Ljava/io/Writer;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/io/File;)V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    setOutputStream = JavaMethod("(Ljava/io/OutputStream;)V")
    getOutputStream = JavaMethod("()Ljava/io/OutputStream;")
    setWriter = JavaMethod("(Ljava/io/Writer;)V")
    getWriter = JavaMethod("()Ljava/io/Writer;")
    setSystemId = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/io/File;)V", False, False)])
    getSystemId = JavaMethod("()Ljava/lang/String;")