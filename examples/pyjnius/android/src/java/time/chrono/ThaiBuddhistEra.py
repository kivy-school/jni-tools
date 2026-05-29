from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThaiBuddhistEra"]

class ThaiBuddhistEra(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/ThaiBuddhistEra"
    BEFORE_BE = JavaStaticField("Ljava/time/chrono/ThaiBuddhistEra;")
    BE = JavaStaticField("Ljava/time/chrono/ThaiBuddhistEra;")
    values = JavaStaticMethod("()[Ljava/time/chrono/ThaiBuddhistEra;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/chrono/ThaiBuddhistEra;")
    of = JavaStaticMethod("(I)Ljava/time/chrono/ThaiBuddhistEra;")
    getValue = JavaMethod("()I")
    getDisplayName = JavaMethod("(Ljava/time/format/TextStyle;Ljava/util/Locale;)Ljava/lang/String;")
    BEFORE_BE = JavaStaticField("Ljava/time/chrono/ThaiBuddhistEra;")
    BE = JavaStaticField("Ljava/time/chrono/ThaiBuddhistEra;")