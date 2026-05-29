from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocaleData"]

class LocaleData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/LocaleData"
    ALT_QUOTATION_END = JavaStaticField("I")
    ALT_QUOTATION_START = JavaStaticField("I")
    QUOTATION_END = JavaStaticField("I")
    QUOTATION_START = JavaStaticField("I")
    getCLDRVersion = JavaStaticMethod("()Landroid/icu/util/VersionInfo;")
    getDelimiter = JavaMethod("(I)Ljava/lang/String;")
    getMeasurementSystem = JavaStaticMethod("(Landroid/icu/util/ULocale;)Landroid/icu/util/LocaleData$MeasurementSystem;")
    getNoSubstitute = JavaMethod("()Z")
    getPaperSize = JavaStaticMethod("(Landroid/icu/util/ULocale;)Landroid/icu/util/LocaleData$PaperSize;")
    setNoSubstitute = JavaMethod("(Z)V")
    getInstance = JavaMultipleMethod([("()Landroid/icu/util/LocaleData;", True, False), ("(Landroid/icu/util/ULocale;)Landroid/icu/util/LocaleData;", True, False)])

    class PaperSize(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/util/LocaleData$PaperSize"
        getHeight = JavaMethod("()I")
        getWidth = JavaMethod("()I")

    class MeasurementSystem(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/util/LocaleData$MeasurementSystem"
        SI = JavaStaticField("Landroid/icu/util/LocaleData$MeasurementSystem;")
        UK = JavaStaticField("Landroid/icu/util/LocaleData$MeasurementSystem;")
        US = JavaStaticField("Landroid/icu/util/LocaleData$MeasurementSystem;")