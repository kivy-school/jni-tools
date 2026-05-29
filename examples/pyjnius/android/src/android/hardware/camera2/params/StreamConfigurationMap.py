from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamConfigurationMap"]

class StreamConfigurationMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/StreamConfigurationMap"
    getHighSpeedVideoSizesFor = JavaMethod("(Landroid/util/Range;)[Landroid/util/Size;")
    getInputFormats = JavaMethod("()[I")
    getInputSizes = JavaMethod("(I)[Landroid/util/Size;")
    getOutputFormats = JavaMethod("()[I")
    getOutputMinFrameDuration = JavaMultipleMethod([("(ILandroid/util/Size;)J", False, False), ("(Ljava/lang/Class;Landroid/util/Size;)J", False, False)])
    getOutputSizes = JavaMultipleMethod([("(Ljava/lang/Class;)[Landroid/util/Size;", False, False), ("(I)[Landroid/util/Size;", False, False)])
    getOutputStallDuration = JavaMultipleMethod([("(Ljava/lang/Class;Landroid/util/Size;)J", False, False), ("(ILandroid/util/Size;)J", False, False)])
    getValidOutputFormatsForInput = JavaMethod("(I)[I")
    getHighResolutionOutputSizes = JavaMethod("(I)[Landroid/util/Size;")
    getHighSpeedVideoFpsRanges = JavaMethod("()[Landroid/util/Range;")
    getHighSpeedVideoFpsRangesFor = JavaMethod("(Landroid/util/Size;)[Landroid/util/Range;")
    getHighSpeedVideoSizes = JavaMethod("()[Landroid/util/Size;")
    isOutputSupportedFor = JavaMultipleMethod([("(Landroid/view/Surface;)Z", False, False), ("(Ljava/lang/Class;)Z", True, False), ("(I)Z", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")