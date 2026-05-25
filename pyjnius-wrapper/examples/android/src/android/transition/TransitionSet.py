from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransitionSet"]

class TransitionSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/TransitionSet"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    ORDERING_SEQUENTIAL = JavaStaticField("I")
    ORDERING_TOGETHER = JavaStaticField("I")
    setOrdering = JavaMethod("(I)Landroid/transition/TransitionSet;")
    getOrdering = JavaMethod("()I")
    addTransition = JavaMethod("(Landroid/transition/Transition;)Landroid/transition/TransitionSet;")
    getTransitionCount = JavaMethod("()I")
    getTransitionAt = JavaMethod("(I)Landroid/transition/Transition;")
    setDuration = JavaMethod("(J)Landroid/transition/TransitionSet;")
    setStartDelay = JavaMethod("(J)Landroid/transition/TransitionSet;")
    setInterpolator = JavaMethod("(Landroid/animation/TimeInterpolator;)Landroid/transition/TransitionSet;")
    addTarget = JavaMultipleMethod([("(Landroid/view/View;)Landroid/transition/TransitionSet;", False, False), ("(I)Landroid/transition/TransitionSet;", False, False), ("(Ljava/lang/String;)Landroid/transition/TransitionSet;", False, False), ("(Ljava/lang/Class;)Landroid/transition/TransitionSet;", False, False)])
    addListener = JavaMethod("(Landroid/transition/Transition$TransitionListener;)Landroid/transition/TransitionSet;")
    removeTarget = JavaMultipleMethod([("(I)Landroid/transition/TransitionSet;", False, False), ("(Landroid/view/View;)Landroid/transition/TransitionSet;", False, False), ("(Ljava/lang/Class;)Landroid/transition/TransitionSet;", False, False), ("(Ljava/lang/String;)Landroid/transition/TransitionSet;", False, False)])
    excludeTarget = JavaMultipleMethod([("(Landroid/view/View;Z)Landroid/transition/Transition;", False, False), ("(Ljava/lang/String;Z)Landroid/transition/Transition;", False, False), ("(IZ)Landroid/transition/Transition;", False, False), ("(Ljava/lang/Class;Z)Landroid/transition/Transition;", False, False)])
    removeListener = JavaMethod("(Landroid/transition/Transition$TransitionListener;)Landroid/transition/TransitionSet;")
    setPathMotion = JavaMethod("(Landroid/transition/PathMotion;)V")
    removeTransition = JavaMethod("(Landroid/transition/Transition;)Landroid/transition/TransitionSet;")
    captureStartValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    captureEndValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    setPropagation = JavaMethod("(Landroid/transition/TransitionPropagation;)V")
    setEpicenterCallback = JavaMethod("(Landroid/transition/Transition$EpicenterCallback;)V")
    clone = JavaMethod("()Landroid/transition/TransitionSet;")