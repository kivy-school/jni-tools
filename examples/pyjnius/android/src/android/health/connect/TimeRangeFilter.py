from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeRangeFilter"]

class TimeRangeFilter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/TimeRangeFilter"