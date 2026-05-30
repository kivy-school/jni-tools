from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class WatchEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/WatchEvent"
    context = JavaMethod("()Ljava/lang/Object;")
    count = JavaMethod("()I")
    kind = JavaMethod("()Ljava/nio/file/WatchEvent$Kind;")

    class Modifier(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/file/WatchEvent$Modifier"
        name = JavaMethod("()Ljava/lang/String;")

    class Kind(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/file/WatchEvent$Kind"
        name = JavaMethod("()Ljava/lang/String;")
        type = JavaMethod("()Ljava/lang/Class;")

class StandardCopyOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/StandardCopyOption"
    REPLACE_EXISTING = JavaStaticField("Ljava/nio/file/StandardCopyOption;")
    COPY_ATTRIBUTES = JavaStaticField("Ljava/nio/file/StandardCopyOption;")
    ATOMIC_MOVE = JavaStaticField("Ljava/nio/file/StandardCopyOption;")
    values = JavaStaticMethod("()[Ljava/nio/file/StandardCopyOption;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/StandardCopyOption;")
    REPLACE_EXISTING = JavaStaticField("Ljava/nio/file/StandardCopyOption;")
    COPY_ATTRIBUTES = JavaStaticField("Ljava/nio/file/StandardCopyOption;")
    ATOMIC_MOVE = JavaStaticField("Ljava/nio/file/StandardCopyOption;")

class FileSystem(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileSystem"
    supportedFileAttributeViews = JavaMethod("()Ljava/util/Set;")
    newWatchService = JavaMethod("()Ljava/nio/file/WatchService;")
    getRootDirectories = JavaMethod("()Ljava/lang/Iterable;")
    getFileStores = JavaMethod("()Ljava/lang/Iterable;")
    getPathMatcher = JavaMethod("(Ljava/lang/String;)Ljava/nio/file/PathMatcher;")
    getUserPrincipalLookupService = JavaMethod("()Ljava/nio/file/attribute/UserPrincipalLookupService;")
    isOpen = JavaMethod("()Z")
    provider = JavaMethod("()Ljava/nio/file/spi/FileSystemProvider;")
    close = JavaMethod("()V")
    getSeparator = JavaMethod("()Ljava/lang/String;")
    getPath = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;)Ljava/nio/file/Path;", varargs=True)
    isReadOnly = JavaMethod("()Z")

class ProviderMismatchException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/ProviderMismatchException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class Files(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/Files"
    newByteChannel = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/util/Set;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/channels/SeekableByteChannel;", True, True), ("(Ljava/nio/file/Path;[Ljava/nio/file/OpenOption;)Ljava/nio/channels/SeekableByteChannel;", True, True)])
    isReadable = JavaStaticMethod("(Ljava/nio/file/Path;)Z")
    isWritable = JavaStaticMethod("(Ljava/nio/file/Path;)Z")
    isExecutable = JavaStaticMethod("(Ljava/nio/file/Path;)Z")
    newDirectoryStream = JavaMultipleMethod([("(Ljava/nio/file/Path;)Ljava/nio/file/DirectoryStream;", True, False), ("(Ljava/nio/file/Path;Ljava/lang/String;)Ljava/nio/file/DirectoryStream;", True, False), ("(Ljava/nio/file/Path;Ljava/nio/file/DirectoryStream$Filter;)Ljava/nio/file/DirectoryStream;", True, False)])
    createSymbolicLink = JavaStaticMethod("(Ljava/nio/file/Path;Ljava/nio/file/Path;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/file/Path;", varargs=True)
    createLink = JavaStaticMethod("(Ljava/nio/file/Path;Ljava/nio/file/Path;)Ljava/nio/file/Path;")
    readSymbolicLink = JavaStaticMethod("(Ljava/nio/file/Path;)Ljava/nio/file/Path;")
    setAttribute = JavaStaticMethod("(Ljava/nio/file/Path;Ljava/lang/String;Ljava/lang/Object;[Ljava/nio/file/LinkOption;)Ljava/nio/file/Path;", varargs=True)
    deleteIfExists = JavaStaticMethod("(Ljava/nio/file/Path;)Z")
    newInputStream = JavaStaticMethod("(Ljava/nio/file/Path;[Ljava/nio/file/OpenOption;)Ljava/io/InputStream;", varargs=True)
    newOutputStream = JavaStaticMethod("(Ljava/nio/file/Path;[Ljava/nio/file/OpenOption;)Ljava/io/OutputStream;", varargs=True)
    isSymbolicLink = JavaStaticMethod("(Ljava/nio/file/Path;)Z")
    setOwner = JavaStaticMethod("(Ljava/nio/file/Path;Ljava/nio/file/attribute/UserPrincipal;)Ljava/nio/file/Path;")
    createTempDirectory = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/lang/String;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/file/Path;", True, True), ("(Ljava/lang/String;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/file/Path;", True, True)])
    probeContentType = JavaStaticMethod("(Ljava/nio/file/Path;)Ljava/lang/String;")
    walkFileTree = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/util/Set;ILjava/nio/file/FileVisitor;)Ljava/nio/file/Path;", True, False), ("(Ljava/nio/file/Path;Ljava/nio/file/FileVisitor;)Ljava/nio/file/Path;", True, False)])
    newBufferedReader = JavaMultipleMethod([("(Ljava/nio/file/Path;)Ljava/io/BufferedReader;", True, False), ("(Ljava/nio/file/Path;Ljava/nio/charset/Charset;)Ljava/io/BufferedReader;", True, False)])
    newBufferedWriter = JavaMultipleMethod([("(Ljava/nio/file/Path;[Ljava/nio/file/OpenOption;)Ljava/io/BufferedWriter;", True, True), ("(Ljava/nio/file/Path;Ljava/nio/charset/Charset;[Ljava/nio/file/OpenOption;)Ljava/io/BufferedWriter;", True, True)])
    readString = JavaMultipleMethod([("(Ljava/nio/file/Path;)Ljava/lang/String;", True, False), ("(Ljava/nio/file/Path;Ljava/nio/charset/Charset;)Ljava/lang/String;", True, False)])
    readAllLines = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/nio/charset/Charset;)Ljava/util/List;", True, False), ("(Ljava/nio/file/Path;)Ljava/util/List;", True, False)])
    writeString = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/lang/CharSequence;Ljava/nio/charset/Charset;[Ljava/nio/file/OpenOption;)Ljava/nio/file/Path;", True, True), ("(Ljava/nio/file/Path;Ljava/lang/CharSequence;[Ljava/nio/file/OpenOption;)Ljava/nio/file/Path;", True, True)])
    createFile = JavaStaticMethod("(Ljava/nio/file/Path;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/file/Path;", varargs=True)
    createDirectories = JavaStaticMethod("(Ljava/nio/file/Path;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/file/Path;", varargs=True)
    getAttribute = JavaStaticMethod("(Ljava/nio/file/Path;Ljava/lang/String;[Ljava/nio/file/LinkOption;)Ljava/lang/Object;", varargs=True)
    getPosixFilePermissions = JavaStaticMethod("(Ljava/nio/file/Path;[Ljava/nio/file/LinkOption;)Ljava/util/Set;", varargs=True)
    setPosixFilePermissions = JavaStaticMethod("(Ljava/nio/file/Path;Ljava/util/Set;)Ljava/nio/file/Path;")
    notExists = JavaStaticMethod("(Ljava/nio/file/Path;[Ljava/nio/file/LinkOption;)Z", varargs=True)
    size = JavaStaticMethod("(Ljava/nio/file/Path;)J")
    isHidden = JavaStaticMethod("(Ljava/nio/file/Path;)Z")
    mismatch = JavaStaticMethod("(Ljava/nio/file/Path;Ljava/nio/file/Path;)J")
    lines = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/nio/charset/Charset;)Ljava/util/stream/Stream;", True, False), ("(Ljava/nio/file/Path;)Ljava/util/stream/Stream;", True, False)])
    list = JavaStaticMethod("(Ljava/nio/file/Path;)Ljava/util/stream/Stream;")
    find = JavaStaticMethod("(Ljava/nio/file/Path;ILjava/util/function/BiPredicate;[Ljava/nio/file/FileVisitOption;)Ljava/util/stream/Stream;", varargs=True)
    write = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/lang/Iterable;Ljava/nio/charset/Charset;[Ljava/nio/file/OpenOption;)Ljava/nio/file/Path;", True, True), ("(Ljava/nio/file/Path;[B[Ljava/nio/file/OpenOption;)Ljava/nio/file/Path;", True, True), ("(Ljava/nio/file/Path;Ljava/lang/Iterable;[Ljava/nio/file/OpenOption;)Ljava/nio/file/Path;", True, True)])
    delete = JavaStaticMethod("(Ljava/nio/file/Path;)V")
    readAllBytes = JavaStaticMethod("(Ljava/nio/file/Path;)[B")
    copy = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/io/OutputStream;)J", True, False), ("(Ljava/nio/file/Path;Ljava/nio/file/Path;[Ljava/nio/file/CopyOption;)Ljava/nio/file/Path;", True, True), ("(Ljava/io/InputStream;Ljava/nio/file/Path;[Ljava/nio/file/CopyOption;)J", True, True)])
    getOwner = JavaStaticMethod("(Ljava/nio/file/Path;[Ljava/nio/file/LinkOption;)Ljava/nio/file/attribute/UserPrincipal;", varargs=True)
    exists = JavaStaticMethod("(Ljava/nio/file/Path;[Ljava/nio/file/LinkOption;)Z", varargs=True)
    walk = JavaMultipleMethod([("(Ljava/nio/file/Path;I[Ljava/nio/file/FileVisitOption;)Ljava/util/stream/Stream;", True, True), ("(Ljava/nio/file/Path;[Ljava/nio/file/FileVisitOption;)Ljava/util/stream/Stream;", True, True)])
    getLastModifiedTime = JavaStaticMethod("(Ljava/nio/file/Path;[Ljava/nio/file/LinkOption;)Ljava/nio/file/attribute/FileTime;", varargs=True)
    createDirectory = JavaStaticMethod("(Ljava/nio/file/Path;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/file/Path;", varargs=True)
    setLastModifiedTime = JavaStaticMethod("(Ljava/nio/file/Path;Ljava/nio/file/attribute/FileTime;)Ljava/nio/file/Path;")
    createTempFile = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/file/Path;", True, True), ("(Ljava/nio/file/Path;Ljava/lang/String;Ljava/lang/String;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/file/Path;", True, True)])
    isRegularFile = JavaStaticMethod("(Ljava/nio/file/Path;[Ljava/nio/file/LinkOption;)Z", varargs=True)
    readAttributes = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/lang/String;[Ljava/nio/file/LinkOption;)Ljava/util/Map;", True, True), ("(Ljava/nio/file/Path;Ljava/lang/Class;[Ljava/nio/file/LinkOption;)Ljava/nio/file/attribute/BasicFileAttributes;", True, True)])
    getFileAttributeView = JavaStaticMethod("(Ljava/nio/file/Path;Ljava/lang/Class;[Ljava/nio/file/LinkOption;)Ljava/nio/file/attribute/FileAttributeView;", varargs=True)
    getFileStore = JavaStaticMethod("(Ljava/nio/file/Path;)Ljava/nio/file/FileStore;")
    move = JavaStaticMethod("(Ljava/nio/file/Path;Ljava/nio/file/Path;[Ljava/nio/file/CopyOption;)Ljava/nio/file/Path;", varargs=True)
    isSameFile = JavaStaticMethod("(Ljava/nio/file/Path;Ljava/nio/file/Path;)Z")
    isDirectory = JavaStaticMethod("(Ljava/nio/file/Path;[Ljava/nio/file/LinkOption;)Z", varargs=True)

class FileSystemAlreadyExistsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileSystemAlreadyExistsException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class FileAlreadyExistsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileAlreadyExistsException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]

class AtomicMoveNotSupportedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/AtomicMoveNotSupportedException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]

class LinkPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/LinkPermission"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]

class Path(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/Path"
    getNameCount = JavaMethod("()I")
    subpath = JavaMethod("(II)Ljava/nio/file/Path;")
    toAbsolutePath = JavaMethod("()Ljava/nio/file/Path;")
    toUri = JavaMethod("()Ljava/net/URI;")
    resolveSibling = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/nio/file/Path;", False, False), ("(Ljava/nio/file/Path;)Ljava/nio/file/Path;", False, False)])
    getName = JavaMethod("(I)Ljava/nio/file/Path;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/nio/file/Path;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    startsWith = JavaMultipleMethod([("(Ljava/lang/String;)Z", False, False), ("(Ljava/nio/file/Path;)Z", False, False)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    of = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/String;)Ljava/nio/file/Path;", True, True), ("(Ljava/net/URI;)Ljava/nio/file/Path;", True, False)])
    endsWith = JavaMultipleMethod([("(Ljava/lang/String;)Z", False, False), ("(Ljava/nio/file/Path;)Z", False, False)])
    register = JavaMultipleMethod([("(Ljava/nio/file/WatchService;[Ljava/nio/file/WatchEvent$Kind;)Ljava/nio/file/WatchKey;", False, True), ("(Ljava/nio/file/WatchService;[Ljava/nio/file/WatchEvent$Kind;[Ljava/nio/file/WatchEvent$Modifier;)Ljava/nio/file/WatchKey;", False, True)])
    isAbsolute = JavaMethod("()Z")
    resolve = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/nio/file/Path;", False, False), ("(Ljava/nio/file/Path;)Ljava/nio/file/Path;", False, False)])
    getParent = JavaMethod("()Ljava/nio/file/Path;")
    getRoot = JavaMethod("()Ljava/nio/file/Path;")
    getFileSystem = JavaMethod("()Ljava/nio/file/FileSystem;")
    relativize = JavaMethod("(Ljava/nio/file/Path;)Ljava/nio/file/Path;")
    normalize = JavaMethod("()Ljava/nio/file/Path;")
    toRealPath = JavaMethod("([Ljava/nio/file/LinkOption;)Ljava/nio/file/Path;", varargs=True)
    toFile = JavaMethod("()Ljava/io/File;")
    getFileName = JavaMethod("()Ljava/nio/file/Path;")

class ClosedWatchServiceException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/ClosedWatchServiceException"
    __javaconstructor__ = [("()V", False)]

class WatchKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/WatchKey"
    reset = JavaMethod("()Z")
    cancel = JavaMethod("()V")
    isValid = JavaMethod("()Z")
    pollEvents = JavaMethod("()Ljava/util/List;")
    watchable = JavaMethod("()Ljava/nio/file/Watchable;")

class NotLinkException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/NotLinkException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]

class DirectoryStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/DirectoryStream"
    iterator = JavaMethod("()Ljava/util/Iterator;")

    class Filter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/file/DirectoryStream$Filter"
        accept = JavaMethod("(Ljava/lang/Object;)Z")

class FileVisitOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileVisitOption"
    FOLLOW_LINKS = JavaStaticField("Ljava/nio/file/FileVisitOption;")
    values = JavaStaticMethod("()[Ljava/nio/file/FileVisitOption;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/FileVisitOption;")
    FOLLOW_LINKS = JavaStaticField("Ljava/nio/file/FileVisitOption;")

class FileVisitor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileVisitor"
    visitFile = JavaMethod("(Ljava/lang/Object;Ljava/nio/file/attribute/BasicFileAttributes;)Ljava/nio/file/FileVisitResult;")
    visitFileFailed = JavaMethod("(Ljava/lang/Object;Ljava/io/IOException;)Ljava/nio/file/FileVisitResult;")
    preVisitDirectory = JavaMethod("(Ljava/lang/Object;Ljava/nio/file/attribute/BasicFileAttributes;)Ljava/nio/file/FileVisitResult;")
    postVisitDirectory = JavaMethod("(Ljava/lang/Object;Ljava/io/IOException;)Ljava/nio/file/FileVisitResult;")

class ReadOnlyFileSystemException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/ReadOnlyFileSystemException"
    __javaconstructor__ = [("()V", False)]

class ClosedFileSystemException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/ClosedFileSystemException"
    __javaconstructor__ = [("()V", False)]

class StandardWatchEventKinds(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/StandardWatchEventKinds"
    OVERFLOW = JavaStaticField("Ljava/nio/file/WatchEvent$Kind;")
    ENTRY_CREATE = JavaStaticField("Ljava/nio/file/WatchEvent$Kind;")
    ENTRY_DELETE = JavaStaticField("Ljava/nio/file/WatchEvent$Kind;")
    ENTRY_MODIFY = JavaStaticField("Ljava/nio/file/WatchEvent$Kind;")

class FileSystemException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileSystemException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getFile = JavaMethod("()Ljava/lang/String;")
    getReason = JavaMethod("()Ljava/lang/String;")
    getOtherFile = JavaMethod("()Ljava/lang/String;")

class ClosedDirectoryStreamException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/ClosedDirectoryStreamException"
    __javaconstructor__ = [("()V", False)]

class StandardOpenOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/StandardOpenOption"
    READ = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    WRITE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    APPEND = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    TRUNCATE_EXISTING = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    CREATE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    CREATE_NEW = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    DELETE_ON_CLOSE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    SPARSE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    SYNC = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    DSYNC = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    values = JavaStaticMethod("()[Ljava/nio/file/StandardOpenOption;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/StandardOpenOption;")
    READ = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    WRITE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    APPEND = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    TRUNCATE_EXISTING = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    CREATE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    CREATE_NEW = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    DELETE_ON_CLOSE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    SPARSE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    SYNC = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    DSYNC = JavaStaticField("Ljava/nio/file/StandardOpenOption;")

class NotDirectoryException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/NotDirectoryException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]

class NoSuchFileException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/NoSuchFileException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]

class FileSystemNotFoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileSystemNotFoundException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class FileSystemLoopException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileSystemLoopException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]

class PathMatcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/PathMatcher"
    matches = JavaMethod("(Ljava/nio/file/Path;)Z")

class Watchable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/Watchable"
    register = JavaMultipleMethod([("(Ljava/nio/file/WatchService;[Ljava/nio/file/WatchEvent$Kind;[Ljava/nio/file/WatchEvent$Modifier;)Ljava/nio/file/WatchKey;", False, True), ("(Ljava/nio/file/WatchService;[Ljava/nio/file/WatchEvent$Kind;)Ljava/nio/file/WatchKey;", False, True)])

class FileSystems(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileSystems"
    getDefault = JavaStaticMethod("()Ljava/nio/file/FileSystem;")
    getFileSystem = JavaStaticMethod("(Ljava/net/URI;)Ljava/nio/file/FileSystem;")
    newFileSystem = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/util/Map;)Ljava/nio/file/FileSystem;", True, False), ("(Ljava/nio/file/Path;)Ljava/nio/file/FileSystem;", True, False), ("(Ljava/nio/file/Path;Ljava/util/Map;Ljava/lang/ClassLoader;)Ljava/nio/file/FileSystem;", True, False), ("(Ljava/nio/file/Path;Ljava/lang/ClassLoader;)Ljava/nio/file/FileSystem;", True, False), ("(Ljava/net/URI;Ljava/util/Map;Ljava/lang/ClassLoader;)Ljava/nio/file/FileSystem;", True, False), ("(Ljava/net/URI;Ljava/util/Map;)Ljava/nio/file/FileSystem;", True, False)])

class AccessDeniedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/AccessDeniedException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]

class CopyOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/CopyOption"

class DirectoryNotEmptyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/DirectoryNotEmptyException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]

class FileVisitResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileVisitResult"
    CONTINUE = JavaStaticField("Ljava/nio/file/FileVisitResult;")
    TERMINATE = JavaStaticField("Ljava/nio/file/FileVisitResult;")
    SKIP_SUBTREE = JavaStaticField("Ljava/nio/file/FileVisitResult;")
    SKIP_SIBLINGS = JavaStaticField("Ljava/nio/file/FileVisitResult;")
    values = JavaStaticMethod("()[Ljava/nio/file/FileVisitResult;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/FileVisitResult;")
    CONTINUE = JavaStaticField("Ljava/nio/file/FileVisitResult;")
    TERMINATE = JavaStaticField("Ljava/nio/file/FileVisitResult;")
    SKIP_SUBTREE = JavaStaticField("Ljava/nio/file/FileVisitResult;")
    SKIP_SIBLINGS = JavaStaticField("Ljava/nio/file/FileVisitResult;")

class InvalidPathException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/InvalidPathException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;I)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getIndex = JavaMethod("()I")
    getReason = JavaMethod("()Ljava/lang/String;")
    getInput = JavaMethod("()Ljava/lang/String;")

