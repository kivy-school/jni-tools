from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImsRegistrationImplBase"]

class ImsRegistrationImplBase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/stub/ImsRegistrationImplBase"
    REGISTRATION_TECH_3G = JavaStaticField("I")
    REGISTRATION_TECH_CROSS_SIM = JavaStaticField("I")
    REGISTRATION_TECH_IWLAN = JavaStaticField("I")
    REGISTRATION_TECH_LTE = JavaStaticField("I")
    REGISTRATION_TECH_NONE = JavaStaticField("I")
    REGISTRATION_TECH_NR = JavaStaticField("I")