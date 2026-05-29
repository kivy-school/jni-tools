from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SumPathEffect"]

class SumPathEffect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/SumPathEffect"
    __javaconstructor__ = [("(Landroid/graphics/PathEffect;Landroid/graphics/PathEffect;)V", False)]