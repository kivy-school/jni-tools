from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeRangeFilter"]

class TimeRangeFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/TimeRangeFilter"