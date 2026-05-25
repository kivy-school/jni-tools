from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MinguoEra"]

class MinguoEra(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/MinguoEra"
    values = JavaStaticMethod("()[Ljava/time/chrono/MinguoEra;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/chrono/MinguoEra;")
    of = JavaStaticMethod("(I)Ljava/time/chrono/MinguoEra;")
    getValue = JavaMethod("()I")
    getDisplayName = JavaMethod("(Ljava/time/format/TextStyle;Ljava/util/Locale;)Ljava/lang/String;")
    BEFORE_ROC = JavaStaticField("Ljava/time/chrono/MinguoEra;")
    ROC = JavaStaticField("Ljava/time/chrono/MinguoEra;")