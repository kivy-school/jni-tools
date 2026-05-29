from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PosixFileAttributes"]

class PosixFileAttributes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/PosixFileAttributes"
    group = JavaMethod("()Ljava/nio/file/attribute/GroupPrincipal;")
    permissions = JavaMethod("()Ljava/util/Set;")
    owner = JavaMethod("()Ljava/nio/file/attribute/UserPrincipal;")