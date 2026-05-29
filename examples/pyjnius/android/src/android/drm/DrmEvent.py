from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmEvent"]

class DrmEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmEvent"
    DRM_INFO_OBJECT = JavaStaticField("Ljava/lang/String;")
    DRM_INFO_STATUS_OBJECT = JavaStaticField("Ljava/lang/String;")
    TYPE_ALL_RIGHTS_REMOVED = JavaStaticField("I")
    TYPE_DRM_INFO_PROCESSED = JavaStaticField("I")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()I")
    getUniqueId = JavaMethod("()I")
    getAttribute = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")