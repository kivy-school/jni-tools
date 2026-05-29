from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScientificNumberFormatter"]

class ScientificNumberFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/ScientificNumberFormatter"
    getMarkupInstance = JavaMultipleMethod([("(Landroid/icu/text/DecimalFormat;Ljava/lang/String;Ljava/lang/String;)Landroid/icu/text/ScientificNumberFormatter;", True, False), ("(Landroid/icu/util/ULocale;Ljava/lang/String;Ljava/lang/String;)Landroid/icu/text/ScientificNumberFormatter;", True, False)])
    getSuperscriptInstance = JavaMultipleMethod([("(Landroid/icu/text/DecimalFormat;)Landroid/icu/text/ScientificNumberFormatter;", True, False), ("(Landroid/icu/util/ULocale;)Landroid/icu/text/ScientificNumberFormatter;", True, False)])
    format = JavaMethod("(Ljava/lang/Object;)Ljava/lang/String;")