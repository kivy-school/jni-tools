from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class MmTelFeature(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/feature/MmTelFeature"

    class MmTelCapabilities(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/ims/feature/MmTelFeature$MmTelCapabilities"
        CAPABILITY_TYPE_CALL_COMPOSER = JavaStaticField("I")
        CAPABILITY_TYPE_CALL_COMPOSER_BUSINESS_ONLY = JavaStaticField("I")
        CAPABILITY_TYPE_SMS = JavaStaticField("I")
        CAPABILITY_TYPE_UT = JavaStaticField("I")
        CAPABILITY_TYPE_VIDEO = JavaStaticField("I")
        CAPABILITY_TYPE_VOICE = JavaStaticField("I")
        isCapable = JavaMethod("(I)Z")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")