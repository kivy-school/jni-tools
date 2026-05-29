from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImsManager"]

class ImsManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/ImsManager"
    ACTION_WFC_IMS_REGISTRATION_ERROR = JavaStaticField("Ljava/lang/String;")
    EXTRA_WFC_REGISTRATION_FAILURE_MESSAGE = JavaStaticField("Ljava/lang/String;")
    EXTRA_WFC_REGISTRATION_FAILURE_TITLE = JavaStaticField("Ljava/lang/String;")
    getImsMmTelManager = JavaMethod("(I)Landroid/telephony/ims/ImsMmTelManager;")
    getImsRcsManager = JavaMethod("(I)Landroid/telephony/ims/ImsRcsManager;")
    getProvisioningManager = JavaMethod("(I)Landroid/telephony/ims/ProvisioningManager;")