from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmConvertedStatus"]

class DrmConvertedStatus(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmConvertedStatus"
    __javaconstructor__ = [("(I[BI)V", False)]
    STATUS_ERROR = JavaStaticField("I")
    STATUS_INPUTDATA_ERROR = JavaStaticField("I")
    STATUS_OK = JavaStaticField("I")
    convertedData = JavaField("[B")
    offset = JavaField("I")
    statusCode = JavaField("I")