from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemporalQuery"]

class TemporalQuery(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/TemporalQuery"
    queryFrom = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/lang/Object;")