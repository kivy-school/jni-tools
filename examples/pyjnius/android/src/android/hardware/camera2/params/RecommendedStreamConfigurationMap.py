from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecommendedStreamConfigurationMap"]

class RecommendedStreamConfigurationMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/RecommendedStreamConfigurationMap"
    USECASE_10BIT_OUTPUT = JavaStaticField("I")
    USECASE_LOW_LATENCY_SNAPSHOT = JavaStaticField("I")
    USECASE_PREVIEW = JavaStaticField("I")
    USECASE_RAW = JavaStaticField("I")
    USECASE_RECORD = JavaStaticField("I")
    USECASE_SNAPSHOT = JavaStaticField("I")
    USECASE_VIDEO_SNAPSHOT = JavaStaticField("I")
    USECASE_ZSL = JavaStaticField("I")
    getHighSpeedVideoSizesFor = JavaMethod("(Landroid/util/Range;)Ljava/util/Set;")
    getInputFormats = JavaMethod("()Ljava/util/Set;")
    getInputSizes = JavaMethod("(I)Ljava/util/Set;")
    getOutputFormats = JavaMethod("()Ljava/util/Set;")
    getOutputMinFrameDuration = JavaMultipleMethod([("(Ljava/lang/Class;Landroid/util/Size;)J", False, False), ("(ILandroid/util/Size;)J", False, False)])
    getOutputSizes = JavaMultipleMethod([("(I)Ljava/util/Set;", False, False), ("(Ljava/lang/Class;)Ljava/util/Set;", False, False)])
    getOutputStallDuration = JavaMultipleMethod([("(ILandroid/util/Size;)J", False, False), ("(Ljava/lang/Class;Landroid/util/Size;)J", False, False)])
    getRecommendedUseCase = JavaMethod("()I")
    getValidOutputFormatsForInput = JavaMethod("(I)Ljava/util/Set;")
    getHighResolutionOutputSizes = JavaMethod("(I)Ljava/util/Set;")
    getHighSpeedVideoFpsRanges = JavaMethod("()Ljava/util/Set;")
    getHighSpeedVideoFpsRangesFor = JavaMethod("(Landroid/util/Size;)Ljava/util/Set;")
    getHighSpeedVideoSizes = JavaMethod("()Ljava/util/Set;")
    isOutputSupportedFor = JavaMultipleMethod([("(Landroid/view/Surface;)Z", False, False), ("(I)Z", False, False)])