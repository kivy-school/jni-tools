from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DecimalStyle"]

class DecimalStyle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/format/DecimalStyle"
    STANDARD = JavaStaticField("Ljava/time/format/DecimalStyle;")
    getAvailableLocales = JavaStaticMethod("()Ljava/util/Set;")
    ofDefaultLocale = JavaStaticMethod("()Ljava/time/format/DecimalStyle;")
    of = JavaStaticMethod("(Ljava/util/Locale;)Ljava/time/format/DecimalStyle;")
    getZeroDigit = JavaMethod("()C")
    withZeroDigit = JavaMethod("(C)Ljava/time/format/DecimalStyle;")
    getPositiveSign = JavaMethod("()C")
    withPositiveSign = JavaMethod("(C)Ljava/time/format/DecimalStyle;")
    getNegativeSign = JavaMethod("()C")
    withNegativeSign = JavaMethod("(C)Ljava/time/format/DecimalStyle;")
    getDecimalSeparator = JavaMethod("()C")
    withDecimalSeparator = JavaMethod("(C)Ljava/time/format/DecimalStyle;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")