class WatchService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/WatchService"
    poll = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Ljava/nio/file/WatchKey;", False, False), ("()Ljava/nio/file/WatchKey;", False, False)])
    close = JavaMethod("()V")
    take = JavaMethod("()Ljava/nio/file/WatchKey;")

class SimpleFileVisitor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/SimpleFileVisitor"
    visitFile = JavaMethod("(Ljava/lang/Object;Ljava/nio/file/attribute/BasicFileAttributes;)Ljava/nio/file/FileVisitResult;")
    visitFileFailed = JavaMethod("(Ljava/lang/Object;Ljava/io/IOException;)Ljava/nio/file/FileVisitResult;")
    preVisitDirectory = JavaMethod("(Ljava/lang/Object;Ljava/nio/file/attribute/BasicFileAttributes;)Ljava/nio/file/FileVisitResult;")
    postVisitDirectory = JavaMethod("(Ljava/lang/Object;Ljava/io/IOException;)Ljava/nio/file/FileVisitResult;")

class ProviderNotFoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/ProviderNotFoundException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class LinkOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/LinkOption"
    NOFOLLOW_LINKS = JavaStaticField("Ljava/nio/file/LinkOption;")
    values = JavaStaticMethod("()[Ljava/nio/file/LinkOption;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/LinkOption;")
    NOFOLLOW_LINKS = JavaStaticField("Ljava/nio/file/LinkOption;")

