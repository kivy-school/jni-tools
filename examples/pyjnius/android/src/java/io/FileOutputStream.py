from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileOutputStream"]

class FileOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FileOutputStream"
    __javaconstructor__ = [("(Ljava/io/FileDescriptor;)V", False), ("(Ljava/io/File;Z)V", False), ("(Ljava/io/File;)V", False), ("(Ljava/lang/String;Z)V", False), ("(Ljava/lang/String;)V", False)]
    close = JavaMethod("()V")
    write = JavaMultipleMethod([("([BII)V", False, False), ("(I)V", False, False), ("([B)V", False, False)])
    getChannel = JavaMethod("()Ljava/nio/channels/FileChannel;")
    getFD = JavaMethod("()Ljava/io/FileDescriptor;")