from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeInterpolator"]

class TimeInterpolator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/TimeInterpolator"
    getInterpolation = JavaMethod("(F)F")