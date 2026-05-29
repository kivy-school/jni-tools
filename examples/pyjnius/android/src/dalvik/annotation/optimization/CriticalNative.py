from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CriticalNative"]

class CriticalNative(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/annotation/optimization/CriticalNative"