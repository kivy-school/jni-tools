from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLXML"]

class SQLXML(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/SQLXML"
    free = JavaMethod("()V")
    getBinaryStream = JavaMethod("()Ljava/io/InputStream;")
    setBinaryStream = JavaMethod("()Ljava/io/OutputStream;")
    getCharacterStream = JavaMethod("()Ljava/io/Reader;")
    setCharacterStream = JavaMethod("()Ljava/io/Writer;")
    getString = JavaMethod("()Ljava/lang/String;")
    setString = JavaMethod("(Ljava/lang/String;)V")
    getSource = JavaMethod("(Ljava/lang/Class;)Ljavax/xml/transform/Source;")
    setResult = JavaMethod("(Ljava/lang/Class;)Ljavax/xml/transform/Result;")