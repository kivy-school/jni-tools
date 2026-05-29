from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemporalQueries"]

class TemporalQueries(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/TemporalQueries"
    zoneId = JavaStaticMethod("()Ljava/time/temporal/TemporalQuery;")
    chronology = JavaStaticMethod("()Ljava/time/temporal/TemporalQuery;")
    precision = JavaStaticMethod("()Ljava/time/temporal/TemporalQuery;")
    zone = JavaStaticMethod("()Ljava/time/temporal/TemporalQuery;")
    offset = JavaStaticMethod("()Ljava/time/temporal/TemporalQuery;")
    localDate = JavaStaticMethod("()Ljava/time/temporal/TemporalQuery;")
    localTime = JavaStaticMethod("()Ljava/time/temporal/TemporalQuery;")