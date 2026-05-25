from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicFile"]

class AtomicFile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/AtomicFile"
    __javaconstructor__ = [("(Ljava/io/File;)V", False)]
    getBaseFile = JavaMethod("()Ljava/io/File;")
    delete = JavaMethod("()V")
    startWrite = JavaMethod("()Ljava/io/FileOutputStream;")
    finishWrite = JavaMethod("(Ljava/io/FileOutputStream;)V")
    failWrite = JavaMethod("(Ljava/io/FileOutputStream;)V")
    openRead = JavaMethod("()Ljava/io/FileInputStream;")
    getLastModifiedTime = JavaMethod("()J")
    readFully = JavaMethod("()[B")
    toString = JavaMethod("()Ljava/lang/String;")