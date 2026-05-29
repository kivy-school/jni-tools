from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileInputStream"]

class FileInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FileInputStream"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/io/File;)V", False), ("(Ljava/io/FileDescriptor;)V", False)]
    read = JavaMultipleMethod([("()I", False, False), ("([B)I", False, False), ("([BII)I", False, False)])
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    close = JavaMethod("()V")
    getFD = JavaMethod("()Ljava/io/FileDescriptor;")
    getChannel = JavaMethod("()Ljava/nio/channels/FileChannel;")
    finalize = JavaMethod("()V")