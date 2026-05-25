from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Manifest"]

class Manifest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/jar/Manifest"
    __javaconstructor__ = [("()V", False), ("(Ljava/io/InputStream;)V", False), ("(Ljava/util/jar/Manifest;)V", False)]
    getMainAttributes = JavaMethod("()Ljava/util/jar/Attributes;")
    getEntries = JavaMethod("()Ljava/util/Map;")
    getAttributes = JavaMethod("(Ljava/lang/String;)Ljava/util/jar/Attributes;")
    clear = JavaMethod("()V")
    write = JavaMethod("(Ljava/io/OutputStream;)V")
    read = JavaMethod("(Ljava/io/InputStream;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")