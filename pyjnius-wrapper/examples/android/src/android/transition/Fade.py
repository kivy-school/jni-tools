from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Fade"]

class Fade(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/Fade"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    IN = JavaStaticField("I")
    OUT = JavaStaticField("I")
    captureStartValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    onAppear = JavaMethod("(Landroid/view/ViewGroup;Landroid/view/View;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;")
    onDisappear = JavaMethod("(Landroid/view/ViewGroup;Landroid/view/View;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;")