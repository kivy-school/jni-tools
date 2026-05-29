from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Normalizer2"]

class Normalizer2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/Normalizer2"
    isNormalized = JavaMethod("(Ljava/lang/CharSequence;)Z")
    spanQuickCheckYes = JavaMethod("(Ljava/lang/CharSequence;)I")
    getCombiningClass = JavaMethod("(I)I")
    append = JavaMethod("(Ljava/lang/StringBuilder;Ljava/lang/CharSequence;)Ljava/lang/StringBuilder;")
    getInstance = JavaStaticMethod("(Ljava/io/InputStream;Ljava/lang/String;Landroid/icu/text/Normalizer2$Mode;)Landroid/icu/text/Normalizer2;")
    normalize = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/lang/String;", False, False), ("(Ljava/lang/CharSequence;Ljava/lang/StringBuilder;)Ljava/lang/StringBuilder;", False, False), ("(Ljava/lang/CharSequence;Ljava/lang/Appendable;)Ljava/lang/Appendable;", False, False)])
    getNFDInstance = JavaStaticMethod("()Landroid/icu/text/Normalizer2;")
    getNFCInstance = JavaStaticMethod("()Landroid/icu/text/Normalizer2;")
    hasBoundaryAfter = JavaMethod("(I)Z")
    composePair = JavaMethod("(II)I")
    getDecomposition = JavaMethod("(I)Ljava/lang/String;")
    hasBoundaryBefore = JavaMethod("(I)Z")
    getNFKCInstance = JavaStaticMethod("()Landroid/icu/text/Normalizer2;")
    getNFKDInstance = JavaStaticMethod("()Landroid/icu/text/Normalizer2;")
    getNFKCCasefoldInstance = JavaStaticMethod("()Landroid/icu/text/Normalizer2;")
    getNFKCSimpleCasefoldInstance = JavaStaticMethod("()Landroid/icu/text/Normalizer2;")
    getRawDecomposition = JavaMethod("(I)Ljava/lang/String;")
    isInert = JavaMethod("(I)Z")
    quickCheck = JavaMethod("(Ljava/lang/CharSequence;)Landroid/icu/text/Normalizer$QuickCheckResult;")
    normalizeSecondAndAppend = JavaMethod("(Ljava/lang/StringBuilder;Ljava/lang/CharSequence;)Ljava/lang/StringBuilder;")

    class Mode(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/Normalizer2$Mode"
        COMPOSE = JavaStaticField("Landroid/icu/text/Normalizer2$Mode;")
        COMPOSE_CONTIGUOUS = JavaStaticField("Landroid/icu/text/Normalizer2$Mode;")
        DECOMPOSE = JavaStaticField("Landroid/icu/text/Normalizer2$Mode;")
        FCD = JavaStaticField("Landroid/icu/text/Normalizer2$Mode;")
        values = JavaStaticMethod("()[Landroid/icu/text/Normalizer2$Mode;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/Normalizer2$Mode;")
        COMPOSE = JavaStaticField("Landroid/icu/text/Normalizer2$Mode;")
        COMPOSE_CONTIGUOUS = JavaStaticField("Landroid/icu/text/Normalizer2$Mode;")
        DECOMPOSE = JavaStaticField("Landroid/icu/text/Normalizer2$Mode;")
        FCD = JavaStaticField("Landroid/icu/text/Normalizer2$Mode;")