from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class StreamSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/stream/StreamSource"
    __javaconstructor__ = [("(Ljava/io/Reader;Ljava/lang/String;)V", False), ("()V", False), ("(Ljava/io/InputStream;Ljava/lang/String;)V", False), ("(Ljava/io/InputStream;)V", False), ("(Ljava/io/Reader;)V", False), ("(Ljava/io/File;)V", False), ("(Ljava/lang/String;)V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    getReader = JavaMethod("()Ljava/io/Reader;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMultipleMethod([("(Ljava/io/File;)V", False, False), ("(Ljava/lang/String;)V", False, False)])
    getPublicId = JavaMethod("()Ljava/lang/String;")
    setInputStream = JavaMethod("(Ljava/io/InputStream;)V")
    setReader = JavaMethod("(Ljava/io/Reader;)V")
    setPublicId = JavaMethod("(Ljava/lang/String;)V")
    isEmpty = JavaMethod("()Z")
    getInputStream = JavaMethod("()Ljava/io/InputStream;")

class StreamResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/stream/StreamResult"
    __javaconstructor__ = [("()V", False), ("(Ljava/io/Writer;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/io/File;)V", False), ("(Ljava/io/OutputStream;)V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    PI_DISABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    PI_ENABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    getOutputStream = JavaMethod("()Ljava/io/OutputStream;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/io/File;)V", False, False)])
    setWriter = JavaMethod("(Ljava/io/Writer;)V")
    getWriter = JavaMethod("()Ljava/io/Writer;")
    setOutputStream = JavaMethod("(Ljava/io/OutputStream;)V")