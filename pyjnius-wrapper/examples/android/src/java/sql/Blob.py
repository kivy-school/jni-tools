from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Blob"]

class Blob(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Blob"
    length = JavaMethod("()J")
    getBytes = JavaMethod("(JI)[B")
    getBinaryStream = JavaMultipleMethod([("()Ljava/io/InputStream;", False, False), ("(JJ)Ljava/io/InputStream;", False, False)])
    position = JavaMultipleMethod([("([BJ)J", False, False), ("(Ljava/sql/Blob;J)J", False, False)])
    setBytes = JavaMultipleMethod([("(J[B)I", False, False), ("(J[BII)I", False, False)])
    setBinaryStream = JavaMethod("(J)Ljava/io/OutputStream;")
    truncate = JavaMethod("(J)V")
    free = JavaMethod("()V")