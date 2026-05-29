from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DosFileAttributes"]

class DosFileAttributes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/DosFileAttributes"
    isHidden = JavaMethod("()Z")
    isSystem = JavaMethod("()Z")
    isArchive = JavaMethod("()Z")
    isReadOnly = JavaMethod("()Z")