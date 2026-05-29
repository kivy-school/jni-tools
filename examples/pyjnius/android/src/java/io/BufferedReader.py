from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BufferedReader"]

class BufferedReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/BufferedReader"
    __javaconstructor__ = [("(Ljava/io/Reader;I)V", False), ("(Ljava/io/Reader;)V", False)]
    reset = JavaMethod("()V")
    lines = JavaMethod("()Ljava/util/stream/Stream;")
    close = JavaMethod("()V")
    readLine = JavaMethod("()Ljava/lang/String;")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("()I", False, False), ("([CII)I", False, False)])
    skip = JavaMethod("(J)J")
    markSupported = JavaMethod("()Z")
    ready = JavaMethod("()Z")