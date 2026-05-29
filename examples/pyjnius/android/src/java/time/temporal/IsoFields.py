from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IsoFields"]

class IsoFields(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/IsoFields"
    DAY_OF_QUARTER = JavaStaticField("Ljava/time/temporal/TemporalField;")
    QUARTER_OF_YEAR = JavaStaticField("Ljava/time/temporal/TemporalField;")
    WEEK_OF_WEEK_BASED_YEAR = JavaStaticField("Ljava/time/temporal/TemporalField;")
    WEEK_BASED_YEAR = JavaStaticField("Ljava/time/temporal/TemporalField;")
    WEEK_BASED_YEARS = JavaStaticField("Ljava/time/temporal/TemporalUnit;")
    QUARTER_YEARS = JavaStaticField("Ljava/time/temporal/TemporalUnit;")