from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicFile"]

class AtomicFile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/AtomicFile"
    __javaconstructor__ = [("(Ljava/io/File;)V", False)]
    openRead = JavaMethod("()Ljava/io/FileInputStream;")
    finishWrite = JavaMethod("(Ljava/io/FileOutputStream;)V")
    failWrite = JavaMethod("(Ljava/io/FileOutputStream;)V")
    getBaseFile = JavaMethod("()Ljava/io/File;")
    startWrite = JavaMethod("()Ljava/io/FileOutputStream;")
    toString = JavaMethod("()Ljava/lang/String;")
    delete = JavaMethod("()V")
    getLastModifiedTime = JavaMethod("()J")
    readFully = JavaMethod("()[B")