from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamConfigurationMap"]

class StreamConfigurationMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/StreamConfigurationMap"
    getOutputFormats = JavaMethod("()[I")
    getValidOutputFormatsForInput = JavaMethod("(I)[I")
    getInputFormats = JavaMethod("()[I")
    getInputSizes = JavaMethod("(I)[Landroid/util/Size;")
    isOutputSupportedFor = JavaMultipleMethod([("(I)Z", False, False), ("(Ljava/lang/Class;)Z", True, False), ("(Landroid/view/Surface;)Z", False, False)])
    getOutputSizes = JavaMultipleMethod([("(Ljava/lang/Class;)[Landroid/util/Size;", False, False), ("(I)[Landroid/util/Size;", False, False)])
    getHighSpeedVideoSizes = JavaMethod("()[Landroid/util/Size;")
    getHighSpeedVideoFpsRangesFor = JavaMethod("(Landroid/util/Size;)[Landroid/util/Range;")
    getHighSpeedVideoFpsRanges = JavaMethod("()[Landroid/util/Range;")
    getHighSpeedVideoSizesFor = JavaMethod("(Landroid/util/Range;)[Landroid/util/Size;")
    getHighResolutionOutputSizes = JavaMethod("(I)[Landroid/util/Size;")
    getOutputMinFrameDuration = JavaMultipleMethod([("(ILandroid/util/Size;)J", False, False), ("(Ljava/lang/Class;Landroid/util/Size;)J", False, False)])
    getOutputStallDuration = JavaMultipleMethod([("(ILandroid/util/Size;)J", False, False), ("(Ljava/lang/Class;Landroid/util/Size;)J", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")