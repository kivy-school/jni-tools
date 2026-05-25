from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SweepGradient"]

class SweepGradient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/SweepGradient"
    __javaconstructor__ = [("(FF[I[F)V", False), ("(FF[J[F)V", False), ("(FFII)V", False), ("(FFJJ)V", False)]