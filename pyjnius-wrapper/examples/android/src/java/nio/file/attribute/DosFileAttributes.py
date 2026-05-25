from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DosFileAttributes"]

class DosFileAttributes(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/DosFileAttributes"
    isReadOnly = JavaMethod("()Z")
    isHidden = JavaMethod("()Z")
    isArchive = JavaMethod("()Z")
    isSystem = JavaMethod("()Z")