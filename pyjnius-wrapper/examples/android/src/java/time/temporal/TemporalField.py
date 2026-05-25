from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemporalField"]

class TemporalField(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/TemporalField"
    getDisplayName = JavaMethod("(Ljava/util/Locale;)Ljava/lang/String;")
    getBaseUnit = JavaMethod("()Ljava/time/temporal/TemporalUnit;")
    getRangeUnit = JavaMethod("()Ljava/time/temporal/TemporalUnit;")
    range = JavaMethod("()Ljava/time/temporal/ValueRange;")
    isDateBased = JavaMethod("()Z")
    isTimeBased = JavaMethod("()Z")
    isSupportedBy = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)Z")
    rangeRefinedBy = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/temporal/ValueRange;")
    getFrom = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)J")
    adjustInto = JavaMethod("(Ljava/time/temporal/Temporal;J)Ljava/time/temporal/Temporal;")
    resolve = JavaMethod("(Ljava/util/Map;Ljava/time/temporal/TemporalAccessor;Ljava/time/format/ResolverStyle;)Ljava/time/temporal/TemporalAccessor;")
    toString = JavaMethod("()Ljava/lang/String;")