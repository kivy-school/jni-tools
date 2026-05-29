from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmEvent"]

class DrmEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmEvent"
    __javaconstructor__ = [("(IILjava/lang/String;Ljava/util/HashMap;)V", False), ("(IILjava/lang/String;)V", False)]
    DRM_INFO_OBJECT = JavaStaticField("Ljava/lang/String;")
    DRM_INFO_STATUS_OBJECT = JavaStaticField("Ljava/lang/String;")
    TYPE_ALL_RIGHTS_REMOVED = JavaStaticField("I")
    TYPE_DRM_INFO_PROCESSED = JavaStaticField("I")
    getUniqueId = JavaMethod("()I")
    getType = JavaMethod("()I")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getAttribute = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")