from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnicodeSetSpanner"]

class UnicodeSetSpanner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/UnicodeSetSpanner"
    __javaconstructor__ = [("(Landroid/icu/text/UnicodeSet;)V", False)]
    getUnicodeSet = JavaMethod("()Landroid/icu/text/UnicodeSet;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    countIn = JavaMultipleMethod([("(Ljava/lang/CharSequence;)I", False, False), ("(Ljava/lang/CharSequence;Landroid/icu/text/UnicodeSetSpanner$CountMethod;)I", False, False), ("(Ljava/lang/CharSequence;Landroid/icu/text/UnicodeSetSpanner$CountMethod;Landroid/icu/text/UnicodeSet$SpanCondition;)I", False, False)])
    deleteFrom = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/lang/String;", False, False), ("(Ljava/lang/CharSequence;Landroid/icu/text/UnicodeSet$SpanCondition;)Ljava/lang/String;", False, False)])
    replaceFrom = JavaMultipleMethod([("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;", False, False), ("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;Landroid/icu/text/UnicodeSetSpanner$CountMethod;)Ljava/lang/String;", False, False), ("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;Landroid/icu/text/UnicodeSetSpanner$CountMethod;Landroid/icu/text/UnicodeSet$SpanCondition;)Ljava/lang/String;", False, False)])
    trim = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/lang/CharSequence;", False, False), ("(Ljava/lang/CharSequence;Landroid/icu/text/UnicodeSetSpanner$TrimOption;)Ljava/lang/CharSequence;", False, False), ("(Ljava/lang/CharSequence;Landroid/icu/text/UnicodeSetSpanner$TrimOption;Landroid/icu/text/UnicodeSet$SpanCondition;)Ljava/lang/CharSequence;", False, False)])

    class CountMethod(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/UnicodeSetSpanner/CountMethod"
        values = JavaStaticMethod("()[Landroid/icu/text/UnicodeSetSpanner$CountMethod;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/UnicodeSetSpanner$CountMethod;")
        WHOLE_SPAN = JavaStaticField("Landroid/icu/text/UnicodeSetSpanner/CountMethod;")
        MIN_ELEMENTS = JavaStaticField("Landroid/icu/text/UnicodeSetSpanner/CountMethod;")

    class TrimOption(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/UnicodeSetSpanner/TrimOption"
        values = JavaStaticMethod("()[Landroid/icu/text/UnicodeSetSpanner$TrimOption;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/UnicodeSetSpanner$TrimOption;")
        LEADING = JavaStaticField("Landroid/icu/text/UnicodeSetSpanner/TrimOption;")
        BOTH = JavaStaticField("Landroid/icu/text/UnicodeSetSpanner/TrimOption;")
        TRAILING = JavaStaticField("Landroid/icu/text/UnicodeSetSpanner/TrimOption;")