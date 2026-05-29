from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectOutput"]

class ObjectOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ObjectOutput"
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    writeObject = JavaMethod("(Ljava/lang/Object;)V")
    write = JavaMultipleMethod([("([B)V", False, False), ("(I)V", False, False), ("([BII)V", False, False)])