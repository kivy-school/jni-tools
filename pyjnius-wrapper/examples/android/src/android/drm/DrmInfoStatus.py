from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmInfoStatus"]

class DrmInfoStatus(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmInfoStatus"
    __javaconstructor__ = [("(IILandroid/drm/ProcessedData;Ljava/lang/String;)V", False)]
    STATUS_ERROR = JavaStaticField("I")
    STATUS_OK = JavaStaticField("I")
    data = JavaField("Landroid/drm/ProcessedData;")
    infoType = JavaField("I")
    mimeType = JavaField("Ljava/lang/String;")
    statusCode = JavaField("I")