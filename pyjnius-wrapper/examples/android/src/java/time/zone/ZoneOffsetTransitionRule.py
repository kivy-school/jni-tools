from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZoneOffsetTransitionRule"]

class ZoneOffsetTransitionRule(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/zone/ZoneOffsetTransitionRule"
    of = JavaStaticMethod("(Ljava/time/Month;ILjava/time/DayOfWeek;Ljava/time/LocalTime;ZLjava/time/zone/ZoneOffsetTransitionRule$TimeDefinition;Ljava/time/ZoneOffset;Ljava/time/ZoneOffset;Ljava/time/ZoneOffset;)Ljava/time/zone/ZoneOffsetTransitionRule;")
    getMonth = JavaMethod("()Ljava/time/Month;")
    getDayOfMonthIndicator = JavaMethod("()I")
    getDayOfWeek = JavaMethod("()Ljava/time/DayOfWeek;")
    getLocalTime = JavaMethod("()Ljava/time/LocalTime;")
    isMidnightEndOfDay = JavaMethod("()Z")
    getTimeDefinition = JavaMethod("()Ljava/time/zone/ZoneOffsetTransitionRule$TimeDefinition;")
    getStandardOffset = JavaMethod("()Ljava/time/ZoneOffset;")
    getOffsetBefore = JavaMethod("()Ljava/time/ZoneOffset;")
    getOffsetAfter = JavaMethod("()Ljava/time/ZoneOffset;")
    createTransition = JavaMethod("(I)Ljava/time/zone/ZoneOffsetTransition;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class TimeDefinition(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/time/zone/ZoneOffsetTransitionRule/TimeDefinition"
        values = JavaStaticMethod("()[Ljava/time/zone/ZoneOffsetTransitionRule$TimeDefinition;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/zone/ZoneOffsetTransitionRule$TimeDefinition;")
        createDateTime = JavaMethod("(Ljava/time/LocalDateTime;Ljava/time/ZoneOffset;Ljava/time/ZoneOffset;)Ljava/time/LocalDateTime;")
        UTC = JavaStaticField("Ljava/time/zone/ZoneOffsetTransitionRule/TimeDefinition;")
        WALL = JavaStaticField("Ljava/time/zone/ZoneOffsetTransitionRule/TimeDefinition;")
        STANDARD = JavaStaticField("Ljava/time/zone/ZoneOffsetTransitionRule/TimeDefinition;")