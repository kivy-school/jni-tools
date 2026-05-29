from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JapaneseEra"]

class JapaneseEra(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/JapaneseEra"
    MEIJI = JavaStaticField("Ljava/time/chrono/JapaneseEra;")
    TAISHO = JavaStaticField("Ljava/time/chrono/JapaneseEra;")
    SHOWA = JavaStaticField("Ljava/time/chrono/JapaneseEra;")
    HEISEI = JavaStaticField("Ljava/time/chrono/JapaneseEra;")
    REIWA = JavaStaticField("Ljava/time/chrono/JapaneseEra;")
    toString = JavaMethod("()Ljava/lang/String;")
    values = JavaStaticMethod("()[Ljava/time/chrono/JapaneseEra;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/chrono/JapaneseEra;")
    of = JavaStaticMethod("(I)Ljava/time/chrono/JapaneseEra;")
    getValue = JavaMethod("()I")
    getDisplayName = JavaMethod("(Ljava/time/format/TextStyle;Ljava/util/Locale;)Ljava/lang/String;")
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")