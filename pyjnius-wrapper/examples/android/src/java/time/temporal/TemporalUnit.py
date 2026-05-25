from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemporalUnit"]

class TemporalUnit(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/TemporalUnit"
    getDuration = JavaMethod("()Ljava/time/Duration;")
    isDurationEstimated = JavaMethod("()Z")
    isDateBased = JavaMethod("()Z")
    isTimeBased = JavaMethod("()Z")
    isSupportedBy = JavaMethod("(Ljava/time/temporal/Temporal;)Z")
    addTo = JavaMethod("(Ljava/time/temporal/Temporal;J)Ljava/time/temporal/Temporal;")
    between = JavaMethod("(Ljava/time/temporal/Temporal;Ljava/time/temporal/Temporal;)J")
    toString = JavaMethod("()Ljava/lang/String;")