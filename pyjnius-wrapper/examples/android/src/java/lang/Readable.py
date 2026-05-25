from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Readable"]

class Readable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Readable"
    read = JavaMethod("(Ljava/nio/CharBuffer;)I")