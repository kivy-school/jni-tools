from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileOutputStream"]

class FileOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FileOutputStream"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Z)V", False), ("(Ljava/io/File;)V", False), ("(Ljava/io/File;Z)V", False), ("(Ljava/io/FileDescriptor;)V", False)]
    write = JavaMultipleMethod([("(I)V", False, False), ("([B)V", False, False), ("([BII)V", False, False)])
    close = JavaMethod("()V")
    getFD = JavaMethod("()Ljava/io/FileDescriptor;")
    getChannel = JavaMethod("()Ljava/nio/channels/FileChannel;")
    finalize = JavaMethod("()V")