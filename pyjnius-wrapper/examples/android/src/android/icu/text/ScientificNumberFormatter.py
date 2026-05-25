from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScientificNumberFormatter"]

class ScientificNumberFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/ScientificNumberFormatter"
    getSuperscriptInstance = JavaMultipleMethod([("(Landroid/icu/util/ULocale;)Landroid/icu/text/ScientificNumberFormatter;", True, False), ("(Landroid/icu/text/DecimalFormat;)Landroid/icu/text/ScientificNumberFormatter;", True, False)])
    getMarkupInstance = JavaMultipleMethod([("(Landroid/icu/util/ULocale;Ljava/lang/String;Ljava/lang/String;)Landroid/icu/text/ScientificNumberFormatter;", True, False), ("(Landroid/icu/text/DecimalFormat;Ljava/lang/String;Ljava/lang/String;)Landroid/icu/text/ScientificNumberFormatter;", True, False)])
    format = JavaMethod("(Ljava/lang/Object;)Ljava/lang/String;")