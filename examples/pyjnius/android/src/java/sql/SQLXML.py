from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLXML"]

class SQLXML(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/SQLXML"
    getBinaryStream = JavaMethod("()Ljava/io/InputStream;")
    setBinaryStream = JavaMethod("()Ljava/io/OutputStream;")
    setCharacterStream = JavaMethod("()Ljava/io/Writer;")
    getCharacterStream = JavaMethod("()Ljava/io/Reader;")
    close = JavaMethod("()V")
    setString = JavaMethod("(Ljava/lang/String;)V")
    setResult = JavaMethod("(Ljava/lang/Class;)Ljavax/xml/transform/Result;")
    getString = JavaMethod("()Ljava/lang/String;")
    getSource = JavaMethod("(Ljava/lang/Class;)Ljavax/xml/transform/Source;")
    free = JavaMethod("()V")