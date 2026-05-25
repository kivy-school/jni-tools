from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileSystemProvider"]

class FileSystemProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/spi/FileSystemProvider"
    __javaconstructor__ = [("()V", False)]
    installedProviders = JavaStaticMethod("()Ljava/util/List;")
    getScheme = JavaMethod("()Ljava/lang/String;")
    newFileSystem = JavaMultipleMethod([("(Ljava/net/URI;Ljava/util/Map;)Ljava/nio/file/FileSystem;", False, False), ("(Ljava/nio/file/Path;Ljava/util/Map;)Ljava/nio/file/FileSystem;", False, False)])
    getFileSystem = JavaMethod("(Ljava/net/URI;)Ljava/nio/file/FileSystem;")
    getPath = JavaMethod("(Ljava/net/URI;)Ljava/nio/file/Path;")
    newInputStream = JavaMethod("(Ljava/nio/file/Path;[Ljava/nio/file/OpenOption;)Ljava/io/InputStream;", varargs=True)
    newOutputStream = JavaMethod("(Ljava/nio/file/Path;[Ljava/nio/file/OpenOption;)Ljava/io/OutputStream;", varargs=True)
    newFileChannel = JavaMethod("(Ljava/nio/file/Path;Ljava/util/Set;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/channels/FileChannel;", varargs=True)
    newAsynchronousFileChannel = JavaMethod("(Ljava/nio/file/Path;Ljava/util/Set;Ljava/util/concurrent/ExecutorService;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/channels/AsynchronousFileChannel;", varargs=True)
    newByteChannel = JavaMethod("(Ljava/nio/file/Path;Ljava/util/Set;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/channels/SeekableByteChannel;", varargs=True)
    newDirectoryStream = JavaMethod("(Ljava/nio/file/Path;Ljava/nio/file/DirectoryStream$Filter;)Ljava/nio/file/DirectoryStream;")
    createDirectory = JavaMethod("(Ljava/nio/file/Path;[Ljava/nio/file/attribute/FileAttribute;)V", varargs=True)
    createSymbolicLink = JavaMethod("(Ljava/nio/file/Path;Ljava/nio/file/Path;[Ljava/nio/file/attribute/FileAttribute;)V", varargs=True)
    createLink = JavaMethod("(Ljava/nio/file/Path;Ljava/nio/file/Path;)V")
    delete = JavaMethod("(Ljava/nio/file/Path;)V")
    deleteIfExists = JavaMethod("(Ljava/nio/file/Path;)Z")
    readSymbolicLink = JavaMethod("(Ljava/nio/file/Path;)Ljava/nio/file/Path;")
    copy = JavaMethod("(Ljava/nio/file/Path;Ljava/nio/file/Path;[Ljava/nio/file/CopyOption;)V", varargs=True)
    move = JavaMethod("(Ljava/nio/file/Path;Ljava/nio/file/Path;[Ljava/nio/file/CopyOption;)V", varargs=True)
    isSameFile = JavaMethod("(Ljava/nio/file/Path;Ljava/nio/file/Path;)Z")
    isHidden = JavaMethod("(Ljava/nio/file/Path;)Z")
    getFileStore = JavaMethod("(Ljava/nio/file/Path;)Ljava/nio/file/FileStore;")
    checkAccess = JavaMethod("(Ljava/nio/file/Path;[Ljava/nio/file/AccessMode;)V", varargs=True)
    getFileAttributeView = JavaMethod("(Ljava/nio/file/Path;Ljava/lang/Class;[Ljava/nio/file/LinkOption;)Ljava/nio/file/attribute/FileAttributeView;", varargs=True)
    readAttributes = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/lang/Class;[Ljava/nio/file/LinkOption;)Ljava/nio/file/attribute/BasicFileAttributes;", False, True), ("(Ljava/nio/file/Path;Ljava/lang/String;[Ljava/nio/file/LinkOption;)Ljava/util/Map;", False, True)])
    setAttribute = JavaMethod("(Ljava/nio/file/Path;Ljava/lang/String;Ljava/lang/Object;[Ljava/nio/file/LinkOption;)V", varargs=True)