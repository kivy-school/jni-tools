from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MemoryFile"]

class MemoryFile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/MemoryFile"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False)]
    close = JavaMethod("()V")
    length = JavaMethod("()I")
    isPurgingAllowed = JavaMethod("()Z")
    allowPurging = JavaMethod("(Z)Z")
    getInputStream = JavaMethod("()Ljava/io/InputStream;")
    getOutputStream = JavaMethod("()Ljava/io/OutputStream;")
    readBytes = JavaMethod("([BIII)I")
    writeBytes = JavaMethod("([BIII)V")