class AccessMode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/AccessMode"
    READ = JavaStaticField("Ljava/nio/file/AccessMode;")
    WRITE = JavaStaticField("Ljava/nio/file/AccessMode;")
    EXECUTE = JavaStaticField("Ljava/nio/file/AccessMode;")
    values = JavaStaticMethod("()[Ljava/nio/file/AccessMode;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/AccessMode;")
    READ = JavaStaticField("Ljava/nio/file/AccessMode;")
    WRITE = JavaStaticField("Ljava/nio/file/AccessMode;")
    EXECUTE = JavaStaticField("Ljava/nio/file/AccessMode;")

class FileStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileStore"
    getBlockSize = JavaMethod("()J")
    getAttribute = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    name = JavaMethod("()Ljava/lang/String;")
    type = JavaMethod("()Ljava/lang/String;")
    getTotalSpace = JavaMethod("()J")
    getUsableSpace = JavaMethod("()J")
    isReadOnly = JavaMethod("()Z")
    getUnallocatedSpace = JavaMethod("()J")
    supportsFileAttributeView = JavaMultipleMethod([("(Ljava/lang/Class;)Z", False, False), ("(Ljava/lang/String;)Z", False, False)])
    getFileStoreAttributeView = JavaMethod("(Ljava/lang/Class;)Ljava/nio/file/attribute/FileStoreAttributeView;")

class SecureDirectoryStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/SecureDirectoryStream"
    newByteChannel = JavaMethod("(Ljava/lang/Object;Ljava/util/Set;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/channels/SeekableByteChannel;", varargs=True)
    newDirectoryStream = JavaMethod("(Ljava/lang/Object;[Ljava/nio/file/LinkOption;)Ljava/nio/file/SecureDirectoryStream;", varargs=True)
    deleteFile = JavaMethod("(Ljava/lang/Object;)V")
    getFileAttributeView = JavaMultipleMethod([("(Ljava/lang/Class;)Ljava/nio/file/attribute/FileAttributeView;", False, False), ("(Ljava/lang/Object;Ljava/lang/Class;[Ljava/nio/file/LinkOption;)Ljava/nio/file/attribute/FileAttributeView;", False, True)])
    move = JavaMethod("(Ljava/lang/Object;Ljava/nio/file/SecureDirectoryStream;Ljava/lang/Object;)V")
    deleteDirectory = JavaMethod("(Ljava/lang/Object;)V")

class DirectoryIteratorException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/DirectoryIteratorException"
    __javaconstructor__ = [("(Ljava/io/IOException;)V", False)]
    getCause = JavaMultipleMethod([("()Ljava/lang/Throwable;", False, False), ("()Ljava/io/IOException;", False, False)])

class OpenOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/OpenOption"

class Paths(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/Paths"
    get = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/String;)Ljava/nio/file/Path;", True, True), ("(Ljava/net/URI;)Ljava/nio/file/Path;", True, False)])