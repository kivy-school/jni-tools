from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IsolatedServiceException"]

class IsolatedServiceException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/IsolatedServiceException"
    __javaconstructor__ = [("(ILjava/lang/Throwable;)V", False), ("(ILjava/lang/String;Ljava/lang/Throwable;)V", False), ("(I)V", False)]
    getErrorCode = JavaMethod("()I")