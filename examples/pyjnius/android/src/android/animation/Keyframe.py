from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Keyframe"]

class Keyframe(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/Keyframe"
    __javaconstructor__ = [("()V", False)]
    setFraction = JavaMethod("(F)V")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/animation/Keyframe;", False, False)])
    getValue = JavaMethod("()Ljava/lang/Object;")
    setValue = JavaMethod("(Ljava/lang/Object;)V")
    getType = JavaMethod("()Ljava/lang/Class;")
    getFraction = JavaMethod("()F")
    hasValue = JavaMethod("()Z")
    ofInt = JavaMultipleMethod([("(F)Landroid/animation/Keyframe;", True, False), ("(FI)Landroid/animation/Keyframe;", True, False)])
    ofObject = JavaMultipleMethod([("(F)Landroid/animation/Keyframe;", True, False), ("(FLjava/lang/Object;)Landroid/animation/Keyframe;", True, False)])
    ofFloat = JavaMultipleMethod([("(F)Landroid/animation/Keyframe;", True, False), ("(FF)Landroid/animation/Keyframe;", True, False)])
    getInterpolator = JavaMethod("()Landroid/animation/TimeInterpolator;")
    setInterpolator = JavaMethod("(Landroid/animation/TimeInterpolator;)V")