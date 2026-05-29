from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeUnit"]

class TimeUnit(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/TimeUnit"
    values = JavaStaticMethod("()[Ljava/util/concurrent/TimeUnit;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/concurrent/TimeUnit;")
    convert = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)J", False, False), ("(Ljava/time/Duration;)J", False, False)])
    toNanos = JavaMethod("(J)J")
    toMicros = JavaMethod("(J)J")
    toMillis = JavaMethod("(J)J")
    toSeconds = JavaMethod("(J)J")
    toMinutes = JavaMethod("(J)J")
    toHours = JavaMethod("(J)J")
    toDays = JavaMethod("(J)J")
    timedWait = JavaMethod("(Ljava/lang/Object;J)V")
    timedJoin = JavaMethod("(Ljava/lang/Thread;J)V")
    sleep = JavaMethod("(J)V")
    toChronoUnit = JavaMethod("()Ljava/time/temporal/ChronoUnit;")
    of = JavaStaticMethod("(Ljava/time/temporal/ChronoUnit;)Ljava/util/concurrent/TimeUnit;")
    NANOSECONDS = JavaStaticField("Ljava/util/concurrent/TimeUnit;")
    MICROSECONDS = JavaStaticField("Ljava/util/concurrent/TimeUnit;")
    MILLISECONDS = JavaStaticField("Ljava/util/concurrent/TimeUnit;")
    SECONDS = JavaStaticField("Ljava/util/concurrent/TimeUnit;")
    MINUTES = JavaStaticField("Ljava/util/concurrent/TimeUnit;")
    HOURS = JavaStaticField("Ljava/util/concurrent/TimeUnit;")
    DAYS = JavaStaticField("Ljava/util/concurrent/TimeUnit;")