from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringBufferInputStream"]

class StringBufferInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/StringBufferInputStream"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    reset = JavaMethod("()V")
    read = JavaMultipleMethod([("([BII)I", False, False), ("()I", False, False)])
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")