from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Capability"]

class Capability(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/Capability"
    __javaconstructor__ = [("(ILandroid/util/Size;Landroid/util/Range;)V", False)]
    getZoomRatioRange = JavaMethod("()Landroid/util/Range;")
    getMaxStreamingSize = JavaMethod("()Landroid/util/Size;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getMode = JavaMethod("()I")