from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DosFileAttributeView"]

class DosFileAttributeView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/DosFileAttributeView"
    name = JavaMethod("()Ljava/lang/String;")
    setReadOnly = JavaMethod("(Z)V")
    setHidden = JavaMethod("(Z)V")
    readAttributes = JavaMultipleMethod([("()Ljava/nio/file/attribute/BasicFileAttributes;", False, False), ("()Ljava/nio/file/attribute/DosFileAttributes;", False, False)])
    setSystem = JavaMethod("(Z)V")
    setArchive = JavaMethod("(Z)V")