from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileSystem"]

class FileSystem(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileSystem"
    __javaconstructor__ = [("()V", False)]
    provider = JavaMethod("()Ljava/nio/file/spi/FileSystemProvider;")
    close = JavaMethod("()V")
    isOpen = JavaMethod("()Z")
    isReadOnly = JavaMethod("()Z")
    getSeparator = JavaMethod("()Ljava/lang/String;")
    getRootDirectories = JavaMethod("()Ljava/lang/Iterable;")
    getFileStores = JavaMethod("()Ljava/lang/Iterable;")
    supportedFileAttributeViews = JavaMethod("()Ljava/util/Set;")
    getPath = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;)Ljava/nio/file/Path;", varargs=True)
    getPathMatcher = JavaMethod("(Ljava/lang/String;)Ljava/nio/file/PathMatcher;")
    getUserPrincipalLookupService = JavaMethod("()Ljava/nio/file/attribute/UserPrincipalLookupService;")
    newWatchService = JavaMethod("()Ljava/nio/file/WatchService;")