from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintStream"]

class PrintStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PrintStream"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/io/OutputStream;ZLjava/nio/charset/Charset;)V", False), ("(Ljava/io/OutputStream;ZLjava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/nio/charset/Charset;)V", False), ("(Ljava/io/File;Ljava/lang/String;)V", False), ("(Ljava/io/File;Ljava/nio/charset/Charset;)V", False), ("(Ljava/io/File;)V", False), ("(Ljava/io/OutputStream;)V", False), ("(Ljava/io/OutputStream;Z)V", False)]
    println = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/Object;)V", False, False), ("(F)V", False, False), ("(D)V", False, False), ("([C)V", False, False), ("(Z)V", False, False), ("()V", False, False), ("(C)V", False, False), ("(I)V", False, False), ("(J)V", False, False)])
    append = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/lang/Appendable;", False, False), ("(C)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/CharSequence;)Ljava/io/PrintStream;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/io/PrintStream;", False, False), ("(C)Ljava/io/PrintStream;", False, False)])
    flush = JavaMethod("()V")
    format = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintStream;", False, True), ("(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintStream;", False, True)])
    charset = JavaMethod("()Ljava/nio/charset/Charset;")
    close = JavaMethod("()V")
    print = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Ljava/lang/String;)V", False, False), ("(J)V", False, False), ("(I)V", False, False), ("(C)V", False, False), ("(Z)V", False, False), ("([C)V", False, False), ("(D)V", False, False), ("(F)V", False, False)])
    write = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False), ("([B)V", False, False)])
    printf = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintStream;", False, True), ("(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintStream;", False, True)])
    writeBytes = JavaMethod("([B)V")
    checkError = JavaMethod("()Z")