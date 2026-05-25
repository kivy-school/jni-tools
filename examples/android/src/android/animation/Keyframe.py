from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Keyframe"]

class Keyframe(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/Keyframe"
    __javaconstructor__ = [("()V", False)]
    ofInt = JavaMultipleMethod([("(FI)Landroid/animation/Keyframe;", True, False), ("(F)Landroid/animation/Keyframe;", True, False)])
    ofFloat = JavaMultipleMethod([("(FF)Landroid/animation/Keyframe;", True, False), ("(F)Landroid/animation/Keyframe;", True, False)])
    ofObject = JavaMultipleMethod([("(FLjava/lang/Object;)Landroid/animation/Keyframe;", True, False), ("(F)Landroid/animation/Keyframe;", True, False)])
    hasValue = JavaMethod("()Z")
    getValue = JavaMethod("()Ljava/lang/Object;")
    setValue = JavaMethod("(Ljava/lang/Object;)V")
    getFraction = JavaMethod("()F")
    setFraction = JavaMethod("(F)V")
    getInterpolator = JavaMethod("()Landroid/animation/TimeInterpolator;")
    setInterpolator = JavaMethod("(Landroid/animation/TimeInterpolator;)V")
    getType = JavaMethod("()Ljava/lang/Class;")
    clone = JavaMethod("()Landroid/animation/Keyframe;")