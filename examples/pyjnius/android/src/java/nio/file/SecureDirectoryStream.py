from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecureDirectoryStream"]

class SecureDirectoryStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/SecureDirectoryStream"
    deleteFile = JavaMethod("(Ljava/lang/Object;)V")
    getFileAttributeView = JavaMultipleMethod([("(Ljava/lang/Class;)Ljava/nio/file/attribute/FileAttributeView;", False, False), ("(Ljava/lang/Object;Ljava/lang/Class;[Ljava/nio/file/LinkOption;)Ljava/nio/file/attribute/FileAttributeView;", False, True)])
    move = JavaMethod("(Ljava/lang/Object;Ljava/nio/file/SecureDirectoryStream;Ljava/lang/Object;)V")
    newByteChannel = JavaMethod("(Ljava/lang/Object;Ljava/util/Set;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/channels/SeekableByteChannel;", varargs=True)
    newDirectoryStream = JavaMethod("(Ljava/lang/Object;[Ljava/nio/file/LinkOption;)Ljava/nio/file/SecureDirectoryStream;", varargs=True)
    deleteDirectory = JavaMethod("(Ljava/lang/Object;)V")