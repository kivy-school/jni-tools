from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Readable"]

class Readable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Readable"
    read = JavaMethod("(Ljava/nio/CharBuffer;)I")