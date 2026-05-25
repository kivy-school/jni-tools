from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PosixFilePermissions"]

class PosixFilePermissions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/PosixFilePermissions"
    toString = JavaStaticMethod("(Ljava/util/Set;)Ljava/lang/String;")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/Set;")
    asFileAttribute = JavaStaticMethod("(Ljava/util/Set;)Ljava/nio/file/attribute/FileAttribute;")