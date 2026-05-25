from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZoneOffset"]

class ZoneOffset(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/ZoneOffset"
    MAX = JavaStaticField("Ljava/time/ZoneOffset;")
    MIN = JavaStaticField("Ljava/time/ZoneOffset;")
    UTC = JavaStaticField("Ljava/time/ZoneOffset;")
    of = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/ZoneOffset;")
    ofHours = JavaStaticMethod("(I)Ljava/time/ZoneOffset;")
    ofHoursMinutes = JavaStaticMethod("(II)Ljava/time/ZoneOffset;")
    ofHoursMinutesSeconds = JavaStaticMethod("(III)Ljava/time/ZoneOffset;")
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/ZoneOffset;")
    ofTotalSeconds = JavaStaticMethod("(I)Ljava/time/ZoneOffset;")
    getTotalSeconds = JavaMethod("()I")
    getId = JavaMethod("()Ljava/lang/String;")
    getRules = JavaMethod("()Ljava/time/zone/ZoneRules;")
    isSupported = JavaMethod("(Ljava/time/temporal/TemporalField;)Z")
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")
    get = JavaMethod("(Ljava/time/temporal/TemporalField;)I")
    getLong = JavaMethod("(Ljava/time/temporal/TemporalField;)J")
    query = JavaMethod("(Ljava/time/temporal/TemporalQuery;)Ljava/lang/Object;")
    adjustInto = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")
    compareTo = JavaMethod("(Ljava/time/ZoneOffset;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")