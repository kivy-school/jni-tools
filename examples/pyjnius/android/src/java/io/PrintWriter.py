from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintWriter"]

class PrintWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PrintWriter"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/nio/charset/Charset;)V", False), ("(Ljava/io/File;)V", False), ("(Ljava/io/File;Ljava/nio/charset/Charset;)V", False), ("(Ljava/io/File;Ljava/lang/String;)V", False), ("(Ljava/io/Writer;)V", False), ("(Ljava/io/Writer;Z)V", False), ("(Ljava/io/OutputStream;ZLjava/nio/charset/Charset;)V", False), ("(Ljava/io/OutputStream;Z)V", False), ("(Ljava/io/OutputStream;)V", False)]
    println = JavaMultipleMethod([("(D)V", False, False), ("(F)V", False, False), ("(J)V", False, False), ("([C)V", False, False), ("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/Object;)V", False, False), ("()V", False, False), ("(Z)V", False, False), ("(C)V", False, False), ("(I)V", False, False)])
    append = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/lang/Appendable;", False, False), ("(C)Ljava/io/PrintWriter;", False, False), ("(C)Ljava/io/Writer;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/CharSequence;)Ljava/io/Writer;", False, False), ("(C)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/io/Writer;", False, False), ("(Ljava/lang/CharSequence;)Ljava/io/PrintWriter;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/io/PrintWriter;", False, False)])
    flush = JavaMethod("()V")
    format = JavaMultipleMethod([("(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintWriter;", False, True), ("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintWriter;", False, True)])
    close = JavaMethod("()V")
    print = JavaMultipleMethod([("(F)V", False, False), ("(J)V", False, False), ("(I)V", False, False), ("(C)V", False, False), ("(Z)V", False, False), ("(Ljava/lang/Object;)V", False, False), ("(Ljava/lang/String;)V", False, False), ("([C)V", False, False), ("(D)V", False, False)])
    write = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("([C)V", False, False), ("(Ljava/lang/String;II)V", False, False), ("([CII)V", False, False), ("(I)V", False, False)])
    printf = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintWriter;", False, True), ("(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintWriter;", False, True)])
    checkError = JavaMethod("()Z")