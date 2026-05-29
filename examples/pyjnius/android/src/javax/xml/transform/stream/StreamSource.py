from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamSource"]

class StreamSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/stream/StreamSource"
    __javaconstructor__ = [("(Ljava/io/File;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False), ("(Ljava/io/InputStream;)V", False), ("(Ljava/io/InputStream;Ljava/lang/String;)V", False), ("(Ljava/io/Reader;)V", False), ("(Ljava/io/Reader;Ljava/lang/String;)V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    getReader = JavaMethod("()Ljava/io/Reader;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    isEmpty = JavaMethod("()Z")
    getInputStream = JavaMethod("()Ljava/io/InputStream;")
    setSystemId = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/io/File;)V", False, False)])
    getPublicId = JavaMethod("()Ljava/lang/String;")
    setInputStream = JavaMethod("(Ljava/io/InputStream;)V")
    setReader = JavaMethod("(Ljava/io/Reader;)V")
    setPublicId = JavaMethod("(Ljava/lang/String;)V")