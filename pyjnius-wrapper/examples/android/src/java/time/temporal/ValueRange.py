from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ValueRange"]

class ValueRange(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/ValueRange"
    of = JavaMultipleMethod([("(JJ)Ljava/time/temporal/ValueRange;", True, False), ("(JJJ)Ljava/time/temporal/ValueRange;", True, False), ("(JJJJ)Ljava/time/temporal/ValueRange;", True, False)])
    isFixed = JavaMethod("()Z")
    getMinimum = JavaMethod("()J")
    getLargestMinimum = JavaMethod("()J")
    getSmallestMaximum = JavaMethod("()J")
    getMaximum = JavaMethod("()J")
    isIntValue = JavaMethod("()Z")
    isValidValue = JavaMethod("(J)Z")
    isValidIntValue = JavaMethod("(J)Z")
    checkValidValue = JavaMethod("(JLjava/time/temporal/TemporalField;)J")
    checkValidIntValue = JavaMethod("(JLjava/time/temporal/TemporalField;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")