from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectOutput"]

class ObjectOutput(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ObjectOutput"
    writeObject = JavaMethod("(Ljava/lang/Object;)V")
    write = JavaMultipleMethod([("(I)V", False, False), ("([B)V", False, False), ("([BII)V", False, False)])
    flush = JavaMethod("()V")
    close = JavaMethod("()V")