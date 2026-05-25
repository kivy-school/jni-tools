from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintStream"]

class PrintStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PrintStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;)V", False), ("(Ljava/io/OutputStream;Z)V", False), ("(Ljava/io/OutputStream;ZLjava/lang/String;)V", False), ("(Ljava/io/OutputStream;ZLjava/nio/charset/Charset;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/nio/charset/Charset;)V", False), ("(Ljava/io/File;)V", False), ("(Ljava/io/File;Ljava/lang/String;)V", False), ("(Ljava/io/File;Ljava/nio/charset/Charset;)V", False)]
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    checkError = JavaMethod("()Z")
    setError = JavaMethod("()V")
    clearError = JavaMethod("()V")
    write = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False), ("([B)V", False, False)])
    writeBytes = JavaMethod("([B)V")
    print = JavaMultipleMethod([("(Z)V", False, False), ("(C)V", False, False), ("(I)V", False, False), ("(J)V", False, False), ("(F)V", False, False), ("(D)V", False, False), ("([C)V", False, False), ("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/Object;)V", False, False)])
    println = JavaMultipleMethod([("()V", False, False), ("(Z)V", False, False), ("(C)V", False, False), ("(I)V", False, False), ("(J)V", False, False), ("(F)V", False, False), ("(D)V", False, False), ("([C)V", False, False), ("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/Object;)V", False, False)])
    printf = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintStream;", False, True), ("(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintStream;", False, True)])
    format = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintStream;", False, True), ("(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintStream;", False, True)])
    append = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/io/PrintStream;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/io/PrintStream;", False, False), ("(C)Ljava/io/PrintStream;", False, False)])