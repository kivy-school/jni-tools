from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZoneOffset"]

class ZoneOffset(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/ZoneOffset"
    UTC = JavaStaticField("Ljava/time/ZoneOffset;")
    MIN = JavaStaticField("Ljava/time/ZoneOffset;")
    MAX = JavaStaticField("Ljava/time/ZoneOffset;")
    SHORT_IDS = JavaStaticField("Ljava/util/Map;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/time/ZoneOffset;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    getLong = JavaMethod("(Ljava/time/temporal/TemporalField;)J")
    of = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/ZoneOffset;")
    get = JavaMethod("(Ljava/time/temporal/TemporalField;)I")
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/ZoneOffset;")
    isSupported = JavaMethod("(Ljava/time/temporal/TemporalField;)Z")
    getId = JavaMethod("()Ljava/lang/String;")
    query = JavaMethod("(Ljava/time/temporal/TemporalQuery;)Ljava/lang/Object;")
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")
    normalized = JavaMethod("()Ljava/time/ZoneId;")
    ofHoursMinutesSeconds = JavaStaticMethod("(III)Ljava/time/ZoneOffset;")
    ofTotalSeconds = JavaStaticMethod("(I)Ljava/time/ZoneOffset;")
    ofHoursMinutes = JavaStaticMethod("(II)Ljava/time/ZoneOffset;")
    ofHours = JavaStaticMethod("(I)Ljava/time/ZoneOffset;")
    getTotalSeconds = JavaMethod("()I")
    adjustInto = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")
    getRules = JavaMethod("()Ljava/time/zone/ZoneRules;")