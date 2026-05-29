from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileStoreAttributeView"]

class FileStoreAttributeView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/FileStoreAttributeView"