from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemporalQuery"]

class TemporalQuery(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/TemporalQuery"
    queryFrom = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/lang/Object;")