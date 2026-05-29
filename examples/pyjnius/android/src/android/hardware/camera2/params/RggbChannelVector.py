from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RggbChannelVector"]

class RggbChannelVector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/RggbChannelVector"
    __javaconstructor__ = [("(FFFF)V", False)]
    BLUE = JavaStaticField("I")
    COUNT = JavaStaticField("I")
    GREEN_EVEN = JavaStaticField("I")
    GREEN_ODD = JavaStaticField("I")
    RED = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getBlue = JavaMethod("()F")
    getGreenEven = JavaMethod("()F")
    getGreenOdd = JavaMethod("()F")
    getRed = JavaMethod("()F")
    getComponent = JavaMethod("(I)F")
    copyTo = JavaMethod("([FI)V")