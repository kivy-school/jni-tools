from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZoneOffsetTransitionRule"]

class ZoneOffsetTransitionRule(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/zone/ZoneOffsetTransitionRule"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    of = JavaStaticMethod("(Ljava/time/Month;ILjava/time/DayOfWeek;Ljava/time/LocalTime;ZLjava/time/zone/ZoneOffsetTransitionRule$TimeDefinition;Ljava/time/ZoneOffset;Ljava/time/ZoneOffset;Ljava/time/ZoneOffset;)Ljava/time/zone/ZoneOffsetTransitionRule;")
    getMonth = JavaMethod("()Ljava/time/Month;")
    getOffsetAfter = JavaMethod("()Ljava/time/ZoneOffset;")
    getOffsetBefore = JavaMethod("()Ljava/time/ZoneOffset;")
    getDayOfWeek = JavaMethod("()Ljava/time/DayOfWeek;")
    getDayOfMonthIndicator = JavaMethod("()I")
    getLocalTime = JavaMethod("()Ljava/time/LocalTime;")
    isMidnightEndOfDay = JavaMethod("()Z")
    getTimeDefinition = JavaMethod("()Ljava/time/zone/ZoneOffsetTransitionRule$TimeDefinition;")
    createTransition = JavaMethod("(I)Ljava/time/zone/ZoneOffsetTransition;")
    getStandardOffset = JavaMethod("()Ljava/time/ZoneOffset;")

    class TimeDefinition(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/time/zone/ZoneOffsetTransitionRule$TimeDefinition"
        UTC = JavaStaticField("Ljava/time/zone/ZoneOffsetTransitionRule$TimeDefinition;")
        WALL = JavaStaticField("Ljava/time/zone/ZoneOffsetTransitionRule$TimeDefinition;")
        STANDARD = JavaStaticField("Ljava/time/zone/ZoneOffsetTransitionRule$TimeDefinition;")
        values = JavaStaticMethod("()[Ljava/time/zone/ZoneOffsetTransitionRule$TimeDefinition;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/zone/ZoneOffsetTransitionRule$TimeDefinition;")
        createDateTime = JavaMethod("(Ljava/time/LocalDateTime;Ljava/time/ZoneOffset;Ljava/time/ZoneOffset;)Ljava/time/LocalDateTime;")
        UTC = JavaStaticField("Ljava/time/zone/ZoneOffsetTransitionRule$TimeDefinition;")
        WALL = JavaStaticField("Ljava/time/zone/ZoneOffsetTransitionRule$TimeDefinition;")
        STANDARD = JavaStaticField("Ljava/time/zone/ZoneOffsetTransitionRule$TimeDefinition;")