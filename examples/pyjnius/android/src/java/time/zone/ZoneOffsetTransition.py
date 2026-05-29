from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZoneOffsetTransition"]

class ZoneOffsetTransition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/zone/ZoneOffsetTransition"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/time/zone/ZoneOffsetTransition;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    of = JavaStaticMethod("(Ljava/time/LocalDateTime;Ljava/time/ZoneOffset;Ljava/time/ZoneOffset;)Ljava/time/zone/ZoneOffsetTransition;")
    getDuration = JavaMethod("()Ljava/time/Duration;")
    getInstant = JavaMethod("()Ljava/time/Instant;")
    getOffsetAfter = JavaMethod("()Ljava/time/ZoneOffset;")
    isValidOffset = JavaMethod("(Ljava/time/ZoneOffset;)Z")
    isOverlap = JavaMethod("()Z")
    getOffsetBefore = JavaMethod("()Ljava/time/ZoneOffset;")
    isGap = JavaMethod("()Z")
    getDateTimeAfter = JavaMethod("()Ljava/time/LocalDateTime;")
    toEpochSecond = JavaMethod("()J")
    getDateTimeBefore = JavaMethod("()Ljava/time/LocalDateTime;")