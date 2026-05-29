from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LineNumberInputStream"]

class LineNumberInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/LineNumberInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False)]
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    skip = JavaMethod("(J)J")
    setLineNumber = JavaMethod("(I)V")
    getLineNumber = JavaMethod("()I")
    available = JavaMethod("()I")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")