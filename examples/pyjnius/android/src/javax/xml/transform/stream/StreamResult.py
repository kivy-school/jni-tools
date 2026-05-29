from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamResult"]

class StreamResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/stream/StreamResult"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/io/File;)V", False), ("()V", False), ("(Ljava/io/Writer;)V", False), ("(Ljava/io/OutputStream;)V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    PI_DISABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    PI_ENABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    getOutputStream = JavaMethod("()Ljava/io/OutputStream;")
    setSystemId = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/io/File;)V", False, False)])
    setWriter = JavaMethod("(Ljava/io/Writer;)V")
    getWriter = JavaMethod("()Ljava/io/Writer;")
    setOutputStream = JavaMethod("(Ljava/io/OutputStream;)V")