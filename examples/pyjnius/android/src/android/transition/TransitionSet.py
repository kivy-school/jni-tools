from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransitionSet"]

class TransitionSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/TransitionSet"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    ORDERING_SEQUENTIAL = JavaStaticField("I")
    ORDERING_TOGETHER = JavaStaticField("I")
    MATCH_ID = JavaStaticField("I")
    MATCH_INSTANCE = JavaStaticField("I")
    MATCH_ITEM_ID = JavaStaticField("I")
    MATCH_NAME = JavaStaticField("I")
    addTransition = JavaMethod("(Landroid/transition/Transition;)Landroid/transition/TransitionSet;")
    removeTransition = JavaMethod("(Landroid/transition/Transition;)Landroid/transition/TransitionSet;")
    getTransitionAt = JavaMethod("(I)Landroid/transition/Transition;")
    getTransitionCount = JavaMethod("()I")
    getOrdering = JavaMethod("()I")
    setOrdering = JavaMethod("(I)Landroid/transition/TransitionSet;")
    clone = JavaMultipleMethod([("()Landroid/transition/TransitionSet;", False, False), ("()Landroid/transition/Transition;", False, False), ("()Ljava/lang/Object;", False, False)])
    addListener = JavaMultipleMethod([("(Landroid/transition/Transition$TransitionListener;)Landroid/transition/TransitionSet;", False, False), ("(Landroid/transition/Transition$TransitionListener;)Landroid/transition/Transition;", False, False)])
    addTarget = JavaMultipleMethod([("(I)Landroid/transition/Transition;", False, False), ("(Ljava/lang/String;)Landroid/transition/TransitionSet;", False, False), ("(Ljava/lang/Class;)Landroid/transition/Transition;", False, False), ("(Landroid/view/View;)Landroid/transition/Transition;", False, False), ("(Ljava/lang/String;)Landroid/transition/Transition;", False, False), ("(Landroid/view/View;)Landroid/transition/TransitionSet;", False, False), ("(Ljava/lang/Class;)Landroid/transition/TransitionSet;", False, False), ("(I)Landroid/transition/TransitionSet;", False, False)])
    captureEndValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    captureStartValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    excludeTarget = JavaMultipleMethod([("(Landroid/view/View;Z)Landroid/transition/Transition;", False, False), ("(Ljava/lang/String;Z)Landroid/transition/Transition;", False, False), ("(Ljava/lang/Class;Z)Landroid/transition/Transition;", False, False), ("(IZ)Landroid/transition/Transition;", False, False)])
    removeListener = JavaMultipleMethod([("(Landroid/transition/Transition$TransitionListener;)Landroid/transition/Transition;", False, False), ("(Landroid/transition/Transition$TransitionListener;)Landroid/transition/TransitionSet;", False, False)])
    removeTarget = JavaMultipleMethod([("(I)Landroid/transition/Transition;", False, False), ("(Ljava/lang/Class;)Landroid/transition/Transition;", False, False), ("(Ljava/lang/String;)Landroid/transition/Transition;", False, False), ("(Landroid/view/View;)Landroid/transition/Transition;", False, False), ("(Landroid/view/View;)Landroid/transition/TransitionSet;", False, False), ("(Ljava/lang/Class;)Landroid/transition/TransitionSet;", False, False), ("(I)Landroid/transition/TransitionSet;", False, False), ("(Ljava/lang/String;)Landroid/transition/TransitionSet;", False, False)])
    setDuration = JavaMultipleMethod([("(J)Landroid/transition/TransitionSet;", False, False), ("(J)Landroid/transition/Transition;", False, False)])
    setEpicenterCallback = JavaMethod("(Landroid/transition/Transition$EpicenterCallback;)V")
    setInterpolator = JavaMultipleMethod([("(Landroid/animation/TimeInterpolator;)Landroid/transition/TransitionSet;", False, False), ("(Landroid/animation/TimeInterpolator;)Landroid/transition/Transition;", False, False)])
    setPathMotion = JavaMethod("(Landroid/transition/PathMotion;)V")
    setPropagation = JavaMethod("(Landroid/transition/TransitionPropagation;)V")
    setStartDelay = JavaMultipleMethod([("(J)Landroid/transition/Transition;", False, False), ("(J)Landroid/transition/TransitionSet;", False, False)])