from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Formatter"]

class Formatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Formatter"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/Appendable;)V", False), ("(Ljava/util/Locale;)V", False), ("(Ljava/lang/Appendable;Ljava/util/Locale;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Locale;)V", False), ("(Ljava/lang/String;Ljava/nio/charset/Charset;Ljava/util/Locale;)V", False), ("(Ljava/io/File;)V", False), ("(Ljava/io/File;Ljava/lang/String;)V", False), ("(Ljava/io/File;Ljava/lang/String;Ljava/util/Locale;)V", False), ("(Ljava/io/File;Ljava/nio/charset/Charset;Ljava/util/Locale;)V", False), ("(Ljava/io/PrintStream;)V", False), ("(Ljava/io/OutputStream;)V", False), ("(Ljava/io/OutputStream;Ljava/lang/String;)V", False), ("(Ljava/io/OutputStream;Ljava/lang/String;Ljava/util/Locale;)V", False), ("(Ljava/io/OutputStream;Ljava/nio/charset/Charset;Ljava/util/Locale;)V", False)]
    locale = JavaMethod("()Ljava/util/Locale;")
    out = JavaMethod("()Ljava/lang/Appendable;")
    toString = JavaMethod("()Ljava/lang/String;")
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    ioException = JavaMethod("()Ljava/io/IOException;")
    format = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/util/Formatter;", False, True), ("(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/util/Formatter;", False, True)])

    class BigDecimalLayoutForm(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Formatter/BigDecimalLayoutForm"
        values = JavaStaticMethod("()[Ljava/util/Formatter$BigDecimalLayoutForm;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/Formatter$BigDecimalLayoutForm;")
        SCIENTIFIC = JavaStaticField("Ljava/util/Formatter/BigDecimalLayoutForm;")
        DECIMAL_FLOAT = JavaStaticField("Ljava/util/Formatter/BigDecimalLayoutForm;")