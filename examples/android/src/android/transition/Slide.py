from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Slide"]

class Slide(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/Slide"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    captureStartValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    captureEndValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    setSlideEdge = JavaMethod("(I)V")
    getSlideEdge = JavaMethod("()I")
    onAppear = JavaMethod("(Landroid/view/ViewGroup;Landroid/view/View;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;")
    onDisappear = JavaMethod("(Landroid/view/ViewGroup;Landroid/view/View;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;")