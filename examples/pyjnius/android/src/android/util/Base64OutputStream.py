from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Base64OutputStream"]

class Base64OutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Base64OutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;I)V", False)]
    close = JavaMethod("()V")
    write = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False)])