from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BufferedReader"]

class BufferedReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/BufferedReader"
    __javaconstructor__ = [("(Ljava/io/Reader;I)V", False), ("(Ljava/io/Reader;)V", False)]
    read = JavaMultipleMethod([("()I", False, False), ("([CII)I", False, False)])
    readLine = JavaMethod("()Ljava/lang/String;")
    skip = JavaMethod("(J)J")
    ready = JavaMethod("()Z")
    markSupported = JavaMethod("()Z")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
    lines = JavaMethod("()Ljava/util/stream/Stream;")