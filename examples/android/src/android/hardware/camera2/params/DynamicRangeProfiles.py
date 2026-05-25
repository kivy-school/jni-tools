from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DynamicRangeProfiles"]

class DynamicRangeProfiles(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/DynamicRangeProfiles"
    __javaconstructor__ = [("([J)V", False)]
    DOLBY_VISION_10B_HDR_OEM = JavaStaticField("J")
    DOLBY_VISION_10B_HDR_OEM_PO = JavaStaticField("J")
    DOLBY_VISION_10B_HDR_REF = JavaStaticField("J")
    DOLBY_VISION_10B_HDR_REF_PO = JavaStaticField("J")
    DOLBY_VISION_8B_HDR_OEM = JavaStaticField("J")
    DOLBY_VISION_8B_HDR_OEM_PO = JavaStaticField("J")
    DOLBY_VISION_8B_HDR_REF = JavaStaticField("J")
    DOLBY_VISION_8B_HDR_REF_PO = JavaStaticField("J")
    HDR10 = JavaStaticField("J")
    HDR10_PLUS = JavaStaticField("J")
    HLG10 = JavaStaticField("J")
    PUBLIC_MAX = JavaStaticField("J")
    STANDARD = JavaStaticField("J")
    getSupportedProfiles = JavaMethod("()Ljava/util/Set;")
    getProfileCaptureRequestConstraints = JavaMethod("(J)Ljava/util/Set;")
    isExtraLatencyPresent = JavaMethod("(J)Z")