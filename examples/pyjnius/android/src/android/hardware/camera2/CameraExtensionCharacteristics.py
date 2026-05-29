from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CameraExtensionCharacteristics"]

class CameraExtensionCharacteristics(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/CameraExtensionCharacteristics"
    EXTENSION_AUTOMATIC = JavaStaticField("I")
    EXTENSION_BEAUTY = JavaStaticField("I")
    EXTENSION_BOKEH = JavaStaticField("I")
    EXTENSION_FACE_RETOUCH = JavaStaticField("I")
    EXTENSION_HDR = JavaStaticField("I")
    EXTENSION_NIGHT = JavaStaticField("I")
    getEstimatedCaptureLatencyRangeMillis = JavaMethod("(ILandroid/util/Size;I)Landroid/util/Range;")
    getExtensionSupportedSizes = JavaMultipleMethod([("(ILjava/lang/Class;)Ljava/util/List;", False, False), ("(II)Ljava/util/List;", False, False)])
    getPostviewSupportedSizes = JavaMethod("(ILandroid/util/Size;I)Ljava/util/List;")
    getSupportedExtensions = JavaMethod("()Ljava/util/List;")
    isCaptureProcessProgressAvailable = JavaMethod("(I)Z")
    isPostviewAvailable = JavaMethod("(I)Z")
    getAvailableCaptureRequestKeys = JavaMethod("(I)Ljava/util/Set;")
    getAvailableCaptureResultKeys = JavaMethod("(I)Ljava/util/Set;")
    get = JavaMethod("(ILandroid/hardware/camera2/CameraCharacteristics$Key;)Ljava/lang/Object;")
    getKeys = JavaMethod("(I)Ljava/util/Set;")