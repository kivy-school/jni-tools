from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputStreamReader"]

class InputStreamReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/InputStreamReader"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False), ("(Ljava/io/InputStream;Ljava/lang/String;)V", False), ("(Ljava/io/InputStream;Ljava/nio/charset/Charset;)V", False), ("(Ljava/io/InputStream;Ljava/nio/charset/CharsetDecoder;)V", False)]
    getEncoding = JavaMethod("()Ljava/lang/String;")
    read = JavaMultipleMethod([("(Ljava/nio/CharBuffer;)I", False, False), ("()I", False, False), ("([CII)I", False, False)])
    ready = JavaMethod("()Z")
    close = JavaMethod("()V")