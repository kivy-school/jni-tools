from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FastNative"]

class FastNative(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/annotation/optimization/FastNative"