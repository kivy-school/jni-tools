from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DateIntervalInfo"]

class DateIntervalInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/DateIntervalInfo"
    __javaconstructor__ = [("(Ljava/util/Locale;)V", False), ("(Landroid/icu/util/ULocale;)V", False)]
    cloneAsThawed = JavaMultipleMethod([("()Landroid/icu/text/DateIntervalInfo;", False, False), ("()Ljava/lang/Object;", False, False)])
    setIntervalPattern = JavaMethod("(Ljava/lang/String;ILjava/lang/String;)V")
    getIntervalPattern = JavaMethod("(Ljava/lang/String;I)Landroid/icu/text/DateIntervalInfo$PatternInfo;")
    getDefaultOrder = JavaMethod("()Z")
    getFallbackIntervalPattern = JavaMethod("()Ljava/lang/String;")
    setFallbackIntervalPattern = JavaMethod("(Ljava/lang/String;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    isFrozen = JavaMethod("()Z")
    freeze = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/icu/text/DateIntervalInfo;", False, False)])

    class PatternInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/DateIntervalInfo$PatternInfo"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Z)V", False)]
        firstDateInPtnIsLaterDate = JavaMethod("()Z")
        getFirstPart = JavaMethod("()Ljava/lang/String;")
        getSecondPart = JavaMethod("()Ljava/lang/String;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")