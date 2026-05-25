from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlphaAnimation"]

class AlphaAnimation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/AlphaAnimation"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(FF)V", False)]
    applyTransformation = JavaMethod("(FLandroid/view/animation/Transformation;)V")
    willChangeTransformationMatrix = JavaMethod("()Z")
    willChangeBounds = JavaMethod("()Z")