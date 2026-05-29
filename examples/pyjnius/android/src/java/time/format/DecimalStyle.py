from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DecimalStyle"]

class DecimalStyle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/format/DecimalStyle"
    STANDARD = JavaStaticField("Ljava/time/format/DecimalStyle;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    of = JavaStaticMethod("(Ljava/util/Locale;)Ljava/time/format/DecimalStyle;")
    getAvailableLocales = JavaStaticMethod("()Ljava/util/Set;")
    getPositiveSign = JavaMethod("()C")
    getNegativeSign = JavaMethod("()C")
    ofDefaultLocale = JavaStaticMethod("()Ljava/time/format/DecimalStyle;")
    withZeroDigit = JavaMethod("(C)Ljava/time/format/DecimalStyle;")
    withPositiveSign = JavaMethod("(C)Ljava/time/format/DecimalStyle;")
    withNegativeSign = JavaMethod("(C)Ljava/time/format/DecimalStyle;")
    withDecimalSeparator = JavaMethod("(C)Ljava/time/format/DecimalStyle;")
    getZeroDigit = JavaMethod("()C")
    getDecimalSeparator = JavaMethod("()C")