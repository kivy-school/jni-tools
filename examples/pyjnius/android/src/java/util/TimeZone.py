from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeZone"]

class TimeZone(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/TimeZone"
    __javaconstructor__ = [("()V", False)]
    SHORT = JavaStaticField("I")
    LONG = JavaStaticField("I")
    inDaylightTime = JavaMethod("(Ljava/util/Date;)Z")
    getRawOffset = JavaMethod("()I")
    getDSTSavings = JavaMethod("()I")
    useDaylightTime = JavaMethod("()Z")
    getAvailableIDs = JavaMultipleMethod([("(I)[Ljava/lang/String;", True, False), ("()[Ljava/lang/String;", True, False)])
    availableIDs = JavaMultipleMethod([("(I)Ljava/util/stream/Stream;", True, False), ("()Ljava/util/stream/Stream;", True, False)])
    setID = JavaMethod("(Ljava/lang/String;)V")
    setRawOffset = JavaMethod("(I)V")
    observesDaylightTime = JavaMethod("()Z")
    hasSameRules = JavaMethod("(Ljava/util/TimeZone;)Z")
    clone = JavaMethod("()Ljava/lang/Object;")
    getDefault = JavaStaticMethod("()Ljava/util/TimeZone;")
    getTimeZone = JavaMultipleMethod([("(Ljava/time/ZoneId;)Ljava/util/TimeZone;", True, False), ("(Ljava/lang/String;)Ljava/util/TimeZone;", True, False)])
    getOffset = JavaMultipleMethod([("(J)I", False, False), ("(IIIIII)I", False, False)])
    setDefault = JavaStaticMethod("(Ljava/util/TimeZone;)V")
    getID = JavaMethod("()Ljava/lang/String;")
    getDisplayName = JavaMultipleMethod([("(ZI)Ljava/lang/String;", False, False), ("(Ljava/util/Locale;)Ljava/lang/String;", False, False), ("(ZILjava/util/Locale;)Ljava/lang/String;", False, False), ("()Ljava/lang/String;", False, False)])
    toZoneId = JavaMethod("()Ljava/time/ZoneId;")