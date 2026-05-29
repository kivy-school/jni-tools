from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputSource"]

class InputSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/InputSource"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/io/InputStream;)V", False), ("(Ljava/io/Reader;)V", False)]
    setPublicId = JavaMethod("(Ljava/lang/String;)V")
    getPublicId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setByteStream = JavaMethod("(Ljava/io/InputStream;)V")
    getByteStream = JavaMethod("()Ljava/io/InputStream;")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")
    getEncoding = JavaMethod("()Ljava/lang/String;")
    setCharacterStream = JavaMethod("(Ljava/io/Reader;)V")
    getCharacterStream = JavaMethod("()Ljava/io/Reader;")