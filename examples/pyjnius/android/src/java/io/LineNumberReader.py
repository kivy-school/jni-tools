from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LineNumberReader"]

class LineNumberReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/LineNumberReader"
    __javaconstructor__ = [("(Ljava/io/Reader;)V", False), ("(Ljava/io/Reader;I)V", False)]
    reset = JavaMethod("()V")
    readLine = JavaMethod("()Ljava/lang/String;")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("([CII)I", False, False), ("()I", False, False)])
    skip = JavaMethod("(J)J")
    setLineNumber = JavaMethod("(I)V")
    getLineNumber = JavaMethod("()I")