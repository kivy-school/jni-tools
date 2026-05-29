from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Interpolator"]

class Interpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Interpolator"
    __javaconstructor__ = [("(I)V", False), ("(II)V", False)]
    reset = JavaMultipleMethod([("(I)V", False, False), ("(II)V", False, False)])
    getKeyFrameCount = JavaMethod("()I")
    getValueCount = JavaMethod("()I")
    setKeyFrame = JavaMultipleMethod([("(II[F)V", False, False), ("(II[F[F)V", False, False)])
    setRepeatMirror = JavaMethod("(FZ)V")
    timeToValues = JavaMultipleMethod([("([F)Landroid/graphics/Interpolator$Result;", False, False), ("(I[F)Landroid/graphics/Interpolator$Result;", False, False)])
    finalize = JavaMethod("()V")

    class Result(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/Interpolator/Result"
        values = JavaStaticMethod("()[Landroid/graphics/Interpolator$Result;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/graphics/Interpolator$Result;")
        NORMAL = JavaStaticField("Landroid/graphics/Interpolator/Result;")
        FREEZE_START = JavaStaticField("Landroid/graphics/Interpolator/Result;")
        FREEZE_END = JavaStaticField("Landroid/graphics/Interpolator/Result;")