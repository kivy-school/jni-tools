from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputSource"]

class InputSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/InputSource"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/io/InputStream;)V", False), ("(Ljava/io/Reader;)V", False)]
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setCharacterStream = JavaMethod("(Ljava/io/Reader;)V")
    getCharacterStream = JavaMethod("()Ljava/io/Reader;")
    isEmpty = JavaMethod("()Z")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")
    getEncoding = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getPublicId = JavaMethod("()Ljava/lang/String;")
    setPublicId = JavaMethod("(Ljava/lang/String;)V")
    setByteStream = JavaMethod("(Ljava/io/InputStream;)V")
    getByteStream = JavaMethod("()Ljava/io/InputStream;")