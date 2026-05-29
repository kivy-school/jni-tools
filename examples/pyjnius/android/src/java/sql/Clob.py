from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Clob"]

class Clob(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Clob"
    setAsciiStream = JavaMethod("(J)Ljava/io/OutputStream;")
    setCharacterStream = JavaMethod("(J)Ljava/io/Writer;")
    getCharacterStream = JavaMultipleMethod([("(JJ)Ljava/io/Reader;", False, False), ("()Ljava/io/Reader;", False, False)])
    getSubString = JavaMethod("(JI)Ljava/lang/String;")
    getAsciiStream = JavaMethod("()Ljava/io/InputStream;")
    length = JavaMethod("()J")
    position = JavaMultipleMethod([("(Ljava/sql/Clob;J)J", False, False), ("(Ljava/lang/String;J)J", False, False)])
    close = JavaMethod("()V")
    setString = JavaMultipleMethod([("(JLjava/lang/String;)I", False, False), ("(JLjava/lang/String;II)I", False, False)])
    truncate = JavaMethod("(J)V")
    free = JavaMethod("()V")