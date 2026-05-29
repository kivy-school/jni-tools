from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlphabeticIndex"]

class AlphabeticIndex(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/AlphabeticIndex"
    __javaconstructor__ = [("(Landroid/icu/util/ULocale;)V", False), ("(Ljava/util/Locale;)V", False), ("(Landroid/icu/text/RuleBasedCollator;)V", False)]
    addLabels = JavaMultipleMethod([("(Landroid/icu/text/UnicodeSet;)Landroid/icu/text/AlphabeticIndex;", False, False), ("([Landroid/icu/util/ULocale;)Landroid/icu/text/AlphabeticIndex;", False, True), ("([Ljava/util/Locale;)Landroid/icu/text/AlphabeticIndex;", False, True)])
    setOverflowLabel = JavaMethod("(Ljava/lang/String;)Landroid/icu/text/AlphabeticIndex;")
    getUnderflowLabel = JavaMethod("()Ljava/lang/String;")
    setUnderflowLabel = JavaMethod("(Ljava/lang/String;)Landroid/icu/text/AlphabeticIndex;")
    getOverflowLabel = JavaMethod("()Ljava/lang/String;")
    setInflowLabel = JavaMethod("(Ljava/lang/String;)Landroid/icu/text/AlphabeticIndex;")
    getInflowLabel = JavaMethod("()Ljava/lang/String;")
    getMaxLabelCount = JavaMethod("()I")
    setMaxLabelCount = JavaMethod("(I)Landroid/icu/text/AlphabeticIndex;")
    buildImmutableIndex = JavaMethod("()Landroid/icu/text/AlphabeticIndex$ImmutableIndex;")
    getBucketLabels = JavaMethod("()Ljava/util/List;")
    getCollator = JavaMethod("()Landroid/icu/text/RuleBasedCollator;")
    addRecord = JavaMethod("(Ljava/lang/CharSequence;Ljava/lang/Object;)Landroid/icu/text/AlphabeticIndex;")
    getBucketIndex = JavaMethod("(Ljava/lang/CharSequence;)I")
    clearRecords = JavaMethod("()Landroid/icu/text/AlphabeticIndex;")
    getBucketCount = JavaMethod("()I")
    getRecordCount = JavaMethod("()I")
    iterator = JavaMethod("()Ljava/util/Iterator;")

    class Bucket(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/AlphabeticIndex/Bucket"
        getLabel = JavaMethod("()Ljava/lang/String;")
        getLabelType = JavaMethod("()Landroid/icu/text/AlphabeticIndex$Bucket$LabelType;")
        size = JavaMethod("()I")
        iterator = JavaMethod("()Ljava/util/Iterator;")
        toString = JavaMethod("()Ljava/lang/String;")

        class LabelType(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/icu/text/AlphabeticIndex/Bucket/LabelType"
            values = JavaStaticMethod("()[Landroid/icu/text/AlphabeticIndex$Bucket$LabelType;")
            valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/AlphabeticIndex$Bucket$LabelType;")
            NORMAL = JavaStaticField("Landroid/icu/text/AlphabeticIndex/Bucket/LabelType;")
            UNDERFLOW = JavaStaticField("Landroid/icu/text/AlphabeticIndex/Bucket/LabelType;")
            INFLOW = JavaStaticField("Landroid/icu/text/AlphabeticIndex/Bucket/LabelType;")
            OVERFLOW = JavaStaticField("Landroid/icu/text/AlphabeticIndex/Bucket/LabelType;")

    class ImmutableIndex(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/AlphabeticIndex/ImmutableIndex"
        getBucketCount = JavaMethod("()I")
        getBucketIndex = JavaMethod("(Ljava/lang/CharSequence;)I")
        getBucket = JavaMethod("(I)Landroid/icu/text/AlphabeticIndex$Bucket;")
        iterator = JavaMethod("()Ljava/util/Iterator;")

    class Record(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/AlphabeticIndex/Record"
        getName = JavaMethod("()Ljava/lang/CharSequence;")
        getData = JavaMethod("()Ljava/lang/Object;")
        toString = JavaMethod("()Ljava/lang/String;")