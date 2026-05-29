from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InterruptedIOException"]

class InterruptedIOException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/InterruptedIOException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]
    bytesTransferred = JavaField("I")