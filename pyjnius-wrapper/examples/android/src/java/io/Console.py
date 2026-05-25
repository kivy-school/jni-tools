from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Console"]

class Console(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/Console"
    writer = JavaMethod("()Ljava/io/PrintWriter;")
    reader = JavaMethod("()Ljava/io/Reader;")
    format = JavaMethod("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/Console;", varargs=True)
    printf = JavaMethod("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/Console;", varargs=True)
    readLine = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;", False, True), ("()Ljava/lang/String;", False, False)])
    readPassword = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/Object;)[C", False, True), ("()[C", False, False)])
    flush = JavaMethod("()V")
    charset = JavaMethod("()Ljava/nio/charset/Charset;")