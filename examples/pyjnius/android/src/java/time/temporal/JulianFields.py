from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JulianFields"]

class JulianFields(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/JulianFields"
    JULIAN_DAY = JavaStaticField("Ljava/time/temporal/TemporalField;")
    MODIFIED_JULIAN_DAY = JavaStaticField("Ljava/time/temporal/TemporalField;")
    RATA_DIE = JavaStaticField("Ljava/time/temporal/TemporalField;")