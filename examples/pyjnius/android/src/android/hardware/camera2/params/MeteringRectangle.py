from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MeteringRectangle"]

class MeteringRectangle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/MeteringRectangle"
    __javaconstructor__ = [("(Landroid/graphics/Point;Landroid/util/Size;I)V", False), ("(IIIII)V", False), ("(Landroid/graphics/Rect;I)V", False)]
    METERING_WEIGHT_DONT_CARE = JavaStaticField("I")
    METERING_WEIGHT_MAX = JavaStaticField("I")
    METERING_WEIGHT_MIN = JavaStaticField("I")
    getUpperLeftPoint = JavaMethod("()Landroid/graphics/Point;")
    getMeteringWeight = JavaMethod("()I")
    equals = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Landroid/hardware/camera2/params/MeteringRectangle;)Z", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getSize = JavaMethod("()Landroid/util/Size;")
    getHeight = JavaMethod("()I")
    getWidth = JavaMethod("()I")
    getX = JavaMethod("()I")
    getY = JavaMethod("()I")
    getRect = JavaMethod("()Landroid/graphics/Rect;")