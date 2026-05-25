from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Base64OutputStream"]

class Base64OutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Base64OutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;I)V", False)]
    write = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False)])
    close = JavaMethod("()V")