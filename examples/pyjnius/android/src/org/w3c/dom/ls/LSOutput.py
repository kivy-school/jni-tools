from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LSOutput"]

class LSOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSOutput"
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setCharacterStream = JavaMethod("(Ljava/io/Writer;)V")
    getCharacterStream = JavaMethod("()Ljava/io/Writer;")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")
    getEncoding = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    setByteStream = JavaMethod("(Ljava/io/OutputStream;)V")
    getByteStream = JavaMethod("()Ljava/io/OutputStream;")