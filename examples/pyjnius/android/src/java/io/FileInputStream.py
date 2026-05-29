from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileInputStream"]

class FileInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FileInputStream"
    __javaconstructor__ = [("(Ljava/io/FileDescriptor;)V", False), ("(Ljava/io/File;)V", False), ("(Ljava/lang/String;)V", False)]
    close = JavaMethod("()V")
    readAllBytes = JavaMethod("()[B")
    read = JavaMultipleMethod([("([BII)I", False, False), ("([B)I", False, False), ("()I", False, False)])
    readNBytes = JavaMethod("(I)[B")
    transferTo = JavaMethod("(Ljava/io/OutputStream;)J")
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    getChannel = JavaMethod("()Ljava/nio/channels/FileChannel;")
    getFD = JavaMethod("()Ljava/io/FileDescriptor;")