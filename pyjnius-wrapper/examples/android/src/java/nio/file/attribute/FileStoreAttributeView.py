from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileStoreAttributeView"]

class FileStoreAttributeView(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/FileStoreAttributeView"