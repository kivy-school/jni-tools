from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileStore"]

class FileStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileStore"
    getBlockSize = JavaMethod("()J")
    name = JavaMethod("()Ljava/lang/String;")
    type = JavaMethod("()Ljava/lang/String;")
    getTotalSpace = JavaMethod("()J")
    getUsableSpace = JavaMethod("()J")
    getUnallocatedSpace = JavaMethod("()J")
    supportsFileAttributeView = JavaMultipleMethod([("(Ljava/lang/String;)Z", False, False), ("(Ljava/lang/Class;)Z", False, False)])
    getFileStoreAttributeView = JavaMethod("(Ljava/lang/Class;)Ljava/nio/file/attribute/FileStoreAttributeView;")
    isReadOnly = JavaMethod("()Z")
    getAttribute = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")