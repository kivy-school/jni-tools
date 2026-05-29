from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SweepGradient"]

class SweepGradient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/SweepGradient"
    __javaconstructor__ = [("(FF[J[F)V", False), ("(FFJJ)V", False), ("(FF[I[F)V", False), ("(FFII)V", False)]