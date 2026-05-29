from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PosixFileAttributeView"]

class PosixFileAttributeView(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/PosixFileAttributeView"
    name = JavaMethod("()Ljava/lang/String;")
    readAttributes = JavaMethod("()Ljava/nio/file/attribute/PosixFileAttributes;")
    setPermissions = JavaMethod("(Ljava/util/Set;)V")
    setGroup = JavaMethod("(Ljava/nio/file/attribute/GroupPrincipal;)V")