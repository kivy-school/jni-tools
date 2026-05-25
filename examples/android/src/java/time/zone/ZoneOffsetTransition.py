from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZoneOffsetTransition"]

class ZoneOffsetTransition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/zone/ZoneOffsetTransition"
    of = JavaStaticMethod("(Ljava/time/LocalDateTime;Ljava/time/ZoneOffset;Ljava/time/ZoneOffset;)Ljava/time/zone/ZoneOffsetTransition;")
    getInstant = JavaMethod("()Ljava/time/Instant;")
    toEpochSecond = JavaMethod("()J")
    getDateTimeBefore = JavaMethod("()Ljava/time/LocalDateTime;")
    getDateTimeAfter = JavaMethod("()Ljava/time/LocalDateTime;")
    getOffsetBefore = JavaMethod("()Ljava/time/ZoneOffset;")
    getOffsetAfter = JavaMethod("()Ljava/time/ZoneOffset;")
    getDuration = JavaMethod("()Ljava/time/Duration;")
    isGap = JavaMethod("()Z")
    isOverlap = JavaMethod("()Z")
    isValidOffset = JavaMethod("(Ljava/time/ZoneOffset;)Z")
    compareTo = JavaMethod("(Ljava/time/zone/ZoneOffsetTransition;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")