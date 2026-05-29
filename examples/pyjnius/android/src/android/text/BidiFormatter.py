from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BidiFormatter"]

class BidiFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/BidiFormatter"
    getStereoReset = JavaMethod("()Z")
    unicodeWrap = JavaMultipleMethod([("(Ljava/lang/String;Landroid/text/TextDirectionHeuristic;Z)Ljava/lang/String;", False, False), ("(Ljava/lang/CharSequence;Landroid/text/TextDirectionHeuristic;Z)Ljava/lang/CharSequence;", False, False), ("(Ljava/lang/CharSequence;Landroid/text/TextDirectionHeuristic;)Ljava/lang/CharSequence;", False, False), ("(Ljava/lang/String;Z)Ljava/lang/String;", False, False), ("(Ljava/lang/CharSequence;Z)Ljava/lang/CharSequence;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Landroid/text/TextDirectionHeuristic;)Ljava/lang/String;", False, False), ("(Ljava/lang/CharSequence;)Ljava/lang/CharSequence;", False, False)])
    isRtlContext = JavaMethod("()Z")
    getInstance = JavaMultipleMethod([("(Z)Landroid/text/BidiFormatter;", True, False), ("()Landroid/text/BidiFormatter;", True, False), ("(Ljava/util/Locale;)Landroid/text/BidiFormatter;", True, False)])
    isRtl = JavaMultipleMethod([("(Ljava/lang/String;)Z", False, False), ("(Ljava/lang/CharSequence;)Z", False, False)])

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/BidiFormatter$Builder"
        __javaconstructor__ = [("()V", False), ("(Ljava/util/Locale;)V", False), ("(Z)V", False)]
        setTextDirectionHeuristic = JavaMethod("(Landroid/text/TextDirectionHeuristic;)Landroid/text/BidiFormatter$Builder;")
        build = JavaMethod("()Landroid/text/BidiFormatter;")
        stereoReset = JavaMethod("(Z)Landroid/text/BidiFormatter$Builder;")