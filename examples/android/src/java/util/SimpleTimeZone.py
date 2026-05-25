from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SimpleTimeZone"]

class SimpleTimeZone(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/SimpleTimeZone"
    __javaconstructor__ = [("(ILjava/lang/String;)V", False), ("(ILjava/lang/String;IIIIIIII)V", False), ("(ILjava/lang/String;IIIIIIIII)V", False), ("(ILjava/lang/String;IIIIIIIIIII)V", False)]
    STANDARD_TIME = JavaStaticField("I")
    UTC_TIME = JavaStaticField("I")
    WALL_TIME = JavaStaticField("I")
    setStartYear = JavaMethod("(I)V")
    setStartRule = JavaMultipleMethod([("(IIII)V", False, False), ("(III)V", False, False), ("(IIIIZ)V", False, False)])
    setEndRule = JavaMultipleMethod([("(IIII)V", False, False), ("(III)V", False, False), ("(IIIIZ)V", False, False)])
    getOffset = JavaMultipleMethod([("(J)I", False, False), ("(IIIIII)I", False, False)])
    getRawOffset = JavaMethod("()I")
    setRawOffset = JavaMethod("(I)V")
    setDSTSavings = JavaMethod("(I)V")
    getDSTSavings = JavaMethod("()I")
    useDaylightTime = JavaMethod("()Z")
    observesDaylightTime = JavaMethod("()Z")
    inDaylightTime = JavaMethod("(Ljava/util/Date;)Z")
    clone = JavaMethod("()Ljava/lang/Object;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hasSameRules = JavaMethod("(Ljava/util/TimeZone;)Z")
    toString = JavaMethod("()Ljava/lang/String;")