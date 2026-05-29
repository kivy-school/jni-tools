from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HijrahEra"]

class HijrahEra(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/HijrahEra"
    values = JavaStaticMethod("()[Ljava/time/chrono/HijrahEra;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/chrono/HijrahEra;")
    of = JavaStaticMethod("(I)Ljava/time/chrono/HijrahEra;")
    getValue = JavaMethod("()I")
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")
    getDisplayName = JavaMethod("(Ljava/time/format/TextStyle;Ljava/util/Locale;)Ljava/lang/String;")
    AH = JavaStaticField("Ljava/time/chrono/HijrahEra;")