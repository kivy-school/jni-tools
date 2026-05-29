from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Capability"]

class Capability(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/Capability"
    __javaconstructor__ = [("(ILandroid/util/Size;Landroid/util/Range;)V", False)]
    getMode = JavaMethod("()I")
    getMaxStreamingSize = JavaMethod("()Landroid/util/Size;")
    getZoomRatioRange = JavaMethod("()Landroid/util/Range;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")