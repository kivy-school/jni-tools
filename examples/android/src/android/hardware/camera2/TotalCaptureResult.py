from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TotalCaptureResult"]

class TotalCaptureResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/TotalCaptureResult"
    getPartialResults = JavaMethod("()Ljava/util/List;")
    getPhysicalCameraResults = JavaMethod("()Ljava/util/Map;")
    getPhysicalCameraTotalResults = JavaMethod("()Ljava/util/Map;")