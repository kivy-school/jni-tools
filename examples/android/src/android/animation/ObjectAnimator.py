from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectAnimator"]

class ObjectAnimator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/ObjectAnimator"
    __javaconstructor__ = [("()V", False)]
    setPropertyName = JavaMethod("(Ljava/lang/String;)V")
    setProperty = JavaMethod("(Landroid/util/Property;)V")
    getPropertyName = JavaMethod("()Ljava/lang/String;")
    ofInt = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/String;[I)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Landroid/util/Property;[I)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Landroid/util/Property;Landroid/util/Property;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False)])
    ofMultiInt = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/String;[[I)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ObjectAnimator;", True, True)])
    ofArgb = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/String;[I)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Landroid/util/Property;[I)Landroid/animation/ObjectAnimator;", True, True)])
    ofFloat = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Landroid/util/Property;[F)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Landroid/util/Property;Landroid/util/Property;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False)])
    ofMultiFloat = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/String;[[F)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ObjectAnimator;", True, True)])
    ofObject = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/String;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False), ("(Ljava/lang/Object;Landroid/util/Property;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Landroid/util/Property;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ObjectAnimator;", True, True), ("(Ljava/lang/Object;Landroid/util/Property;Landroid/animation/TypeConverter;Landroid/graphics/Path;)Landroid/animation/ObjectAnimator;", True, False)])
    ofPropertyValuesHolder = JavaStaticMethod("(Ljava/lang/Object;[Landroid/animation/PropertyValuesHolder;)Landroid/animation/ObjectAnimator;", varargs=True)
    setIntValues = JavaMethod("([I)V", varargs=True)
    setFloatValues = JavaMethod("([F)V", varargs=True)
    setObjectValues = JavaMethod("([Ljava/lang/Object;)V", varargs=True)
    setAutoCancel = JavaMethod("(Z)V")
    start = JavaMethod("()V")
    setDuration = JavaMethod("(J)Landroid/animation/ObjectAnimator;")
    getTarget = JavaMethod("()Ljava/lang/Object;")
    setTarget = JavaMethod("(Ljava/lang/Object;)V")
    setupStartValues = JavaMethod("()V")
    setupEndValues = JavaMethod("()V")
    clone = JavaMethod("()Landroid/animation/ObjectAnimator;")
    toString = JavaMethod("()Ljava/lang/String;")