from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Normalizer2"]

class Normalizer2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/Normalizer2"
    getNFCInstance = JavaStaticMethod("()Landroid/icu/text/Normalizer2;")
    getNFDInstance = JavaStaticMethod("()Landroid/icu/text/Normalizer2;")
    getNFKCInstance = JavaStaticMethod("()Landroid/icu/text/Normalizer2;")
    getNFKDInstance = JavaStaticMethod("()Landroid/icu/text/Normalizer2;")
    getNFKCCasefoldInstance = JavaStaticMethod("()Landroid/icu/text/Normalizer2;")
    getInstance = JavaStaticMethod("(Ljava/io/InputStream;Ljava/lang/String;Landroid/icu/text/Normalizer2$Mode;)Landroid/icu/text/Normalizer2;")
    normalize = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/lang/String;", False, False), ("(Ljava/lang/CharSequence;Ljava/lang/StringBuilder;)Ljava/lang/StringBuilder;", False, False), ("(Ljava/lang/CharSequence;Ljava/lang/Appendable;)Ljava/lang/Appendable;", False, False)])
    normalizeSecondAndAppend = JavaMethod("(Ljava/lang/StringBuilder;Ljava/lang/CharSequence;)Ljava/lang/StringBuilder;")
    append = JavaMethod("(Ljava/lang/StringBuilder;Ljava/lang/CharSequence;)Ljava/lang/StringBuilder;")
    getDecomposition = JavaMethod("(I)Ljava/lang/String;")
    getRawDecomposition = JavaMethod("(I)Ljava/lang/String;")
    composePair = JavaMethod("(II)I")
    getCombiningClass = JavaMethod("(I)I")
    isNormalized = JavaMethod("(Ljava/lang/CharSequence;)Z")
    quickCheck = JavaMethod("(Ljava/lang/CharSequence;)Landroid/icu/text/Normalizer$QuickCheckResult;")
    spanQuickCheckYes = JavaMethod("(Ljava/lang/CharSequence;)I")
    hasBoundaryBefore = JavaMethod("(I)Z")
    hasBoundaryAfter = JavaMethod("(I)Z")
    isInert = JavaMethod("(I)Z")

    class Mode(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/Normalizer2/Mode"
        values = JavaStaticMethod("()[Landroid/icu/text/Normalizer2$Mode;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/Normalizer2$Mode;")
        COMPOSE = JavaStaticField("Landroid/icu/text/Normalizer2/Mode;")
        DECOMPOSE = JavaStaticField("Landroid/icu/text/Normalizer2/Mode;")
        FCD = JavaStaticField("Landroid/icu/text/Normalizer2/Mode;")
        COMPOSE_CONTIGUOUS = JavaStaticField("Landroid/icu/text/Normalizer2/Mode;")