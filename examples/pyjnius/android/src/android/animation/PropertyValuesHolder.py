from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyValuesHolder"]

class PropertyValuesHolder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/PropertyValuesHolder"
    ofKeyframe = JavaMultipleMethod([("(Landroid/util/Property;[Landroid/animation/Keyframe;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Ljava/lang/String;[Landroid/animation/Keyframe;)Landroid/animation/PropertyValuesHolder;", True, True)])
    setConverter = JavaMethod("(Landroid/animation/TypeConverter;)V")
    setKeyframes = JavaMethod("([Landroid/animation/Keyframe;)V", varargs=True)
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/animation/PropertyValuesHolder;", False, False)])
    setProperty = JavaMethod("(Landroid/util/Property;)V")
    ofMultiFloat = JavaMultipleMethod([("(Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/PropertyValuesHolder;", True, False), ("(Ljava/lang/String;[[F)Landroid/animation/PropertyValuesHolder;", True, False), ("(Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Landroid/animation/Keyframe;)Landroid/animation/PropertyValuesHolder;", True, True)])
    setPropertyName = JavaMethod("(Ljava/lang/String;)V")
    ofInt = JavaMultipleMethod([("(Ljava/lang/String;[I)Landroid/animation/PropertyValuesHolder;", True, True), ("(Landroid/util/Property;[I)Landroid/animation/PropertyValuesHolder;", True, True)])
    ofObject = JavaMultipleMethod([("(Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/graphics/Path;)Landroid/animation/PropertyValuesHolder;", True, False), ("(Landroid/util/Property;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Ljava/lang/String;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Landroid/util/Property;Landroid/animation/TypeConverter;Landroid/graphics/Path;)Landroid/animation/PropertyValuesHolder;", True, False), ("(Landroid/util/Property;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/PropertyValuesHolder;", True, True)])
    ofMultiInt = JavaMultipleMethod([("(Ljava/lang/String;Landroid/graphics/Path;)Landroid/animation/PropertyValuesHolder;", True, False), ("(Ljava/lang/String;[[I)Landroid/animation/PropertyValuesHolder;", True, False), ("(Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/PropertyValuesHolder;", True, True), ("(Ljava/lang/String;Landroid/animation/TypeConverter;Landroid/animation/TypeEvaluator;[Landroid/animation/Keyframe;)Landroid/animation/PropertyValuesHolder;", True, True)])
    setObjectValues = JavaMethod("([Ljava/lang/Object;)V", varargs=True)
    setIntValues = JavaMethod("([I)V", varargs=True)
    setFloatValues = JavaMethod("([F)V", varargs=True)
    ofFloat = JavaMultipleMethod([("(Ljava/lang/String;[F)Landroid/animation/PropertyValuesHolder;", True, True), ("(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;", True, True)])
    getPropertyName = JavaMethod("()Ljava/lang/String;")
    setEvaluator = JavaMethod("(Landroid/animation/TypeEvaluator;)V")