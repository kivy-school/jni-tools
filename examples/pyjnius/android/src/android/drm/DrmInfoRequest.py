from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmInfoRequest"]

class DrmInfoRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmInfoRequest"
    __javaconstructor__ = [("(ILjava/lang/String;)V", False)]
    ACCOUNT_ID = JavaStaticField("Ljava/lang/String;")
    SUBSCRIPTION_ID = JavaStaticField("Ljava/lang/String;")
    TYPE_REGISTRATION_INFO = JavaStaticField("I")
    TYPE_RIGHTS_ACQUISITION_INFO = JavaStaticField("I")
    TYPE_RIGHTS_ACQUISITION_PROGRESS_INFO = JavaStaticField("I")
    TYPE_UNREGISTRATION_INFO = JavaStaticField("I")
    getInfoType = JavaMethod("()I")
    keyIterator = JavaMethod("()Ljava/util/Iterator;")
    put = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    get = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    getMimeType = JavaMethod("()Ljava/lang/String;")