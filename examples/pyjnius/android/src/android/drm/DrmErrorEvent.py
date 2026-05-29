from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmErrorEvent"]

class DrmErrorEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmErrorEvent"
    __javaconstructor__ = [("(IILjava/lang/String;)V", False), ("(IILjava/lang/String;Ljava/util/HashMap;)V", False)]
    TYPE_ACQUIRE_DRM_INFO_FAILED = JavaStaticField("I")
    TYPE_NOT_SUPPORTED = JavaStaticField("I")
    TYPE_NO_INTERNET_CONNECTION = JavaStaticField("I")
    TYPE_OUT_OF_MEMORY = JavaStaticField("I")
    TYPE_PROCESS_DRM_INFO_FAILED = JavaStaticField("I")
    TYPE_REMOVE_ALL_RIGHTS_FAILED = JavaStaticField("I")
    TYPE_RIGHTS_NOT_INSTALLED = JavaStaticField("I")
    TYPE_RIGHTS_RENEWAL_NOT_ALLOWED = JavaStaticField("I")
    DRM_INFO_OBJECT = JavaStaticField("Ljava/lang/String;")
    DRM_INFO_STATUS_OBJECT = JavaStaticField("Ljava/lang/String;")
    TYPE_ALL_RIGHTS_REMOVED = JavaStaticField("I")
    TYPE_DRM_INFO_PROCESSED = JavaStaticField("I")