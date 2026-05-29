from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Transition"]

class Transition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/Transition"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    MATCH_ID = JavaStaticField("I")
    MATCH_INSTANCE = JavaStaticField("I")
    MATCH_ITEM_ID = JavaStaticField("I")
    MATCH_NAME = JavaStaticField("I")
    getName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMultipleMethod([("()Landroid/transition/Transition;", False, False), ("()Ljava/lang/Object;", False, False)])
    getDuration = JavaMethod("()J")
    addListener = JavaMethod("(Landroid/transition/Transition$TransitionListener;)Landroid/transition/Transition;")
    addTarget = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/transition/Transition;", False, False), ("(Landroid/view/View;)Landroid/transition/Transition;", False, False), ("(I)Landroid/transition/Transition;", False, False), ("(Ljava/lang/Class;)Landroid/transition/Transition;", False, False)])
    canRemoveViews = JavaMethod("()Z")
    captureEndValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    captureStartValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    createAnimator = JavaMethod("(Landroid/view/ViewGroup;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;")
    excludeChildren = JavaMultipleMethod([("(Ljava/lang/Class;Z)Landroid/transition/Transition;", False, False), ("(IZ)Landroid/transition/Transition;", False, False), ("(Landroid/view/View;Z)Landroid/transition/Transition;", False, False)])
    excludeTarget = JavaMultipleMethod([("(Landroid/view/View;Z)Landroid/transition/Transition;", False, False), ("(IZ)Landroid/transition/Transition;", False, False), ("(Ljava/lang/Class;Z)Landroid/transition/Transition;", False, False), ("(Ljava/lang/String;Z)Landroid/transition/Transition;", False, False)])
    getEpicenter = JavaMethod("()Landroid/graphics/Rect;")
    getEpicenterCallback = JavaMethod("()Landroid/transition/Transition$EpicenterCallback;")
    getInterpolator = JavaMethod("()Landroid/animation/TimeInterpolator;")
    getPathMotion = JavaMethod("()Landroid/transition/PathMotion;")
    getPropagation = JavaMethod("()Landroid/transition/TransitionPropagation;")
    getStartDelay = JavaMethod("()J")
    getTargetIds = JavaMethod("()Ljava/util/List;")
    getTargetNames = JavaMethod("()Ljava/util/List;")
    getTargetTypes = JavaMethod("()Ljava/util/List;")
    getTargets = JavaMethod("()Ljava/util/List;")
    getTransitionProperties = JavaMethod("()[Ljava/lang/String;")
    getTransitionValues = JavaMethod("(Landroid/view/View;Z)Landroid/transition/TransitionValues;")
    isTransitionRequired = JavaMethod("(Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Z")
    removeListener = JavaMethod("(Landroid/transition/Transition$TransitionListener;)Landroid/transition/Transition;")
    removeTarget = JavaMultipleMethod([("(Ljava/lang/Class;)Landroid/transition/Transition;", False, False), ("(Ljava/lang/String;)Landroid/transition/Transition;", False, False), ("(I)Landroid/transition/Transition;", False, False), ("(Landroid/view/View;)Landroid/transition/Transition;", False, False)])
    setDuration = JavaMethod("(J)Landroid/transition/Transition;")
    setEpicenterCallback = JavaMethod("(Landroid/transition/Transition$EpicenterCallback;)V")
    setInterpolator = JavaMethod("(Landroid/animation/TimeInterpolator;)Landroid/transition/Transition;")
    setMatchOrder = JavaMethod("([I)V", varargs=True)
    setPathMotion = JavaMethod("(Landroid/transition/PathMotion;)V")
    setPropagation = JavaMethod("(Landroid/transition/TransitionPropagation;)V")
    setStartDelay = JavaMethod("(J)Landroid/transition/Transition;")

    class TransitionListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/transition/Transition$TransitionListener"
        onTransitionPause = JavaMethod("(Landroid/transition/Transition;)V")
        onTransitionEnd = JavaMethod("(Landroid/transition/Transition;)V")
        onTransitionResume = JavaMethod("(Landroid/transition/Transition;)V")
        onTransitionCancel = JavaMethod("(Landroid/transition/Transition;)V")
        onTransitionStart = JavaMethod("(Landroid/transition/Transition;)V")

    class EpicenterCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/transition/Transition$EpicenterCallback"
        __javaconstructor__ = [("()V", False)]
        onGetEpicenter = JavaMethod("(Landroid/transition/Transition;)Landroid/graphics/Rect;")