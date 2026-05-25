from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ListFormatter"]

class ListFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/ListFormatter"
    getInstance = JavaMultipleMethod([("(Landroid/icu/util/ULocale;Landroid/icu/text/ListFormatter$Type;Landroid/icu/text/ListFormatter$Width;)Landroid/icu/text/ListFormatter;", True, False), ("(Ljava/util/Locale;Landroid/icu/text/ListFormatter$Type;Landroid/icu/text/ListFormatter$Width;)Landroid/icu/text/ListFormatter;", True, False), ("(Landroid/icu/util/ULocale;)Landroid/icu/text/ListFormatter;", True, False), ("(Ljava/util/Locale;)Landroid/icu/text/ListFormatter;", True, False), ("()Landroid/icu/text/ListFormatter;", True, False)])
    format = JavaMultipleMethod([("([Ljava/lang/Object;)Ljava/lang/String;", False, True), ("(Ljava/util/Collection;)Ljava/lang/String;", False, False)])
    formatToValue = JavaMultipleMethod([("([Ljava/lang/Object;)Landroid/icu/text/ListFormatter$FormattedList;", False, True), ("(Ljava/util/Collection;)Landroid/icu/text/ListFormatter$FormattedList;", False, False)])
    getPatternForNumItems = JavaMethod("(I)Ljava/lang/String;")

    class FormattedList(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/ListFormatter/FormattedList"
        toString = JavaMethod("()Ljava/lang/String;")
        length = JavaMethod("()I")
        charAt = JavaMethod("(I)C")
        subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
        appendTo = JavaMethod("(Ljava/lang/Appendable;)Ljava/lang/Appendable;")
        nextPosition = JavaMethod("(Landroid/icu/text/ConstrainedFieldPosition;)Z")
        toCharacterIterator = JavaMethod("()Ljava/text/AttributedCharacterIterator;")

    class Type(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/ListFormatter/Type"
        values = JavaStaticMethod("()[Landroid/icu/text/ListFormatter$Type;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/ListFormatter$Type;")
        AND = JavaStaticField("Landroid/icu/text/ListFormatter/Type;")
        OR = JavaStaticField("Landroid/icu/text/ListFormatter/Type;")
        UNITS = JavaStaticField("Landroid/icu/text/ListFormatter/Type;")

    class Width(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/ListFormatter/Width"
        values = JavaStaticMethod("()[Landroid/icu/text/ListFormatter$Width;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/ListFormatter$Width;")
        WIDE = JavaStaticField("Landroid/icu/text/ListFormatter/Width;")
        SHORT = JavaStaticField("Landroid/icu/text/ListFormatter/Width;")
        NARROW = JavaStaticField("Landroid/icu/text/ListFormatter/Width;")