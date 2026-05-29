from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZoneRules"]

class ZoneRules(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/zone/ZoneRules"
    of = JavaMultipleMethod([("(Ljava/time/ZoneOffset;Ljava/time/ZoneOffset;Ljava/util/List;Ljava/util/List;Ljava/util/List;)Ljava/time/zone/ZoneRules;", True, False), ("(Ljava/time/ZoneOffset;)Ljava/time/zone/ZoneRules;", True, False)])
    isFixedOffset = JavaMethod("()Z")
    getOffset = JavaMultipleMethod([("(Ljava/time/Instant;)Ljava/time/ZoneOffset;", False, False), ("(Ljava/time/LocalDateTime;)Ljava/time/ZoneOffset;", False, False)])
    getValidOffsets = JavaMethod("(Ljava/time/LocalDateTime;)Ljava/util/List;")
    getTransition = JavaMethod("(Ljava/time/LocalDateTime;)Ljava/time/zone/ZoneOffsetTransition;")
    getStandardOffset = JavaMethod("(Ljava/time/Instant;)Ljava/time/ZoneOffset;")
    getDaylightSavings = JavaMethod("(Ljava/time/Instant;)Ljava/time/Duration;")
    isDaylightSavings = JavaMethod("(Ljava/time/Instant;)Z")
    isValidOffset = JavaMethod("(Ljava/time/LocalDateTime;Ljava/time/ZoneOffset;)Z")
    nextTransition = JavaMethod("(Ljava/time/Instant;)Ljava/time/zone/ZoneOffsetTransition;")
    previousTransition = JavaMethod("(Ljava/time/Instant;)Ljava/time/zone/ZoneOffsetTransition;")
    getTransitions = JavaMethod("()Ljava/util/List;")
    getTransitionRules = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")