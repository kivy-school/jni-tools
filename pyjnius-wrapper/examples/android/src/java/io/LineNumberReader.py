from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LineNumberReader"]

class LineNumberReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/LineNumberReader"
    __javaconstructor__ = [("(Ljava/io/Reader;)V", False), ("(Ljava/io/Reader;I)V", False)]
    setLineNumber = JavaMethod("(I)V")
    getLineNumber = JavaMethod("()I")
    read = JavaMultipleMethod([("()I", False, False), ("([CII)I", False, False)])
    readLine = JavaMethod("()Ljava/lang/String;")
    skip = JavaMethod("(J)J")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")