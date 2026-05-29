from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ValueRange"]

class ValueRange(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/ValueRange"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    of = JavaMultipleMethod([("(JJ)Ljava/time/temporal/ValueRange;", True, False), ("(JJJ)Ljava/time/temporal/ValueRange;", True, False), ("(JJJJ)Ljava/time/temporal/ValueRange;", True, False)])
    isValidIntValue = JavaMethod("(J)Z")
    isFixed = JavaMethod("()Z")
    getLargestMinimum = JavaMethod("()J")
    getSmallestMaximum = JavaMethod("()J")
    getMinimum = JavaMethod("()J")
    getMaximum = JavaMethod("()J")
    checkValidIntValue = JavaMethod("(JLjava/time/temporal/TemporalField;)I")
    checkValidValue = JavaMethod("(JLjava/time/temporal/TemporalField;)J")
    isIntValue = JavaMethod("()Z")
    isValidValue = JavaMethod("(J)Z")