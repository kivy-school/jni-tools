from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Clock"]

class Clock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/Clock"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    offset = JavaStaticMethod("(Ljava/time/Clock;Ljava/time/Duration;)Ljava/time/Clock;")
    millis = JavaMethod("()J")
    system = JavaStaticMethod("(Ljava/time/ZoneId;)Ljava/time/Clock;")
    fixed = JavaStaticMethod("(Ljava/time/Instant;Ljava/time/ZoneId;)Ljava/time/Clock;")
    systemUTC = JavaStaticMethod("()Ljava/time/Clock;")
    tickMillis = JavaStaticMethod("(Ljava/time/ZoneId;)Ljava/time/Clock;")
    tickSeconds = JavaStaticMethod("(Ljava/time/ZoneId;)Ljava/time/Clock;")
    tickMinutes = JavaStaticMethod("(Ljava/time/ZoneId;)Ljava/time/Clock;")
    tick = JavaStaticMethod("(Ljava/time/Clock;Ljava/time/Duration;)Ljava/time/Clock;")
    withZone = JavaMethod("(Ljava/time/ZoneId;)Ljava/time/Clock;")
    systemDefaultZone = JavaStaticMethod("()Ljava/time/Clock;")
    getZone = JavaMethod("()Ljava/time/ZoneId;")
    instant = JavaMethod("()Ljava/time/Instant;")