from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MemoryFile"]

class MemoryFile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/MemoryFile"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False)]
    length = JavaMethod("()I")
    close = JavaMethod("()V")
    getInputStream = JavaMethod("()Ljava/io/InputStream;")
    allowPurging = JavaMethod("(Z)Z")
    isPurgingAllowed = JavaMethod("()Z")
    getOutputStream = JavaMethod("()Ljava/io/OutputStream;")
    readBytes = JavaMethod("([BIII)I")
    writeBytes = JavaMethod("([BIII)V")