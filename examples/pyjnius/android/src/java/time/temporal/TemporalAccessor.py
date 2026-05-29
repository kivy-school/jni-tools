from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemporalAccessor"]

class TemporalAccessor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/TemporalAccessor"
    getLong = JavaMethod("(Ljava/time/temporal/TemporalField;)J")
    get = JavaMethod("(Ljava/time/temporal/TemporalField;)I")
    isSupported = JavaMethod("(Ljava/time/temporal/TemporalField;)Z")
    query = JavaMethod("(Ljava/time/temporal/TemporalQuery;)Ljava/lang/Object;")
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")