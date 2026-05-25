from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Clob"]

class Clob(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Clob"
    length = JavaMethod("()J")
    getSubString = JavaMethod("(JI)Ljava/lang/String;")
    getCharacterStream = JavaMultipleMethod([("()Ljava/io/Reader;", False, False), ("(JJ)Ljava/io/Reader;", False, False)])
    getAsciiStream = JavaMethod("()Ljava/io/InputStream;")
    position = JavaMultipleMethod([("(Ljava/lang/String;J)J", False, False), ("(Ljava/sql/Clob;J)J", False, False)])
    setString = JavaMultipleMethod([("(JLjava/lang/String;)I", False, False), ("(JLjava/lang/String;II)I", False, False)])
    setAsciiStream = JavaMethod("(J)Ljava/io/OutputStream;")
    setCharacterStream = JavaMethod("(J)Ljava/io/Writer;")
    truncate = JavaMethod("(J)V")
    free = JavaMethod("()V")