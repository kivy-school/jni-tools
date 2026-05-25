from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DosFileAttributeView"]

class DosFileAttributeView(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/DosFileAttributeView"
    name = JavaMethod("()Ljava/lang/String;")
    readAttributes = JavaMethod("()Ljava/nio/file/attribute/DosFileAttributes;")
    setReadOnly = JavaMethod("(Z)V")
    setHidden = JavaMethod("(Z)V")
    setSystem = JavaMethod("(Z)V")
    setArchive = JavaMethod("(Z)V")