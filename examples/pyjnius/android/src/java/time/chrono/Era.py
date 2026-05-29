from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Era"]

class Era(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/Era"
    getLong = JavaMethod("(Ljava/time/temporal/TemporalField;)J")
    getValue = JavaMethod("()I")
    get = JavaMethod("(Ljava/time/temporal/TemporalField;)I")
    isSupported = JavaMethod("(Ljava/time/temporal/TemporalField;)Z")
    query = JavaMethod("(Ljava/time/temporal/TemporalQuery;)Ljava/lang/Object;")
    getDisplayName = JavaMethod("(Ljava/time/format/TextStyle;Ljava/util/Locale;)Ljava/lang/String;")
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")
    adjustInto = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")