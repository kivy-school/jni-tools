from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImsException"]

class ImsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/ImsException"
    CODE_ERROR_INVALID_SUBSCRIPTION = JavaStaticField("I")
    CODE_ERROR_SERVICE_UNAVAILABLE = JavaStaticField("I")
    CODE_ERROR_UNSPECIFIED = JavaStaticField("I")
    CODE_ERROR_UNSUPPORTED_OPERATION = JavaStaticField("I")
    getCode = JavaMethod("()I")