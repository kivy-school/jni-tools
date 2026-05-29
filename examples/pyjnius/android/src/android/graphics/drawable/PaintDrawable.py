from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PaintDrawable"]

class PaintDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/PaintDrawable"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    setCornerRadii = JavaMethod("([F)V")
    setCornerRadius = JavaMethod("(F)V")