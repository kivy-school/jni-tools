from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntervalRecord"]

class IntervalRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/IntervalRecord"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getStartTime = JavaMethod("()Ljava/time/Instant;")
    getEndTime = JavaMethod("()Ljava/time/Instant;")
    getEndZoneOffset = JavaMethod("()Ljava/time/ZoneOffset;")
    getStartZoneOffset = JavaMethod("()Ljava/time/ZoneOffset;")