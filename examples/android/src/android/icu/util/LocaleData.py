from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocaleData"]

class LocaleData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/LocaleData"
    ALT_QUOTATION_END = JavaStaticField("I")
    ALT_QUOTATION_START = JavaStaticField("I")
    QUOTATION_END = JavaStaticField("I")
    QUOTATION_START = JavaStaticField("I")
    getInstance = JavaMultipleMethod([("(Landroid/icu/util/ULocale;)Landroid/icu/util/LocaleData;", True, False), ("()Landroid/icu/util/LocaleData;", True, False)])
    setNoSubstitute = JavaMethod("(Z)V")
    getNoSubstitute = JavaMethod("()Z")
    getDelimiter = JavaMethod("(I)Ljava/lang/String;")
    getMeasurementSystem = JavaStaticMethod("(Landroid/icu/util/ULocale;)Landroid/icu/util/LocaleData$MeasurementSystem;")
    getPaperSize = JavaStaticMethod("(Landroid/icu/util/ULocale;)Landroid/icu/util/LocaleData$PaperSize;")
    getCLDRVersion = JavaStaticMethod("()Landroid/icu/util/VersionInfo;")

    class MeasurementSystem(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/util/LocaleData/MeasurementSystem"
        SI = JavaStaticField("Landroid/icu/util/LocaleData$MeasurementSystem;")
        UK = JavaStaticField("Landroid/icu/util/LocaleData$MeasurementSystem;")
        US = JavaStaticField("Landroid/icu/util/LocaleData$MeasurementSystem;")

    class PaperSize(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/util/LocaleData/PaperSize"
        getHeight = JavaMethod("()I")
        getWidth = JavaMethod("()I")