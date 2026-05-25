from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamSource"]

class StreamSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/stream/StreamSource"
    __javaconstructor__ = [("()V", False), ("(Ljava/io/InputStream;)V", False), ("(Ljava/io/InputStream;Ljava/lang/String;)V", False), ("(Ljava/io/Reader;)V", False), ("(Ljava/io/Reader;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/io/File;)V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    setInputStream = JavaMethod("(Ljava/io/InputStream;)V")
    getInputStream = JavaMethod("()Ljava/io/InputStream;")
    setReader = JavaMethod("(Ljava/io/Reader;)V")
    getReader = JavaMethod("()Ljava/io/Reader;")
    setPublicId = JavaMethod("(Ljava/lang/String;)V")
    getPublicId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/io/File;)V", False, False)])
    getSystemId = JavaMethod("()Ljava/lang/String;")