from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Path"]

class Path(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/Path"
    of = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/String;)Ljava/nio/file/Path;", True, True), ("(Ljava/net/URI;)Ljava/nio/file/Path;", True, False)])
    getFileSystem = JavaMethod("()Ljava/nio/file/FileSystem;")
    isAbsolute = JavaMethod("()Z")
    getRoot = JavaMethod("()Ljava/nio/file/Path;")
    getFileName = JavaMethod("()Ljava/nio/file/Path;")
    getParent = JavaMethod("()Ljava/nio/file/Path;")
    getNameCount = JavaMethod("()I")
    getName = JavaMethod("(I)Ljava/nio/file/Path;")
    subpath = JavaMethod("(II)Ljava/nio/file/Path;")
    startsWith = JavaMultipleMethod([("(Ljava/nio/file/Path;)Z", False, False), ("(Ljava/lang/String;)Z", False, False)])
    endsWith = JavaMultipleMethod([("(Ljava/nio/file/Path;)Z", False, False), ("(Ljava/lang/String;)Z", False, False)])
    normalize = JavaMethod("()Ljava/nio/file/Path;")
    resolve = JavaMultipleMethod([("(Ljava/nio/file/Path;)Ljava/nio/file/Path;", False, False), ("(Ljava/lang/String;)Ljava/nio/file/Path;", False, False)])
    resolveSibling = JavaMultipleMethod([("(Ljava/nio/file/Path;)Ljava/nio/file/Path;", False, False), ("(Ljava/lang/String;)Ljava/nio/file/Path;", False, False)])
    relativize = JavaMethod("(Ljava/nio/file/Path;)Ljava/nio/file/Path;")
    toUri = JavaMethod("()Ljava/net/URI;")
    toAbsolutePath = JavaMethod("()Ljava/nio/file/Path;")
    toRealPath = JavaMethod("([Ljava/nio/file/LinkOption;)Ljava/nio/file/Path;", varargs=True)
    toFile = JavaMethod("()Ljava/io/File;")
    register = JavaMultipleMethod([("(Ljava/nio/file/WatchService;[Ljava/nio/file/WatchEvent$Kind;[Ljava/nio/file/WatchEvent$Modifier;)Ljava/nio/file/WatchKey;", False, True), ("(Ljava/nio/file/WatchService;[Ljava/nio/file/WatchEvent$Kind;)Ljava/nio/file/WatchKey;", False, True)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    compareTo = JavaMethod("(Ljava/nio/file/Path;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")