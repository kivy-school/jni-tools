from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InstantSource"]

class InstantSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/InstantSource"
    offset = JavaStaticMethod("(Ljava/time/InstantSource;Ljava/time/Duration;)Ljava/time/InstantSource;")
    millis = JavaMethod("()J")
    system = JavaStaticMethod("()Ljava/time/InstantSource;")
    fixed = JavaStaticMethod("(Ljava/time/Instant;)Ljava/time/InstantSource;")
    tick = JavaStaticMethod("(Ljava/time/InstantSource;Ljava/time/Duration;)Ljava/time/InstantSource;")
    withZone = JavaMethod("(Ljava/time/ZoneId;)Ljava/time/Clock;")
    instant = JavaMethod("()Ljava/time/Instant;")