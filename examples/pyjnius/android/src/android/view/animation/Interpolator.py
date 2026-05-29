from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Interpolator"]

class Interpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/Interpolator"