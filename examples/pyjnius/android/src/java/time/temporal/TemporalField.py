from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemporalField"]

class TemporalField(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/TemporalField"
    toString = JavaMethod("()Ljava/lang/String;")
    resolve = JavaMethod("(Ljava/util/Map;Ljava/time/temporal/TemporalAccessor;Ljava/time/format/ResolverStyle;)Ljava/time/temporal/TemporalAccessor;")
    getDisplayName = JavaMethod("(Ljava/util/Locale;)Ljava/lang/String;")
    range = JavaMethod("()Ljava/time/temporal/ValueRange;")
    getBaseUnit = JavaMethod("()Ljava/time/temporal/TemporalUnit;")
    getRangeUnit = JavaMethod("()Ljava/time/temporal/TemporalUnit;")
    isTimeBased = JavaMethod("()Z")
    isDateBased = JavaMethod("()Z")
    rangeRefinedBy = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/temporal/ValueRange;")
    getFrom = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)J")
    adjustInto = JavaMethod("(Ljava/time/temporal/Temporal;J)Ljava/time/temporal/Temporal;")
    isSupportedBy = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)Z")