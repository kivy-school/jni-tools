from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringBufferInputStream"]

class StringBufferInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/StringBufferInputStream"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    buffer = JavaField("Ljava/lang/String;")
    count = JavaField("I")
    pos = JavaField("I")
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    reset = JavaMethod("()V")