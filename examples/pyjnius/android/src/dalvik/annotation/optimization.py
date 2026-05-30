from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class CriticalNative(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/annotation/optimization/CriticalNative"

class FastNative(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/annotation/optimization/FastNative"