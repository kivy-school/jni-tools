from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DateIntervalInfo"]

class DateIntervalInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/DateIntervalInfo"
    __javaconstructor__ = [("(Landroid/icu/util/ULocale;)V", False), ("(Ljava/util/Locale;)V", False)]
    setIntervalPattern = JavaMethod("(Ljava/lang/String;ILjava/lang/String;)V")
    getIntervalPattern = JavaMethod("(Ljava/lang/String;I)Landroid/icu/text/DateIntervalInfo$PatternInfo;")
    getFallbackIntervalPattern = JavaMethod("()Ljava/lang/String;")
    setFallbackIntervalPattern = JavaMethod("(Ljava/lang/String;)V")
    getDefaultOrder = JavaMethod("()Z")
    clone = JavaMethod("()Ljava/lang/Object;")
    isFrozen = JavaMethod("()Z")
    freeze = JavaMethod("()Landroid/icu/text/DateIntervalInfo;")
    cloneAsThawed = JavaMethod("()Landroid/icu/text/DateIntervalInfo;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class PatternInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/DateIntervalInfo/PatternInfo"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Z)V", False)]
        getFirstPart = JavaMethod("()Ljava/lang/String;")
        getSecondPart = JavaMethod("()Ljava/lang/String;")
        firstDateInPtnIsLaterDate = JavaMethod("()Z")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")