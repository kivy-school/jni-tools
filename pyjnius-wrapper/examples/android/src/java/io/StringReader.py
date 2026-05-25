from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringReader"]

class StringReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/StringReader"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    read = JavaMultipleMethod([("()I", False, False), ("([CII)I", False, False)])
    skip = JavaMethod("(J)J")
    ready = JavaMethod("()Z")
    markSupported = JavaMethod("()Z")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")
    close = JavaMethod("()V")