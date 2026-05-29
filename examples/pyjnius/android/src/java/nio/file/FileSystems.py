from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileSystems"]

class FileSystems(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileSystems"
    getDefault = JavaStaticMethod("()Ljava/nio/file/FileSystem;")
    getFileSystem = JavaStaticMethod("(Ljava/net/URI;)Ljava/nio/file/FileSystem;")
    newFileSystem = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/util/Map;)Ljava/nio/file/FileSystem;", True, False), ("(Ljava/nio/file/Path;)Ljava/nio/file/FileSystem;", True, False), ("(Ljava/nio/file/Path;Ljava/util/Map;Ljava/lang/ClassLoader;)Ljava/nio/file/FileSystem;", True, False), ("(Ljava/nio/file/Path;Ljava/lang/ClassLoader;)Ljava/nio/file/FileSystem;", True, False), ("(Ljava/net/URI;Ljava/util/Map;Ljava/lang/ClassLoader;)Ljava/nio/file/FileSystem;", True, False), ("(Ljava/net/URI;Ljava/util/Map;)Ljava/nio/file/FileSystem;", True, False)])