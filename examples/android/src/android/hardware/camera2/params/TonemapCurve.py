from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TonemapCurve"]

class TonemapCurve(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/TonemapCurve"
    __javaconstructor__ = [("([F[F[F)V", False)]
    CHANNEL_BLUE = JavaStaticField("I")
    CHANNEL_GREEN = JavaStaticField("I")
    CHANNEL_RED = JavaStaticField("I")
    LEVEL_BLACK = JavaStaticField("F")
    LEVEL_WHITE = JavaStaticField("F")
    POINT_SIZE = JavaStaticField("I")
    getPointCount = JavaMethod("(I)I")
    getPoint = JavaMethod("(II)Landroid/graphics/PointF;")
    copyColorCurve = JavaMethod("(I[FI)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")