from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class PointFEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/PointFEvaluator"
    __javaconstructor__ = [("(Landroid/graphics/PointF;)V", False), ("()V", False)]
    evaluate = JavaMultipleMethod([("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False), ("(FLandroid/graphics/PointF;Landroid/graphics/PointF;)Landroid/graphics/PointF;", False, False)])

class RectEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/RectEvaluator"
    __javaconstructor__ = [("(Landroid/graphics/Rect;)V", False), ("()V", False)]
    evaluate = JavaMultipleMethod([("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False), ("(FLandroid/graphics/Rect;Landroid/graphics/Rect;)Landroid/graphics/Rect;", False, False)])

class TimeInterpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/TimeInterpolator"
    getInterpolation = JavaMethod("(F)F")

class StateListAnimator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/StateListAnimator"
    __javaconstructor__ = [("()V", False)]
    addState = JavaMethod("([ILandroid/animation/Animator;)V")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/animation/StateListAnimator;", False, False)])
    jumpToCurrentState = JavaMethod("()V")

class AnimatorInflater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/AnimatorInflater"
    __javaconstructor__ = [("()V", False)]
    loadAnimator = JavaStaticMethod("(Landroid/content/Context;I)Landroid/animation/Animator;")
    loadStateListAnimator = JavaStaticMethod("(Landroid/content/Context;I)Landroid/animation/StateListAnimator;")

class ObjectAnimator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/ObjectAnimator"
    __javaconstructor__ = [("()V", False)]
    INFINITE = JavaStaticField("I")
    RESTART = JavaStaticField("I")
    REVERSE = JavaStaticField("I")
    DURATION_INFINITE = JavaStaticField("J")
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/animation/ValueAnimator;", False, False), ("()Landroid/animation/Animator;", False, False), ("()Landroid/animation/ObjectAnimator;", False, False)])
    setProperty = JavaMethod("(Landroid/util/Property;)V")
    start = JavaMethod("()V")
    ofArgb = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/String;[I)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Landroid/util/Property;[I)Landroid/animation/ObjectAnimator;", True, True)])
    getPropertyName = JavaMethod("()Ljava/lang/String;")
    ofFloat = JavaMultipleMethod([("(Ljava/lang/Object;Landroid/util/Property;[F)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Landroid/util/Property;Landroid/util/Property;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False)])
    ofMultiFloat = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/String;[[F)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False)])
    ofMultiInt = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;[[I)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False)])
    ofObject = JavaMultipleMethod([("(Ljava/lang/Object;Landroid/util/Property;Landroid/animation/TypeConverter;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Landroid/util/Property;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Landroid/util/Property;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ObjectAnimator;", True, True)])
    ofInt = JavaMultipleMethod([("(Ljava/lang/Object;Landroid/util/Property;[I)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;[I)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Landroid/util/Property;Landroid/util/Property;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False)])
    ofPropertyValuesHolder = JavaStaticMethod("(Ljava/lang/Object;[Landroid/animation/PropertyValuesHolder;)Landroid/animation/ObjectAnimator;", varargs=True)
    setAutoCancel = JavaMethod("(Z)V")
    setFloatValues = JavaMethod("([F)V", varargs=True)
    setIntValues = JavaMethod("([I)V", varargs=True)
    setObjectValues = JavaMethod("([Ljava/lang/Object;)V", varargs=True)
    setPropertyName = JavaMethod("(Ljava/lang/String;)V")
    setupEndValues = JavaMethod("()V")
    setupStartValues = JavaMethod("()V")
    setDuration = JavaMultipleMethod([("(J)Landroid/animation/Animator;", False, False), ("(J)Landroid/animation/ObjectAnimator;", False, False), ("(J)Landroid/animation/ValueAnimator;", False, False)])
    getTarget = JavaMethod("()Ljava/lang/Object;")
    setTarget = JavaMethod("(Ljava/lang/Object;)V")

class FloatArrayEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/FloatArrayEvaluator"
    __javaconstructor__ = [("([F)V", False), ("()V", False)]
    evaluate = JavaMultipleMethod([("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False), ("(F[F[F)[F", False, False)])

class FloatEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/FloatEvaluator"
    __javaconstructor__ = [("()V", False)]
    evaluate = JavaMultipleMethod([("(FLjava/lang/Number;Ljava/lang/Number;)Ljava/lang/Float;", False, False), ("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False)])

class ArgbEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/ArgbEvaluator"
    __javaconstructor__ = [("()V", False)]
    evaluate = JavaMethod("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")

class TypeConverter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/TypeConverter"
    __javaconstructor__ = [("(Ljava/lang/Class;Ljava/lang/Class;)V", False)]
    convert = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")

class IntEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/IntEvaluator"
    __javaconstructor__ = [("()V", False)]
    evaluate = JavaMultipleMethod([("(FLjava/lang/Integer;Ljava/lang/Integer;)Ljava/lang/Integer;", False, False), ("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False)])

class AnimatorSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/AnimatorSet"
    __javaconstructor__ = [("()V", False)]
    DURATION_INFINITE = JavaStaticField("J")
    play = JavaMethod("(Landroid/animation/Animator;)Landroid/animation/AnimatorSet$Builder;")
    getChildAnimations = JavaMethod("()Ljava/util/ArrayList;")
    playTogether = JavaMultipleMethod([("([Landroid/animation/Animator;)V", False, True), ("(Ljava/util/Collection;)V", False, False)])
    playSequentially = JavaMultipleMethod([("(Ljava/util/List;)V", False, False), ("([Landroid/animation/Animator;)V", False, True)])
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMultipleMethod([("()Landroid/animation/AnimatorSet;", False, False), ("()Ljava/lang/Object;", False, False), ("()Landroid/animation/Animator;", False, False)])
    reverse = JavaMethod("()V")
    end = JavaMethod("()V")
    start = JavaMethod("()V")
    resume = JavaMethod("()V")
    cancel = JavaMethod("()V")
    setupEndValues = JavaMethod("()V")
    setupStartValues = JavaMethod("()V")
    getCurrentPlayTime = JavaMethod("()J")
    getTotalDuration = JavaMethod("()J")
    isRunning = JavaMethod("()Z")
    setCurrentPlayTime = JavaMethod("(J)V")
    getInterpolator = JavaMethod("()Landroid/animation/TimeInterpolator;")
    getStartDelay = JavaMethod("()J")
    setDuration = JavaMultipleMethod([("(J)Landroid/animation/AnimatorSet;", False, False), ("(J)Landroid/animation/Animator;", False, False)])
    setInterpolator = JavaMethod("(Landroid/animation/TimeInterpolator;)V")
    setStartDelay = JavaMethod("(J)V")
    pause = JavaMethod("()V")
    getDuration = JavaMethod("()J")
    isStarted = JavaMethod("()Z")
    setTarget = JavaMethod("(Ljava/lang/Object;)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/AnimatorSet$Builder"
        with = JavaMethod("(Landroid/animation/Animator;)Landroid/animation/AnimatorSet$Builder;")
        before = JavaMethod("(Landroid/animation/Animator;)Landroid/animation/AnimatorSet$Builder;")
        after = JavaMultipleMethod([("(Landroid/animation/Animator;)Landroid/animation/AnimatorSet$Builder;", False, False), ("(J)Landroid/animation/AnimatorSet$Builder;", False, False)])

class PropertyValuesHolder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/PropertyValuesHolder"
    ofKeyframe = JavaMultipleMethod([("(Landroid/util/Property;[Landroid/animation/Keyframe;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Ljava/lang/String;[Landroid/animation/Keyframe;)Landroid/animation/PropertyValuesHolder;", True, True)])
    setConverter = JavaMethod("(Landroid/animation/TypeConverter;)V")
    setKeyframes = JavaMethod("([Landroid/animation/Keyframe;)V", varargs=True)
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/animation/PropertyValuesHolder;", False, False)])
    setProperty = JavaMethod("(Landroid/util/Property;)V")
    getPropertyName = JavaMethod("()Ljava/lang/String;")
    ofFloat = JavaMultipleMethod([("(Ljava/lang/String;[F)Landroid/animation/PropertyValuesHolder;", True, True), ("(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;", True, True)])
    ofMultiFloat = JavaMultipleMethod([("(Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/PropertyValuesHolder;", True, False), ("(Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Landroid/animation/Keyframe;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Ljava/lang/String;[[F)Landroid/animation/PropertyValuesHolder;", True, False), ("(Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/PropertyValuesHolder;", True, True)])
    ofMultiInt = JavaMultipleMethod([("(Ljava/lang/String;[[I)Landroid/animation/PropertyValuesHolder;", True, False), ("(Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Landroid/animation/Keyframe;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/PropertyValuesHolder;", True, False)])
    ofObject = JavaMultipleMethod([("(Ljava/lang/String;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Landroid/util/Property;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Landroid/util/Property;Landroid/animation/TypeConverter;Landroid/graphics/Path;)Landroid/animation/PropertyValuesHolder;", True, False), ("(Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/graphics/Path;)Landroid/animation/PropertyValuesHolder;", True, False), ("(Landroid/util/Property;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/PropertyValuesHolder;", True, True)])
    ofInt = JavaMultipleMethod([("(Landroid/util/Property;[I)Landroid/animation/PropertyValuesHolder;", True, True), ("(Ljava/lang/String;[I)Landroid/animation/PropertyValuesHolder;", True, True)])
    setFloatValues = JavaMethod("([F)V", varargs=True)
    setIntValues = JavaMethod("([I)V", varargs=True)
    setObjectValues = JavaMethod("([Ljava/lang/Object;)V", varargs=True)
    setPropertyName = JavaMethod("(Ljava/lang/String;)V")
    setEvaluator = JavaMethod("(Landroid/animation/TypeEvaluator;)V")

class AnimatorListenerAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/AnimatorListenerAdapter"
    __javaconstructor__ = [("()V", False)]
    onAnimationCancel = JavaMethod("(Landroid/animation/Animator;)V")
    onAnimationRepeat = JavaMethod("(Landroid/animation/Animator;)V")
    onAnimationResume = JavaMethod("(Landroid/animation/Animator;)V")
    onAnimationPause = JavaMethod("(Landroid/animation/Animator;)V")
    onAnimationEnd = JavaMethod("(Landroid/animation/Animator;)V")
    onAnimationStart = JavaMethod("(Landroid/animation/Animator;)V")

class TimeAnimator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/TimeAnimator"
    __javaconstructor__ = [("()V", False)]
    INFINITE = JavaStaticField("I")
    RESTART = JavaStaticField("I")
    REVERSE = JavaStaticField("I")
    DURATION_INFINITE = JavaStaticField("J")
    setTimeListener = JavaMethod("(Landroid/animation/TimeAnimator$TimeListener;)V")
    start = JavaMethod("()V")
    setCurrentPlayTime = JavaMethod("(J)V")

    class TimeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/TimeAnimator$TimeListener"
        onTimeUpdate = JavaMethod("(Landroid/animation/TimeAnimator;JJ)V")

class Animator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/Animator"
    __javaconstructor__ = [("()V", False)]
    DURATION_INFINITE = JavaStaticField("J")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/animation/Animator;", False, False)])
    end = JavaMethod("()V")
    start = JavaMethod("()V")
    resume = JavaMethod("()V")
    cancel = JavaMethod("()V")
    setupEndValues = JavaMethod("()V")
    setupStartValues = JavaMethod("()V")
    getTotalDuration = JavaMethod("()J")
    isRunning = JavaMethod("()Z")
    addListener = JavaMethod("(Landroid/animation/Animator$AnimatorListener;)V")
    getInterpolator = JavaMethod("()Landroid/animation/TimeInterpolator;")
    getStartDelay = JavaMethod("()J")
    removeListener = JavaMethod("(Landroid/animation/Animator$AnimatorListener;)V")
    setDuration = JavaMethod("(J)Landroid/animation/Animator;")
    setInterpolator = JavaMethod("(Landroid/animation/TimeInterpolator;)V")
    setStartDelay = JavaMethod("(J)V")
    pause = JavaMethod("()V")
    getDuration = JavaMethod("()J")
    isStarted = JavaMethod("()Z")
    getListeners = JavaMethod("()Ljava/util/ArrayList;")
    isPaused = JavaMethod("()Z")
    addPauseListener = JavaMethod("(Landroid/animation/Animator$AnimatorPauseListener;)V")
    removeAllListeners = JavaMethod("()V")
    removePauseListener = JavaMethod("(Landroid/animation/Animator$AnimatorPauseListener;)V")
    setTarget = JavaMethod("(Ljava/lang/Object;)V")

    class AnimatorPauseListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/Animator$AnimatorPauseListener"
        onAnimationResume = JavaMethod("(Landroid/animation/Animator;)V")
        onAnimationPause = JavaMethod("(Landroid/animation/Animator;)V")

    class AnimatorListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/Animator$AnimatorListener"
        onAnimationCancel = JavaMethod("(Landroid/animation/Animator;)V")
        onAnimationRepeat = JavaMethod("(Landroid/animation/Animator;)V")
        onAnimationEnd = JavaMultipleMethod([("(Landroid/animation/Animator;Z)V", False, False), ("(Landroid/animation/Animator;)V", False, False)])
        onAnimationStart = JavaMultipleMethod([("(Landroid/animation/Animator;Z)V", False, False), ("(Landroid/animation/Animator;)V", False, False)])

class IntArrayEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/IntArrayEvaluator"
    __javaconstructor__ = [("([I)V", False), ("()V", False)]
    evaluate = JavaMultipleMethod([("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False), ("(F[I[I)[I", False, False)])

class Keyframe(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/Keyframe"
    __javaconstructor__ = [("()V", False)]
    setFraction = JavaMethod("(F)V")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/animation/Keyframe;", False, False)])
    getValue = JavaMethod("()Ljava/lang/Object;")
    setValue = JavaMethod("(Ljava/lang/Object;)V")
    getType = JavaMethod("()Ljava/lang/Class;")
    ofFloat = JavaMultipleMethod([("(F)Landroid/animation/Keyframe;", True, False), ("(FF)Landroid/animation/Keyframe;", True, False)])
    ofObject = JavaMultipleMethod([("(FLjava/lang/Object;)Landroid/animation/Keyframe;", True, False), ("(F)Landroid/animation/Keyframe;", True, False)])
    ofInt = JavaMultipleMethod([("(FI)Landroid/animation/Keyframe;", True, False), ("(F)Landroid/animation/Keyframe;", True, False)])
    getInterpolator = JavaMethod("()Landroid/animation/TimeInterpolator;")
    setInterpolator = JavaMethod("(Landroid/animation/TimeInterpolator;)V")
    getFraction = JavaMethod("()F")
    hasValue = JavaMethod("()Z")

class LayoutTransition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/LayoutTransition"
    __javaconstructor__ = [("()V", False)]
    APPEARING = JavaStaticField("I")
    CHANGE_APPEARING = JavaStaticField("I")
    CHANGE_DISAPPEARING = JavaStaticField("I")
    CHANGING = JavaStaticField("I")
    DISAPPEARING = JavaStaticField("I")
    isTransitionTypeEnabled = JavaMethod("(I)Z")
    addTransitionListener = JavaMethod("(Landroid/animation/LayoutTransition$TransitionListener;)V")
    disableTransitionType = JavaMethod("(I)V")
    enableTransitionType = JavaMethod("(I)V")
    getAnimator = JavaMethod("(I)Landroid/animation/Animator;")
    getStagger = JavaMethod("(I)J")
    getTransitionListeners = JavaMethod("()Ljava/util/List;")
    hideChild = JavaMultipleMethod([("(Landroid/view/ViewGroup;Landroid/view/View;I)V", False, False), ("(Landroid/view/ViewGroup;Landroid/view/View;)V", False, False)])
    isChangingLayout = JavaMethod("()Z")
    removeTransitionListener = JavaMethod("(Landroid/animation/LayoutTransition$TransitionListener;)V")
    setAnimateParentHierarchy = JavaMethod("(Z)V")
    setAnimator = JavaMethod("(ILandroid/animation/Animator;)V")
    setStagger = JavaMethod("(IJ)V")
    showChild = JavaMultipleMethod([("(Landroid/view/ViewGroup;Landroid/view/View;)V", False, False), ("(Landroid/view/ViewGroup;Landroid/view/View;I)V", False, False)])
    isRunning = JavaMethod("()Z")
    getInterpolator = JavaMethod("(I)Landroid/animation/TimeInterpolator;")
    getStartDelay = JavaMethod("(I)J")
    setDuration = JavaMultipleMethod([("(J)V", False, False), ("(IJ)V", False, False)])
    setInterpolator = JavaMethod("(ILandroid/animation/TimeInterpolator;)V")
    setStartDelay = JavaMethod("(IJ)V")
    getDuration = JavaMethod("(I)J")
    addChild = JavaMethod("(Landroid/view/ViewGroup;Landroid/view/View;)V")
    removeChild = JavaMethod("(Landroid/view/ViewGroup;Landroid/view/View;)V")

    class TransitionListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/LayoutTransition$TransitionListener"
        startTransition = JavaMethod("(Landroid/animation/LayoutTransition;Landroid/view/ViewGroup;Landroid/view/View;I)V")
        endTransition = JavaMethod("(Landroid/animation/LayoutTransition;Landroid/view/ViewGroup;Landroid/view/View;I)V")

class BidirectionalTypeConverter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/BidirectionalTypeConverter"
    __javaconstructor__ = [("(Ljava/lang/Class;Ljava/lang/Class;)V", False)]
    convertBack = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    invert = JavaMethod("()Landroid/animation/BidirectionalTypeConverter;")

class TypeEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/TypeEvaluator"
    evaluate = JavaMethod("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")

class ValueAnimator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/ValueAnimator"
    __javaconstructor__ = [("()V", False)]
    INFINITE = JavaStaticField("I")
    RESTART = JavaStaticField("I")
    REVERSE = JavaStaticField("I")
    DURATION_INFINITE = JavaStaticField("J")
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMultipleMethod([("()Landroid/animation/Animator;", False, False), ("()Ljava/lang/Object;", False, False), ("()Landroid/animation/ValueAnimator;", False, False)])
    reverse = JavaMethod("()V")
    end = JavaMethod("()V")
    start = JavaMethod("()V")
    resume = JavaMethod("()V")
    cancel = JavaMethod("()V")
    getRepeatMode = JavaMethod("()I")
    setRepeatCount = JavaMethod("(I)V")
    setRepeatMode = JavaMethod("(I)V")
    ofArgb = JavaStaticMethod("([I)Landroid/animation/ValueAnimator;", varargs=True)
    ofFloat = JavaStaticMethod("([F)Landroid/animation/ValueAnimator;", varargs=True)
    ofObject = JavaStaticMethod("(Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ValueAnimator;", varargs=True)
    ofInt = JavaStaticMethod("([I)Landroid/animation/ValueAnimator;", varargs=True)
    ofPropertyValuesHolder = JavaStaticMethod("([Landroid/animation/PropertyValuesHolder;)Landroid/animation/ValueAnimator;", varargs=True)
    setFloatValues = JavaMethod("([F)V", varargs=True)
    setIntValues = JavaMethod("([I)V", varargs=True)
    setObjectValues = JavaMethod("([Ljava/lang/Object;)V", varargs=True)
    addUpdateListener = JavaMethod("(Landroid/animation/ValueAnimator$AnimatorUpdateListener;)V")
    areAnimatorsEnabled = JavaStaticMethod("()Z")
    getAnimatedFraction = JavaMethod("()F")
    getAnimatedValue = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(Ljava/lang/String;)Ljava/lang/Object;", False, False)])
    getCurrentPlayTime = JavaMethod("()J")
    getDurationScale = JavaStaticMethod("()F")
    getFrameDelay = JavaStaticMethod("()J")
    getTotalDuration = JavaMethod("()J")
    isRunning = JavaMethod("()Z")
    registerDurationScaleChangeListener = JavaStaticMethod("(Landroid/animation/ValueAnimator$DurationScaleChangeListener;)Z")
    removeAllUpdateListeners = JavaMethod("()V")
    removeUpdateListener = JavaMethod("(Landroid/animation/ValueAnimator$AnimatorUpdateListener;)V")
    setCurrentFraction = JavaMethod("(F)V")
    setCurrentPlayTime = JavaMethod("(J)V")
    setEvaluator = JavaMethod("(Landroid/animation/TypeEvaluator;)V")
    setFrameDelay = JavaStaticMethod("(J)V")
    unregisterDurationScaleChangeListener = JavaStaticMethod("(Landroid/animation/ValueAnimator$DurationScaleChangeListener;)Z")
    getRepeatCount = JavaMethod("()I")
    getInterpolator = JavaMethod("()Landroid/animation/TimeInterpolator;")
    getStartDelay = JavaMethod("()J")
    setDuration = JavaMultipleMethod([("(J)Landroid/animation/Animator;", False, False), ("(J)Landroid/animation/ValueAnimator;", False, False)])
    setInterpolator = JavaMethod("(Landroid/animation/TimeInterpolator;)V")
    setStartDelay = JavaMethod("(J)V")
    getValues = JavaMethod("()[Landroid/animation/PropertyValuesHolder;")
    setValues = JavaMethod("([Landroid/animation/PropertyValuesHolder;)V", varargs=True)
    pause = JavaMethod("()V")
    getDuration = JavaMethod("()J")
    isStarted = JavaMethod("()Z")

    class DurationScaleChangeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/ValueAnimator$DurationScaleChangeListener"
        onChanged = JavaMethod("(F)V")

    class AnimatorUpdateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/ValueAnimator$AnimatorUpdateListener"
        onAnimationUpdate = JavaMethod("(Landroid/animation/ValueAnimator;)V")