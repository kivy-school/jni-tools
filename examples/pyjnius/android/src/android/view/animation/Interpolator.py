from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Interpolator"]

class Interpolator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/Interpolator"