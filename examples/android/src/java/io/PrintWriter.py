from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintWriter"]

class PrintWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PrintWriter"
    __javaconstructor__ = [("(Ljava/io/Writer;)V", False), ("(Ljava/io/Writer;Z)V", False), ("(Ljava/io/OutputStream;)V", False), ("(Ljava/io/OutputStream;Z)V", False), ("(Ljava/io/OutputStream;ZLjava/nio/charset/Charset;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/nio/charset/Charset;)V", False), ("(Ljava/io/File;)V", False), ("(Ljava/io/File;Ljava/lang/String;)V", False), ("(Ljava/io/File;Ljava/nio/charset/Charset;)V", False)]
    out = JavaField("Ljava/io/Writer;")
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    checkError = JavaMethod("()Z")
    setError = JavaMethod("()V")
    clearError = JavaMethod("()V")
    write = JavaMultipleMethod([("(I)V", False, False), ("([CII)V", False, False), ("([C)V", False, False), ("(Ljava/lang/String;II)V", False, False), ("(Ljava/lang/String;)V", False, False)])
    print = JavaMultipleMethod([("(Z)V", False, False), ("(C)V", False, False), ("(I)V", False, False), ("(J)V", False, False), ("(F)V", False, False), ("(D)V", False, False), ("([C)V", False, False), ("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/Object;)V", False, False)])
    println = JavaMultipleMethod([("()V", False, False), ("(Z)V", False, False), ("(C)V", False, False), ("(I)V", False, False), ("(J)V", False, False), ("(F)V", False, False), ("(D)V", False, False), ("([C)V", False, False), ("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/Object;)V", False, False)])
    printf = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintWriter;", False, True), ("(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintWriter;", False, True)])
    format = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintWriter;", False, True), ("(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintWriter;", False, True)])
    append = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/io/PrintWriter;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/io/PrintWriter;", False, False), ("(C)Ljava/io/PrintWriter;", False, False)])