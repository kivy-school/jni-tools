from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectAnimator"]

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
    getTarget = JavaMethod("()Ljava/lang/Object;")
    setTarget = JavaMethod("(Ljava/lang/Object;)V")
    ofMultiFloat = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Ljava/lang/String;[[F)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ObjectAnimator;", True, True)])
    setPropertyName = JavaMethod("(Ljava/lang/String;)V")
    ofInt = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/String;[I)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Landroid/util/Property;Landroid/util/Property;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Landroid/util/Property;[I)Landroid/animation/ObjectAnimator;", True, True)])
    ofObject = JavaMultipleMethod([("(Ljava/lang/Object;Landroid/util/Property;Landroid/animation/TypeConverter;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Landroid/util/Property;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Landroid/util/Property;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False)])
    ofMultiInt = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;[[I)Landroid/animation/ObjectAnimator;", True, False)])
    setupEndValues = JavaMethod("()V")
    setupStartValues = JavaMethod("()V")
    ofArgb = JavaMultipleMethod([("(Ljava/lang/Object;Landroid/util/Property;[I)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;[I)Landroid/animation/ObjectAnimator;", True, True)])
    setObjectValues = JavaMethod("([Ljava/lang/Object;)V", varargs=True)
    setIntValues = JavaMethod("([I)V", varargs=True)
    setFloatValues = JavaMethod("([F)V", varargs=True)
    ofFloat = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Landroid/util/Property;[F)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Landroid/util/Property;Landroid/util/Property;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False)])
    setAutoCancel = JavaMethod("(Z)V")
    getPropertyName = JavaMethod("()Ljava/lang/String;")
    ofPropertyValuesHolder = JavaStaticMethod("(Ljava/lang/Object;[Landroid/animation/PropertyValuesHolder;)Landroid/animation/ObjectAnimator;", varargs=True)
    setDuration = JavaMultipleMethod([("(J)Landroid/animation/Animator;", False, False), ("(J)Landroid/animation/ValueAnimator;", False, False), ("(J)Landroid/animation/ObjectAnimator;", False, False)])