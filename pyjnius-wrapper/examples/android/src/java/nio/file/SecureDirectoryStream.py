from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecureDirectoryStream"]

class SecureDirectoryStream(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/SecureDirectoryStream"
    newDirectoryStream = JavaMethod("(Ljava/lang/Object;[Ljava/nio/file/LinkOption;)Ljava/nio/file/SecureDirectoryStream;", varargs=True)
    newByteChannel = JavaMethod("(Ljava/lang/Object;Ljava/util/Set;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/channels/SeekableByteChannel;", varargs=True)
    deleteFile = JavaMethod("(Ljava/lang/Object;)V")
    deleteDirectory = JavaMethod("(Ljava/lang/Object;)V")
    move = JavaMethod("(Ljava/lang/Object;Ljava/nio/file/SecureDirectoryStream;Ljava/lang/Object;)V")
    getFileAttributeView = JavaMultipleMethod([("(Ljava/lang/Class;)Ljava/nio/file/attribute/FileAttributeView;", False, False), ("(Ljava/lang/Object;Ljava/lang/Class;[Ljava/nio/file/LinkOption;)Ljava/nio/file/attribute/FileAttributeView;", False, True)])