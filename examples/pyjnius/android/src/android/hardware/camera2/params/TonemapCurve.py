from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    copyColorCurve = JavaMethod("(I[FI)V")
    getPoint = JavaMethod("(II)Landroid/graphics/PointF;")
    getPointCount = JavaMethod("(I)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")