from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Temporal"]

class Temporal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/Temporal"
    isSupported = JavaMethod("(Ljava/time/temporal/TemporalUnit;)Z")
    with = JavaMultipleMethod([("(Ljava/time/temporal/TemporalField;J)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/temporal/Temporal;", False, False)])
    plus = JavaMultipleMethod([("(JLjava/time/temporal/TemporalUnit;)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/temporal/Temporal;", False, False)])
    until = JavaMethod("(Ljava/time/temporal/Temporal;Ljava/time/temporal/TemporalUnit;)J")
    minus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/temporal/Temporal;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/temporal/Temporal;", False, False)])