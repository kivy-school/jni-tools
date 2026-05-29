from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemporalAdjuster"]

class TemporalAdjuster(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/TemporalAdjuster"
    adjustInto = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")