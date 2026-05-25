from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LSOutput"]

class LSOutput(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSOutput"
    getCharacterStream = JavaMethod("()Ljava/io/Writer;")
    setCharacterStream = JavaMethod("(Ljava/io/Writer;)V")
    getByteStream = JavaMethod("()Ljava/io/OutputStream;")
    setByteStream = JavaMethod("(Ljava/io/OutputStream;)V")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getEncoding = JavaMethod("()Ljava/lang/String;")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")