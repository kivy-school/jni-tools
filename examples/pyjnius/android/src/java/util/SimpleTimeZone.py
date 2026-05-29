from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SimpleTimeZone"]

class SimpleTimeZone(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/SimpleTimeZone"
    __javaconstructor__ = [("(ILjava/lang/String;)V", False), ("(ILjava/lang/String;IIIIIIII)V", False), ("(ILjava/lang/String;IIIIIIIII)V", False), ("(ILjava/lang/String;IIIIIIIIIII)V", False)]
    WALL_TIME = JavaStaticField("I")
    STANDARD_TIME = JavaStaticField("I")
    UTC_TIME = JavaStaticField("I")
    SHORT = JavaStaticField("I")
    LONG = JavaStaticField("I")
    inDaylightTime = JavaMethod("(Ljava/util/Date;)Z")
    getRawOffset = JavaMethod("()I")
    getDSTSavings = JavaMethod("()I")
    useDaylightTime = JavaMethod("()Z")
    setRawOffset = JavaMethod("(I)V")
    observesDaylightTime = JavaMethod("()Z")
    hasSameRules = JavaMethod("(Ljava/util/TimeZone;)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    getOffset = JavaMultipleMethod([("(IIIIII)I", False, False), ("(J)I", False, False)])
    setStartRule = JavaMultipleMethod([("(IIII)V", False, False), ("(IIIIZ)V", False, False), ("(III)V", False, False)])
    setEndRule = JavaMultipleMethod([("(III)V", False, False), ("(IIII)V", False, False), ("(IIIIZ)V", False, False)])
    setStartYear = JavaMethod("(I)V")
    setDSTSavings = JavaMethod("(I)V")