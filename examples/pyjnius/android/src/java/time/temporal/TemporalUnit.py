from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemporalUnit"]

class TemporalUnit(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/TemporalUnit"
    toString = JavaMethod("()Ljava/lang/String;")
    getDuration = JavaMethod("()Ljava/time/Duration;")
    between = JavaMethod("(Ljava/time/temporal/Temporal;Ljava/time/temporal/Temporal;)J")
    isTimeBased = JavaMethod("()Z")
    isDurationEstimated = JavaMethod("()Z")
    addTo = JavaMethod("(Ljava/time/temporal/Temporal;J)Ljava/time/temporal/Temporal;")
    isDateBased = JavaMethod("()Z")
    isSupportedBy = JavaMethod("(Ljava/time/temporal/Temporal;)Z")