from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Fade"]

class Fade(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/Fade"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    IN = JavaStaticField("I")
    OUT = JavaStaticField("I")
    MODE_IN = JavaStaticField("I")
    MODE_OUT = JavaStaticField("I")
    MATCH_ID = JavaStaticField("I")
    MATCH_INSTANCE = JavaStaticField("I")
    MATCH_ITEM_ID = JavaStaticField("I")
    MATCH_NAME = JavaStaticField("I")
    onAppear = JavaMethod("(Landroid/view/ViewGroup;Landroid/view/View;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;")
    onDisappear = JavaMethod("(Landroid/view/ViewGroup;Landroid/view/View;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;")
    captureStartValues = JavaMethod("(Landroid/transition/TransitionValues;)V")