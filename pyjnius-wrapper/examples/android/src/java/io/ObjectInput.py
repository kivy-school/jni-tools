from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectInput"]

class ObjectInput(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ObjectInput"
    readObject = JavaMethod("()Ljava/lang/Object;")
    read = JavaMultipleMethod([("()I", False, False), ("([B)I", False, False), ("([BII)I", False, False)])
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    close = JavaMethod("()V")