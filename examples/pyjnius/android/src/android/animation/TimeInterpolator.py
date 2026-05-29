from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeInterpolator"]

class TimeInterpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/TimeInterpolator"
    getInterpolation = JavaMethod("(F)F")