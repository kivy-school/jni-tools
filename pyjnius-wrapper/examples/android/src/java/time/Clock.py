from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Clock"]

class Clock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/Clock"
    __javaconstructor__ = [("()V", False)]
    systemUTC = JavaStaticMethod("()Ljava/time/Clock;")
    systemDefaultZone = JavaStaticMethod("()Ljava/time/Clock;")
    system = JavaStaticMethod("(Ljava/time/ZoneId;)Ljava/time/Clock;")
    tickMillis = JavaStaticMethod("(Ljava/time/ZoneId;)Ljava/time/Clock;")
    tickSeconds = JavaStaticMethod("(Ljava/time/ZoneId;)Ljava/time/Clock;")
    tickMinutes = JavaStaticMethod("(Ljava/time/ZoneId;)Ljava/time/Clock;")
    tick = JavaStaticMethod("(Ljava/time/Clock;Ljava/time/Duration;)Ljava/time/Clock;")
    fixed = JavaStaticMethod("(Ljava/time/Instant;Ljava/time/ZoneId;)Ljava/time/Clock;")
    offset = JavaStaticMethod("(Ljava/time/Clock;Ljava/time/Duration;)Ljava/time/Clock;")
    getZone = JavaMethod("()Ljava/time/ZoneId;")
    withZone = JavaMethod("(Ljava/time/ZoneId;)Ljava/time/Clock;")
    millis = JavaMethod("()J")
    instant = JavaMethod("()Ljava/time/Instant;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")