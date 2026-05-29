from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringReader"]

class StringReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/StringReader"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("()I", False, False), ("([CII)I", False, False)])
    skip = JavaMethod("(J)J")
    markSupported = JavaMethod("()Z")
    ready = JavaMethod("()Z")