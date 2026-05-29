from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellSignalStrength"]

class CellSignalStrength(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellSignalStrength"
    SIGNAL_STRENGTH_GOOD = JavaStaticField("I")
    SIGNAL_STRENGTH_GREAT = JavaStaticField("I")
    SIGNAL_STRENGTH_MODERATE = JavaStaticField("I")
    SIGNAL_STRENGTH_NONE_OR_UNKNOWN = JavaStaticField("I")
    SIGNAL_STRENGTH_POOR = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getDbm = JavaMethod("()I")
    getAsuLevel = JavaMethod("()I")
    getLevel = JavaMethod("()I")