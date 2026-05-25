from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemporalAccessor"]

class TemporalAccessor(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/TemporalAccessor"
    isSupported = JavaMethod("(Ljava/time/temporal/TemporalField;)Z")
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")
    get = JavaMethod("(Ljava/time/temporal/TemporalField;)I")
    getLong = JavaMethod("(Ljava/time/temporal/TemporalField;)J")
    query = JavaMethod("(Ljava/time/temporal/TemporalQuery;)Ljava/lang/Object;")