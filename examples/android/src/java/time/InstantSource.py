from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InstantSource"]

class InstantSource(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/InstantSource"
    system = JavaStaticMethod("()Ljava/time/InstantSource;")
    tick = JavaStaticMethod("(Ljava/time/InstantSource;Ljava/time/Duration;)Ljava/time/InstantSource;")
    fixed = JavaStaticMethod("(Ljava/time/Instant;)Ljava/time/InstantSource;")
    offset = JavaStaticMethod("(Ljava/time/InstantSource;Ljava/time/Duration;)Ljava/time/InstantSource;")
    instant = JavaMethod("()Ljava/time/Instant;")
    millis = JavaMethod("()J")
    withZone = JavaMethod("(Ljava/time/ZoneId;)Ljava/time/Clock;")