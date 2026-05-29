from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CaseMap"]

class CaseMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/CaseMap"
    toLower = JavaStaticMethod("()Landroid/icu/text/CaseMap$Lower;")
    toUpper = JavaStaticMethod("()Landroid/icu/text/CaseMap$Upper;")
    toTitle = JavaStaticMethod("()Landroid/icu/text/CaseMap$Title;")
    fold = JavaStaticMethod("()Landroid/icu/text/CaseMap$Fold;")
    omitUnchangedText = JavaMethod("()Landroid/icu/text/CaseMap;")

    class Fold(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/CaseMap/Fold"
        omitUnchangedText = JavaMethod("()Landroid/icu/text/CaseMap$Fold;")
        turkic = JavaMethod("()Landroid/icu/text/CaseMap$Fold;")
        apply = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/lang/String;", False, False), ("(Ljava/lang/CharSequence;Ljava/lang/Appendable;Landroid/icu/text/Edits;)Ljava/lang/Appendable;", False, False)])

    class Lower(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/CaseMap/Lower"
        omitUnchangedText = JavaMethod("()Landroid/icu/text/CaseMap$Lower;")
        apply = JavaMultipleMethod([("(Ljava/util/Locale;Ljava/lang/CharSequence;)Ljava/lang/String;", False, False), ("(Ljava/util/Locale;Ljava/lang/CharSequence;Ljava/lang/Appendable;Landroid/icu/text/Edits;)Ljava/lang/Appendable;", False, False)])

    class Title(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/CaseMap/Title"
        wholeString = JavaMethod("()Landroid/icu/text/CaseMap$Title;")
        sentences = JavaMethod("()Landroid/icu/text/CaseMap$Title;")
        omitUnchangedText = JavaMethod("()Landroid/icu/text/CaseMap$Title;")
        noLowercase = JavaMethod("()Landroid/icu/text/CaseMap$Title;")
        noBreakAdjustment = JavaMethod("()Landroid/icu/text/CaseMap$Title;")
        adjustToCased = JavaMethod("()Landroid/icu/text/CaseMap$Title;")
        apply = JavaMultipleMethod([("(Ljava/util/Locale;Landroid/icu/text/BreakIterator;Ljava/lang/CharSequence;)Ljava/lang/String;", False, False), ("(Ljava/util/Locale;Landroid/icu/text/BreakIterator;Ljava/lang/CharSequence;Ljava/lang/Appendable;Landroid/icu/text/Edits;)Ljava/lang/Appendable;", False, False)])

    class Upper(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/CaseMap/Upper"
        omitUnchangedText = JavaMethod("()Landroid/icu/text/CaseMap$Upper;")
        apply = JavaMultipleMethod([("(Ljava/util/Locale;Ljava/lang/CharSequence;)Ljava/lang/String;", False, False), ("(Ljava/util/Locale;Ljava/lang/CharSequence;Ljava/lang/Appendable;Landroid/icu/text/Edits;)Ljava/lang/Appendable;", False, False)])