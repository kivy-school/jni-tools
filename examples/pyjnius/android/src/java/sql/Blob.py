from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Blob"]

class Blob(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Blob"
    getBinaryStream = JavaMultipleMethod([("(JJ)Ljava/io/InputStream;", False, False), ("()Ljava/io/InputStream;", False, False)])
    setBytes = JavaMultipleMethod([("(J[B)I", False, False), ("(J[BII)I", False, False)])
    setBinaryStream = JavaMethod("(J)Ljava/io/OutputStream;")
    length = JavaMethod("()J")
    position = JavaMultipleMethod([("(Ljava/sql/Blob;J)J", False, False), ("([BJ)J", False, False)])
    getBytes = JavaMethod("(JI)[B")
    close = JavaMethod("()V")
    truncate = JavaMethod("(J)V")
    free = JavaMethod("()V")