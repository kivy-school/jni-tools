from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JapaneseEra"]

class JapaneseEra(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/JapaneseEra"
    HEISEI = JavaStaticField("Ljava/time/chrono/JapaneseEra;")
    MEIJI = JavaStaticField("Ljava/time/chrono/JapaneseEra;")
    REIWA = JavaStaticField("Ljava/time/chrono/JapaneseEra;")
    SHOWA = JavaStaticField("Ljava/time/chrono/JapaneseEra;")
    TAISHO = JavaStaticField("Ljava/time/chrono/JapaneseEra;")
    of = JavaStaticMethod("(I)Ljava/time/chrono/JapaneseEra;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/chrono/JapaneseEra;")
    values = JavaStaticMethod("()[Ljava/time/chrono/JapaneseEra;")
    getDisplayName = JavaMethod("(Ljava/time/format/TextStyle;Ljava/util/Locale;)Ljava/lang/String;")
    getValue = JavaMethod("()I")
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")
    toString = JavaMethod("()Ljava/lang/String;")