from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Console"]

class Console(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/Console"
    isTerminal = JavaMethod("()Z")
    flush = JavaMethod("()V")
    format = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/Console;", False, True), ("(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/Console;", False, True)])
    charset = JavaMethod("()Ljava/nio/charset/Charset;")
    readLine = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;", False, True), ("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;", False, True)])
    reader = JavaMethod("()Ljava/io/Reader;")
    writer = JavaMethod("()Ljava/io/PrintWriter;")
    printf = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/Console;", False, True), ("(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/Console;", False, True)])
    readPassword = JavaMultipleMethod([("(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)[C", False, True), ("()[C", False, False), ("(Ljava/lang/String;[Ljava/lang/Object;)[C", False, True)])