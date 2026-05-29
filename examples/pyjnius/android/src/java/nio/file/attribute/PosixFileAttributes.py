from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PosixFileAttributes"]

class PosixFileAttributes(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/PosixFileAttributes"
    owner = JavaMethod("()Ljava/nio/file/attribute/UserPrincipal;")
    group = JavaMethod("()Ljava/nio/file/attribute/GroupPrincipal;")
    permissions = JavaMethod("()Ljava/util/Set;")