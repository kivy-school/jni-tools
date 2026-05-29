from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BasicFileAttributes"]

class BasicFileAttributes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/BasicFileAttributes"
    size = JavaMethod("()J")
    isDirectory = JavaMethod("()Z")
    isRegularFile = JavaMethod("()Z")
    fileKey = JavaMethod("()Ljava/lang/Object;")
    isSymbolicLink = JavaMethod("()Z")
    lastAccessTime = JavaMethod("()Ljava/nio/file/attribute/FileTime;")
    lastModifiedTime = JavaMethod("()Ljava/nio/file/attribute/FileTime;")
    creationTime = JavaMethod("()Ljava/nio/file/attribute/FileTime;")
    isOther = JavaMethod("()Z")