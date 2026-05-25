from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemporalAmount"]

class TemporalAmount(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/TemporalAmount"
    get = JavaMethod("(Ljava/time/temporal/TemporalUnit;)J")
    getUnits = JavaMethod("()Ljava/util/List;")
    addTo = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")
    subtractFrom = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")