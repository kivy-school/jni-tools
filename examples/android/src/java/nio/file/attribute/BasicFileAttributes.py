from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BasicFileAttributes"]

class BasicFileAttributes(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/BasicFileAttributes"
    lastModifiedTime = JavaMethod("()Ljava/nio/file/attribute/FileTime;")
    lastAccessTime = JavaMethod("()Ljava/nio/file/attribute/FileTime;")
    creationTime = JavaMethod("()Ljava/nio/file/attribute/FileTime;")
    isRegularFile = JavaMethod("()Z")
    isDirectory = JavaMethod("()Z")
    isSymbolicLink = JavaMethod("()Z")
    isOther = JavaMethod("()Z")
    size = JavaMethod("()J")
    fileKey = JavaMethod("()Ljava/lang/Object;")