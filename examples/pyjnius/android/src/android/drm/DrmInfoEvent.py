from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmInfoEvent"]

class DrmInfoEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmInfoEvent"
    __javaconstructor__ = [("(IILjava/lang/String;)V", False), ("(IILjava/lang/String;Ljava/util/HashMap;)V", False)]
    TYPE_ACCOUNT_ALREADY_REGISTERED = JavaStaticField("I")
    TYPE_ALREADY_REGISTERED_BY_ANOTHER_ACCOUNT = JavaStaticField("I")
    TYPE_REMOVE_RIGHTS = JavaStaticField("I")
    TYPE_RIGHTS_INSTALLED = JavaStaticField("I")
    TYPE_RIGHTS_REMOVED = JavaStaticField("I")
    TYPE_WAIT_FOR_RIGHTS = JavaStaticField("I")
    DRM_INFO_OBJECT = JavaStaticField("Ljava/lang/String;")
    DRM_INFO_STATUS_OBJECT = JavaStaticField("Ljava/lang/String;")
    TYPE_ALL_RIGHTS_REMOVED = JavaStaticField("I")
    TYPE_DRM_INFO_PROCESSED = JavaStaticField("I")