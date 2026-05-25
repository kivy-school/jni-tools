from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Transition"]

class Transition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/Transition"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    MATCH_ID = JavaStaticField("I")
    MATCH_INSTANCE = JavaStaticField("I")
    MATCH_ITEM_ID = JavaStaticField("I")
    MATCH_NAME = JavaStaticField("I")
    setDuration = JavaMethod("(J)Landroid/transition/Transition;")
    getDuration = JavaMethod("()J")
    setStartDelay = JavaMethod("(J)Landroid/transition/Transition;")
    getStartDelay = JavaMethod("()J")
    setInterpolator = JavaMethod("(Landroid/animation/TimeInterpolator;)Landroid/transition/Transition;")
    getInterpolator = JavaMethod("()Landroid/animation/TimeInterpolator;")
    getTransitionProperties = JavaMethod("()[Ljava/lang/String;")
    createAnimator = JavaMethod("(Landroid/view/ViewGroup;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;")
    setMatchOrder = JavaMethod("([I)V", varargs=True)
    captureStartValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    captureEndValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    addTarget = JavaMultipleMethod([("(I)Landroid/transition/Transition;", False, False), ("(Ljava/lang/String;)Landroid/transition/Transition;", False, False), ("(Ljava/lang/Class;)Landroid/transition/Transition;", False, False), ("(Landroid/view/View;)Landroid/transition/Transition;", False, False)])
    removeTarget = JavaMultipleMethod([("(I)Landroid/transition/Transition;", False, False), ("(Ljava/lang/String;)Landroid/transition/Transition;", False, False), ("(Landroid/view/View;)Landroid/transition/Transition;", False, False), ("(Ljava/lang/Class;)Landroid/transition/Transition;", False, False)])
    excludeTarget = JavaMultipleMethod([("(IZ)Landroid/transition/Transition;", False, False), ("(Ljava/lang/String;Z)Landroid/transition/Transition;", False, False), ("(Landroid/view/View;Z)Landroid/transition/Transition;", False, False), ("(Ljava/lang/Class;Z)Landroid/transition/Transition;", False, False)])
    excludeChildren = JavaMultipleMethod([("(IZ)Landroid/transition/Transition;", False, False), ("(Landroid/view/View;Z)Landroid/transition/Transition;", False, False), ("(Ljava/lang/Class;Z)Landroid/transition/Transition;", False, False)])
    getTargetIds = JavaMethod("()Ljava/util/List;")
    getTargets = JavaMethod("()Ljava/util/List;")
    getTargetNames = JavaMethod("()Ljava/util/List;")
    getTargetTypes = JavaMethod("()Ljava/util/List;")
    getTransitionValues = JavaMethod("(Landroid/view/View;Z)Landroid/transition/TransitionValues;")
    isTransitionRequired = JavaMethod("(Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Z")
    addListener = JavaMethod("(Landroid/transition/Transition$TransitionListener;)Landroid/transition/Transition;")
    removeListener = JavaMethod("(Landroid/transition/Transition$TransitionListener;)Landroid/transition/Transition;")
    setEpicenterCallback = JavaMethod("(Landroid/transition/Transition$EpicenterCallback;)V")
    getEpicenterCallback = JavaMethod("()Landroid/transition/Transition$EpicenterCallback;")
    getEpicenter = JavaMethod("()Landroid/graphics/Rect;")
    setPathMotion = JavaMethod("(Landroid/transition/PathMotion;)V")
    getPathMotion = JavaMethod("()Landroid/transition/PathMotion;")
    setPropagation = JavaMethod("(Landroid/transition/TransitionPropagation;)V")
    getPropagation = JavaMethod("()Landroid/transition/TransitionPropagation;")
    canRemoveViews = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Landroid/transition/Transition;")
    getName = JavaMethod("()Ljava/lang/String;")

    class EpicenterCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/transition/Transition/EpicenterCallback"
        __javaconstructor__ = [("()V", False)]
        onGetEpicenter = JavaMethod("(Landroid/transition/Transition;)Landroid/graphics/Rect;")

    class TransitionListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/transition/Transition/TransitionListener"
        onTransitionStart = JavaMethod("(Landroid/transition/Transition;)V")
        onTransitionEnd = JavaMethod("(Landroid/transition/Transition;)V")
        onTransitionCancel = JavaMethod("(Landroid/transition/Transition;)V")
        onTransitionPause = JavaMethod("(Landroid/transition/Transition;)V")
        onTransitionResume = JavaMethod("(Landroid/transition/Transition;)V")