from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DiscretePathEffect"]

class DiscretePathEffect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/DiscretePathEffect"
    __javaconstructor__ = [("(FF)V", False)]