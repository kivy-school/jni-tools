from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Path"]

class Path(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/Path"
    getName = JavaMethod("(I)Ljava/nio/file/Path;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Ljava/nio/file/Path;)I", False, False)])
    of = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/String;)Ljava/nio/file/Path;", True, True), ("(Ljava/net/URI;)Ljava/nio/file/Path;", True, False)])
    startsWith = JavaMultipleMethod([("(Ljava/lang/String;)Z", False, False), ("(Ljava/nio/file/Path;)Z", False, False)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    endsWith = JavaMultipleMethod([("(Ljava/lang/String;)Z", False, False), ("(Ljava/nio/file/Path;)Z", False, False)])
    register = JavaMultipleMethod([("(Ljava/nio/file/WatchService;[Ljava/nio/file/WatchEvent$Kind;)Ljava/nio/file/WatchKey;", False, True), ("(Ljava/nio/file/WatchService;[Ljava/nio/file/WatchEvent$Kind;[Ljava/nio/file/WatchEvent$Modifier;)Ljava/nio/file/WatchKey;", False, True)])
    isAbsolute = JavaMethod("()Z")
    resolve = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/String;)Ljava/nio/file/Path;", False, True), ("(Ljava/nio/file/Path;[Ljava/nio/file/Path;)Ljava/nio/file/Path;", False, True), ("(Ljava/nio/file/Path;)Ljava/nio/file/Path;", False, False), ("(Ljava/lang/String;)Ljava/nio/file/Path;", False, False)])
    getParent = JavaMethod("()Ljava/nio/file/Path;")
    getRoot = JavaMethod("()Ljava/nio/file/Path;")
    toRealPath = JavaMethod("([Ljava/nio/file/LinkOption;)Ljava/nio/file/Path;", varargs=True)
    toFile = JavaMethod("()Ljava/io/File;")
    normalize = JavaMethod("()Ljava/nio/file/Path;")
    getFileSystem = JavaMethod("()Ljava/nio/file/FileSystem;")
    relativize = JavaMethod("(Ljava/nio/file/Path;)Ljava/nio/file/Path;")
    getFileName = JavaMethod("()Ljava/nio/file/Path;")
    getNameCount = JavaMethod("()I")
    subpath = JavaMethod("(II)Ljava/nio/file/Path;")
    toAbsolutePath = JavaMethod("()Ljava/nio/file/Path;")
    toUri = JavaMethod("()Ljava/net/URI;")
    resolveSibling = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/nio/file/Path;", False, False), ("(Ljava/nio/file/Path;)Ljava/nio/file/Path;", False, False)])