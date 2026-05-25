from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChronoUnit"]

class ChronoUnit(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/ChronoUnit"
    values = JavaStaticMethod("()[Ljava/time/temporal/ChronoUnit;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/temporal/ChronoUnit;")
    getDuration = JavaMethod("()Ljava/time/Duration;")
    isDurationEstimated = JavaMethod("()Z")
    isDateBased = JavaMethod("()Z")
    isTimeBased = JavaMethod("()Z")
    isSupportedBy = JavaMethod("(Ljava/time/temporal/Temporal;)Z")
    addTo = JavaMethod("(Ljava/time/temporal/Temporal;J)Ljava/time/temporal/Temporal;")
    between = JavaMethod("(Ljava/time/temporal/Temporal;Ljava/time/temporal/Temporal;)J")
    toString = JavaMethod("()Ljava/lang/String;")
    NANOS = JavaStaticField("Ljava/time/temporal/ChronoUnit;")
    MICROS = JavaStaticField("Ljava/time/temporal/ChronoUnit;")
    MILLIS = JavaStaticField("Ljava/time/temporal/ChronoUnit;")
    SECONDS = JavaStaticField("Ljava/time/temporal/ChronoUnit;")
    MINUTES = JavaStaticField("Ljava/time/temporal/ChronoUnit;")
    HOURS = JavaStaticField("Ljava/time/temporal/ChronoUnit;")
    HALF_DAYS = JavaStaticField("Ljava/time/temporal/ChronoUnit;")
    DAYS = JavaStaticField("Ljava/time/temporal/ChronoUnit;")
    WEEKS = JavaStaticField("Ljava/time/temporal/ChronoUnit;")
    MONTHS = JavaStaticField("Ljava/time/temporal/ChronoUnit;")
    YEARS = JavaStaticField("Ljava/time/temporal/ChronoUnit;")
    DECADES = JavaStaticField("Ljava/time/temporal/ChronoUnit;")
    CENTURIES = JavaStaticField("Ljava/time/temporal/ChronoUnit;")
    MILLENNIA = JavaStaticField("Ljava/time/temporal/ChronoUnit;")
    ERAS = JavaStaticField("Ljava/time/temporal/ChronoUnit;")
    FOREVER = JavaStaticField("Ljava/time/temporal/ChronoUnit;")