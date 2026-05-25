from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileStore"]

class FileStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileStore"
    __javaconstructor__ = [("()V", False)]
    name = JavaMethod("()Ljava/lang/String;")
    type = JavaMethod("()Ljava/lang/String;")
    isReadOnly = JavaMethod("()Z")
    getTotalSpace = JavaMethod("()J")
    getUsableSpace = JavaMethod("()J")
    getBlockSize = JavaMethod("()J")
    getUnallocatedSpace = JavaMethod("()J")
    supportsFileAttributeView = JavaMultipleMethod([("(Ljava/lang/Class;)Z", False, False), ("(Ljava/lang/String;)Z", False, False)])
    getFileStoreAttributeView = JavaMethod("(Ljava/lang/Class;)Ljava/nio/file/attribute/FileStoreAttributeView;")
    getAttribute = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")