from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZoneRules"]

class ZoneRules(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/zone/ZoneRules"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    of = JavaMultipleMethod([("(Ljava/time/ZoneOffset;Ljava/time/ZoneOffset;Ljava/util/List;Ljava/util/List;Ljava/util/List;)Ljava/time/zone/ZoneRules;", True, False), ("(Ljava/time/ZoneOffset;)Ljava/time/zone/ZoneRules;", True, False)])
    getOffset = JavaMultipleMethod([("(Ljava/time/Instant;)Ljava/time/ZoneOffset;", False, False), ("(Ljava/time/LocalDateTime;)Ljava/time/ZoneOffset;", False, False)])
    isFixedOffset = JavaMethod("()Z")
    getValidOffsets = JavaMethod("(Ljava/time/LocalDateTime;)Ljava/util/List;")
    isValidOffset = JavaMethod("(Ljava/time/LocalDateTime;Ljava/time/ZoneOffset;)Z")
    getTransition = JavaMethod("(Ljava/time/LocalDateTime;)Ljava/time/zone/ZoneOffsetTransition;")
    isDaylightSavings = JavaMethod("(Ljava/time/Instant;)Z")
    getStandardOffset = JavaMethod("(Ljava/time/Instant;)Ljava/time/ZoneOffset;")
    getDaylightSavings = JavaMethod("(Ljava/time/Instant;)Ljava/time/Duration;")
    nextTransition = JavaMethod("(Ljava/time/Instant;)Ljava/time/zone/ZoneOffsetTransition;")
    previousTransition = JavaMethod("(Ljava/time/Instant;)Ljava/time/zone/ZoneOffsetTransition;")
    getTransitions = JavaMethod("()Ljava/util/List;")
    getTransitionRules = JavaMethod("()Ljava/util/List;")