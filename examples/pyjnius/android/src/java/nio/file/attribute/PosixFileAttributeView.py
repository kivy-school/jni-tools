from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PosixFileAttributeView"]

class PosixFileAttributeView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/PosixFileAttributeView"
    setGroup = JavaMethod("(Ljava/nio/file/attribute/GroupPrincipal;)V")
    name = JavaMethod("()Ljava/lang/String;")
    readAttributes = JavaMultipleMethod([("()Ljava/nio/file/attribute/BasicFileAttributes;", False, False), ("()Ljava/nio/file/attribute/PosixFileAttributes;", False, False)])
    setPermissions = JavaMethod("(Ljava/util/Set;)V")