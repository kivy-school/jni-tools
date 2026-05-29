from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MeteringRectangle"]

class MeteringRectangle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/MeteringRectangle"
    __javaconstructor__ = [("(IIIII)V", False), ("(Landroid/graphics/Point;Landroid/util/Size;I)V", False), ("(Landroid/graphics/Rect;I)V", False)]
    METERING_WEIGHT_DONT_CARE = JavaStaticField("I")
    METERING_WEIGHT_MAX = JavaStaticField("I")
    METERING_WEIGHT_MIN = JavaStaticField("I")
    getX = JavaMethod("()I")
    getY = JavaMethod("()I")
    getWidth = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    getMeteringWeight = JavaMethod("()I")
    getUpperLeftPoint = JavaMethod("()Landroid/graphics/Point;")
    getSize = JavaMethod("()Landroid/util/Size;")
    getRect = JavaMethod("()Landroid/graphics/Rect;")
    equals = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Landroid/hardware/camera2/params/MeteringRectangle;)Z", False, False)])
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")