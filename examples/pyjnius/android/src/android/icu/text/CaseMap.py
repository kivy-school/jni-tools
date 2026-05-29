from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CaseMap"]

class CaseMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/CaseMap"
    toTitle = JavaStaticMethod("()Landroid/icu/text/CaseMap$Title;")
    omitUnchangedText = JavaMethod("()Landroid/icu/text/CaseMap;")
    toLower = JavaStaticMethod("()Landroid/icu/text/CaseMap$Lower;")
    fold = JavaStaticMethod("()Landroid/icu/text/CaseMap$Fold;")
    toUpper = JavaStaticMethod("()Landroid/icu/text/CaseMap$Upper;")

    class Upper(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/CaseMap$Upper"
        omitUnchangedText = JavaMultipleMethod([("()Landroid/icu/text/CaseMap;", False, False), ("()Landroid/icu/text/CaseMap$Upper;", False, False)])
        apply = JavaMultipleMethod([("(Ljava/util/Locale;Ljava/lang/CharSequence;)Ljava/lang/String;", False, False), ("(Ljava/util/Locale;Ljava/lang/CharSequence;Ljava/lang/Appendable;Landroid/icu/text/Edits;)Ljava/lang/Appendable;", False, False)])

    class Title(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/CaseMap$Title"
        adjustToCased = JavaMethod("()Landroid/icu/text/CaseMap$Title;")
        omitUnchangedText = JavaMultipleMethod([("()Landroid/icu/text/CaseMap$Title;", False, False), ("()Landroid/icu/text/CaseMap;", False, False)])
        noBreakAdjustment = JavaMethod("()Landroid/icu/text/CaseMap$Title;")
        noLowercase = JavaMethod("()Landroid/icu/text/CaseMap$Title;")
        sentences = JavaMethod("()Landroid/icu/text/CaseMap$Title;")
        wholeString = JavaMethod("()Landroid/icu/text/CaseMap$Title;")
        apply = JavaMultipleMethod([("(Ljava/util/Locale;Landroid/icu/text/BreakIterator;Ljava/lang/CharSequence;)Ljava/lang/String;", False, False), ("(Ljava/util/Locale;Landroid/icu/text/BreakIterator;Ljava/lang/CharSequence;Ljava/lang/Appendable;Landroid/icu/text/Edits;)Ljava/lang/Appendable;", False, False)])

    class Lower(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/CaseMap$Lower"
        omitUnchangedText = JavaMultipleMethod([("()Landroid/icu/text/CaseMap;", False, False), ("()Landroid/icu/text/CaseMap$Lower;", False, False)])
        apply = JavaMultipleMethod([("(Ljava/util/Locale;Ljava/lang/CharSequence;)Ljava/lang/String;", False, False), ("(Ljava/util/Locale;Ljava/lang/CharSequence;Ljava/lang/Appendable;Landroid/icu/text/Edits;)Ljava/lang/Appendable;", False, False)])

    class Fold(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/CaseMap$Fold"
        omitUnchangedText = JavaMultipleMethod([("()Landroid/icu/text/CaseMap;", False, False), ("()Landroid/icu/text/CaseMap$Fold;", False, False)])
        turkic = JavaMethod("()Landroid/icu/text/CaseMap$Fold;")
        apply = JavaMultipleMethod([("(Ljava/lang/CharSequence;Ljava/lang/Appendable;Landroid/icu/text/Edits;)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/CharSequence;)Ljava/lang/String;", False, False)])