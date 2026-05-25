from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeZone"]

class TimeZone(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/TimeZone"
    __javaconstructor__ = [("()V", False)]
    LONG = JavaStaticField("I")
    SHORT = JavaStaticField("I")
    getOffset = JavaMultipleMethod([("(IIIIII)I", False, False), ("(J)I", False, False)])
    setRawOffset = JavaMethod("(I)V")
    getRawOffset = JavaMethod("()I")
    getID = JavaMethod("()Ljava/lang/String;")
    setID = JavaMethod("(Ljava/lang/String;)V")
    getDisplayName = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Ljava/util/Locale;)Ljava/lang/String;", False, False), ("(ZI)Ljava/lang/String;", False, False), ("(ZILjava/util/Locale;)Ljava/lang/String;", False, False)])
    getDSTSavings = JavaMethod("()I")
    useDaylightTime = JavaMethod("()Z")
    observesDaylightTime = JavaMethod("()Z")
    inDaylightTime = JavaMethod("(Ljava/util/Date;)Z")
    getTimeZone = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/util/TimeZone;", True, False), ("(Ljava/time/ZoneId;)Ljava/util/TimeZone;", True, False)])
    toZoneId = JavaMethod("()Ljava/time/ZoneId;")
    getAvailableIDs = JavaMultipleMethod([("(I)[Ljava/lang/String;", True, False), ("()[Ljava/lang/String;", True, False)])
    getDefault = JavaStaticMethod("()Ljava/util/TimeZone;")
    setDefault = JavaStaticMethod("(Ljava/util/TimeZone;)V")
    hasSameRules = JavaMethod("(Ljava/util/TimeZone;)Z")
    clone = JavaMethod("()Ljava/lang/Object;")