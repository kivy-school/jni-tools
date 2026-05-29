from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LineNumberInputStream"]

class LineNumberInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/LineNumberInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False)]
    reset = JavaMethod("()V")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    setLineNumber = JavaMethod("(I)V")
    getLineNumber = JavaMethod("()I")