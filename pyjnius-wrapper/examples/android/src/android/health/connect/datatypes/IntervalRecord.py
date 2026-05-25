from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntervalRecord"]

class IntervalRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/IntervalRecord"
    getStartTime = JavaMethod("()Ljava/time/Instant;")
    getStartZoneOffset = JavaMethod("()Ljava/time/ZoneOffset;")
    getEndTime = JavaMethod("()Ljava/time/Instant;")
    getEndZoneOffset = JavaMethod("()Ljava/time/ZoneOffset;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")