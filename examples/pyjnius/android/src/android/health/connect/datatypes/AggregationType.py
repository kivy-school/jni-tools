from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AggregationType"]

class AggregationType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/AggregationType"