from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlphabeticIndex"]

class AlphabeticIndex(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/AlphabeticIndex"
    __javaconstructor__ = [("(Landroid/icu/text/RuleBasedCollator;)V", False), ("(Landroid/icu/util/ULocale;)V", False), ("(Ljava/util/Locale;)V", False)]
    getCollator = JavaMethod("()Landroid/icu/text/RuleBasedCollator;")
    buildImmutableIndex = JavaMethod("()Landroid/icu/text/AlphabeticIndex$ImmutableIndex;")
    addLabels = JavaMultipleMethod([("(Landroid/icu/text/UnicodeSet;)Landroid/icu/text/AlphabeticIndex;", False, False), ("([Ljava/util/Locale;)Landroid/icu/text/AlphabeticIndex;", False, True), ("([Landroid/icu/util/ULocale;)Landroid/icu/text/AlphabeticIndex;", False, True)])
    clearRecords = JavaMethod("()Landroid/icu/text/AlphabeticIndex;")
    getBucketCount = JavaMethod("()I")
    getBucketIndex = JavaMethod("(Ljava/lang/CharSequence;)I")
    getBucketLabels = JavaMethod("()Ljava/util/List;")
    getInflowLabel = JavaMethod("()Ljava/lang/String;")
    getMaxLabelCount = JavaMethod("()I")
    getOverflowLabel = JavaMethod("()Ljava/lang/String;")
    getUnderflowLabel = JavaMethod("()Ljava/lang/String;")
    addRecord = JavaMethod("(Ljava/lang/CharSequence;Ljava/lang/Object;)Landroid/icu/text/AlphabeticIndex;")
    setInflowLabel = JavaMethod("(Ljava/lang/String;)Landroid/icu/text/AlphabeticIndex;")
    setMaxLabelCount = JavaMethod("(I)Landroid/icu/text/AlphabeticIndex;")
    setOverflowLabel = JavaMethod("(Ljava/lang/String;)Landroid/icu/text/AlphabeticIndex;")
    setUnderflowLabel = JavaMethod("(Ljava/lang/String;)Landroid/icu/text/AlphabeticIndex;")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    getRecordCount = JavaMethod("()I")

    class Record(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/AlphabeticIndex$Record"
        getName = JavaMethod("()Ljava/lang/CharSequence;")
        toString = JavaMethod("()Ljava/lang/String;")
        getData = JavaMethod("()Ljava/lang/Object;")

    class ImmutableIndex(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/AlphabeticIndex$ImmutableIndex"
        getBucketCount = JavaMethod("()I")
        getBucketIndex = JavaMethod("(Ljava/lang/CharSequence;)I")
        iterator = JavaMethod("()Ljava/util/Iterator;")
        getBucket = JavaMethod("(I)Landroid/icu/text/AlphabeticIndex$Bucket;")

    class Bucket(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/AlphabeticIndex$Bucket"
        getLabelType = JavaMethod("()Landroid/icu/text/AlphabeticIndex$Bucket$LabelType;")
        size = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")
        iterator = JavaMethod("()Ljava/util/Iterator;")
        getLabel = JavaMethod("()Ljava/lang/String;")

        class LabelType(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/icu/text/AlphabeticIndex$Bucket$LabelType"
            INFLOW = JavaStaticField("Landroid/icu/text/AlphabeticIndex$Bucket$LabelType;")
            NORMAL = JavaStaticField("Landroid/icu/text/AlphabeticIndex$Bucket$LabelType;")
            OVERFLOW = JavaStaticField("Landroid/icu/text/AlphabeticIndex$Bucket$LabelType;")
            UNDERFLOW = JavaStaticField("Landroid/icu/text/AlphabeticIndex$Bucket$LabelType;")
            values = JavaStaticMethod("()[Landroid/icu/text/AlphabeticIndex$Bucket$LabelType;")
            valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/AlphabeticIndex$Bucket$LabelType;")
            INFLOW = JavaStaticField("Landroid/icu/text/AlphabeticIndex$Bucket$LabelType;")
            NORMAL = JavaStaticField("Landroid/icu/text/AlphabeticIndex$Bucket$LabelType;")
            OVERFLOW = JavaStaticField("Landroid/icu/text/AlphabeticIndex$Bucket$LabelType;")
            UNDERFLOW = JavaStaticField("Landroid/icu/text/AlphabeticIndex$Bucket$LabelType;")