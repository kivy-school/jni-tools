from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Era"]

class Era(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/Era"
    getValue = JavaMethod("()I")
    isSupported = JavaMethod("(Ljava/time/temporal/TemporalField;)Z")
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")
    get = JavaMethod("(Ljava/time/temporal/TemporalField;)I")
    getLong = JavaMethod("(Ljava/time/temporal/TemporalField;)J")
    query = JavaMethod("(Ljava/time/temporal/TemporalQuery;)Ljava/lang/Object;")
    adjustInto = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")
    getDisplayName = JavaMethod("(Ljava/time/format/TextStyle;Ljava/util/Locale;)Ljava/lang/String;")