from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Interpolator"]

class Interpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Interpolator"
    __javaconstructor__ = [("(I)V", False), ("(II)V", False)]
    reset = JavaMultipleMethod([("(II)V", False, False), ("(I)V", False, False)])
    setKeyFrame = JavaMultipleMethod([("(II[F)V", False, False), ("(II[F[F)V", False, False)])
    timeToValues = JavaMultipleMethod([("([F)Landroid/graphics/Interpolator$Result;", False, False), ("(I[F)Landroid/graphics/Interpolator$Result;", False, False)])
    setRepeatMirror = JavaMethod("(FZ)V")
    getValueCount = JavaMethod("()I")
    getKeyFrameCount = JavaMethod("()I")

    class Result(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/Interpolator$Result"
        FREEZE_END = JavaStaticField("Landroid/graphics/Interpolator$Result;")
        FREEZE_START = JavaStaticField("Landroid/graphics/Interpolator$Result;")
        NORMAL = JavaStaticField("Landroid/graphics/Interpolator$Result;")
        values = JavaStaticMethod("()[Landroid/graphics/Interpolator$Result;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/graphics/Interpolator$Result;")
        FREEZE_END = JavaStaticField("Landroid/graphics/Interpolator$Result;")
        FREEZE_START = JavaStaticField("Landroid/graphics/Interpolator$Result;")
        NORMAL = JavaStaticField("Landroid/graphics/Interpolator$Result;")