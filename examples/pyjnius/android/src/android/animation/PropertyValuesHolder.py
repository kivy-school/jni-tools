from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyValuesHolder"]

class PropertyValuesHolder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/PropertyValuesHolder"
    ofInt = JavaMultipleMethod([("(Ljava/lang/String;[I)Landroid/animation/PropertyValuesHolder;", True, True), ("(Landroid/util/Property;[I)Landroid/animation/PropertyValuesHolder;", True, True)])
    ofMultiInt = JavaMultipleMethod([("(Ljava/lang/String;[[I)Landroid/animation/PropertyValuesHolder;", True, False), ("(Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/PropertyValuesHolder;", True, False), ("(Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Landroid/animation/Keyframe;)Landroid/animation/PropertyValuesHolder;", True, True)])
    ofFloat = JavaMultipleMethod([("(Ljava/lang/String;[F)Landroid/animation/PropertyValuesHolder;", True, True), ("(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;", True, True)])
    ofMultiFloat = JavaMultipleMethod([("(Ljava/lang/String;[[F)Landroid/animation/PropertyValuesHolder;", True, False), ("(Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/PropertyValuesHolder;", True, False), ("(Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Landroid/animation/Keyframe;)Landroid/animation/PropertyValuesHolder;", True, True)])
    ofObject = JavaMultipleMethod([("(Ljava/lang/String;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/graphics/Path;)Landroid/animation/PropertyValuesHolder;", True, False), ("(Landroid/util/Property;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Landroid/util/Property;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Landroid/util/Property;Landroid/animation/TypeConverter;Landroid/graphics/Path;)Landroid/animation/PropertyValuesHolder;", True, False)])
    ofKeyframe = JavaMultipleMethod([("(Ljava/lang/String;[Landroid/animation/Keyframe;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Landroid/util/Property;[Landroid/animation/Keyframe;)Landroid/animation/PropertyValuesHolder;", True, True)])
    setIntValues = JavaMethod("([I)V", varargs=True)
    setFloatValues = JavaMethod("([F)V", varargs=True)
    setKeyframes = JavaMethod("([Landroid/animation/Keyframe;)V", varargs=True)
    setObjectValues = JavaMethod("([Ljava/lang/Object;)V", varargs=True)
    setConverter = JavaMethod("(Landroid/animation/TypeConverter;)V")
    clone = JavaMethod("()Landroid/animation/PropertyValuesHolder;")
    setEvaluator = JavaMethod("(Landroid/animation/TypeEvaluator;)V")
    setPropertyName = JavaMethod("(Ljava/lang/String;)V")
    setProperty = JavaMethod("(Landroid/util/Property;)V")
    getPropertyName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")