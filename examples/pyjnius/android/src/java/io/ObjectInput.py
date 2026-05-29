from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectInput"]

class ObjectInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ObjectInput"
    close = JavaMethod("()V")
    readObject = JavaMethod("()Ljava/lang/Object;")
    read = JavaMultipleMethod([("([BII)I", False, False), ("()I", False, False), ("([B)I", False, False)])
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")