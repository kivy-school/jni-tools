from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ComposePathEffect"]

class ComposePathEffect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/ComposePathEffect"
    __javaconstructor__ = [("(Landroid/graphics/PathEffect;Landroid/graphics/PathEffect;)V", False)]