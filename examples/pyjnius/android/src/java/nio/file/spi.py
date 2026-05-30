from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class FileSystemProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/spi/FileSystemProvider"
    newByteChannel = JavaMethod("(Ljava/nio/file/Path;Ljava/util/Set;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/channels/SeekableByteChannel;", varargs=True)
    newDirectoryStream = JavaMethod("(Ljava/nio/file/Path;Ljava/nio/file/DirectoryStream$Filter;)Ljava/nio/file/DirectoryStream;")
    createSymbolicLink = JavaMethod("(Ljava/nio/file/Path;Ljava/nio/file/Path;[Ljava/nio/file/attribute/FileAttribute;)V", varargs=True)
    createLink = JavaMethod("(Ljava/nio/file/Path;Ljava/nio/file/Path;)V")
    readSymbolicLink = JavaMethod("(Ljava/nio/file/Path;)Ljava/nio/file/Path;")
    setAttribute = JavaMethod("(Ljava/nio/file/Path;Ljava/lang/String;Ljava/lang/Object;[Ljava/nio/file/LinkOption;)V", varargs=True)
    deleteIfExists = JavaMethod("(Ljava/nio/file/Path;)Z")
    installedProviders = JavaStaticMethod("()Ljava/util/List;")
    newInputStream = JavaMethod("(Ljava/nio/file/Path;[Ljava/nio/file/OpenOption;)Ljava/io/InputStream;", varargs=True)
    newOutputStream = JavaMethod("(Ljava/nio/file/Path;[Ljava/nio/file/OpenOption;)Ljava/io/OutputStream;", varargs=True)
    isHidden = JavaMethod("(Ljava/nio/file/Path;)Z")
    delete = JavaMethod("(Ljava/nio/file/Path;)V")
    checkAccess = JavaMethod("(Ljava/nio/file/Path;[Ljava/nio/file/AccessMode;)V", varargs=True)
    copy = JavaMethod("(Ljava/nio/file/Path;Ljava/nio/file/Path;[Ljava/nio/file/CopyOption;)V", varargs=True)
    exists = JavaMethod("(Ljava/nio/file/Path;[Ljava/nio/file/LinkOption;)Z", varargs=True)
    createDirectory = JavaMethod("(Ljava/nio/file/Path;[Ljava/nio/file/attribute/FileAttribute;)V", varargs=True)
    getFileSystem = JavaMethod("(Ljava/net/URI;)Ljava/nio/file/FileSystem;")
    readAttributes = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/lang/String;[Ljava/nio/file/LinkOption;)Ljava/util/Map;", False, True), ("(Ljava/nio/file/Path;Ljava/lang/Class;[Ljava/nio/file/LinkOption;)Ljava/nio/file/attribute/BasicFileAttributes;", False, True)])
    newFileSystem = JavaMultipleMethod([("(Ljava/net/URI;Ljava/util/Map;)Ljava/nio/file/FileSystem;", False, False), ("(Ljava/nio/file/Path;Ljava/util/Map;)Ljava/nio/file/FileSystem;", False, False)])
    getFileAttributeView = JavaMethod("(Ljava/nio/file/Path;Ljava/lang/Class;[Ljava/nio/file/LinkOption;)Ljava/nio/file/attribute/FileAttributeView;", varargs=True)
    getFileStore = JavaMethod("(Ljava/nio/file/Path;)Ljava/nio/file/FileStore;")
    readAttributesIfExists = JavaMethod("(Ljava/nio/file/Path;Ljava/lang/Class;[Ljava/nio/file/LinkOption;)Ljava/nio/file/attribute/BasicFileAttributes;", varargs=True)
    newFileChannel = JavaMethod("(Ljava/nio/file/Path;Ljava/util/Set;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/channels/FileChannel;", varargs=True)
    newAsynchronousFileChannel = JavaMethod("(Ljava/nio/file/Path;Ljava/util/Set;Ljava/util/concurrent/ExecutorService;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/channels/AsynchronousFileChannel;", varargs=True)
    move = JavaMethod("(Ljava/nio/file/Path;Ljava/nio/file/Path;[Ljava/nio/file/CopyOption;)V", varargs=True)
    isSameFile = JavaMethod("(Ljava/nio/file/Path;Ljava/nio/file/Path;)Z")
    getPath = JavaMethod("(Ljava/net/URI;)Ljava/nio/file/Path;")
    getScheme = JavaMethod("()Ljava/lang/String;")

class FileTypeDetector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/spi/FileTypeDetector"
    probeContentType = JavaMethod("(Ljava/nio/file/Path;)Ljava/lang/String;")