from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileSystem"]

class FileSystem(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileSystem"
    isOpen = JavaMethod("()Z")
    close = JavaMethod("()V")
    provider = JavaMethod("()Ljava/nio/file/spi/FileSystemProvider;")
    getPath = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;)Ljava/nio/file/Path;", varargs=True)
    getSeparator = JavaMethod("()Ljava/lang/String;")
    supportedFileAttributeViews = JavaMethod("()Ljava/util/Set;")
    newWatchService = JavaMethod("()Ljava/nio/file/WatchService;")
    isReadOnly = JavaMethod("()Z")
    getRootDirectories = JavaMethod("()Ljava/lang/Iterable;")
    getFileStores = JavaMethod("()Ljava/lang/Iterable;")
    getPathMatcher = JavaMethod("(Ljava/lang/String;)Ljava/nio/file/PathMatcher;")
    getUserPrincipalLookupService = JavaMethod("()Ljava/nio/file/attribute/UserPrincipalLookupService;")