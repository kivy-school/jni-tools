from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RequestSurfacePackageException"]

class RequestSurfacePackageException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/RequestSurfacePackageException"
    __javaconstructor__ = [("(ILjava/lang/String;)V", False), ("(ILjava/lang/String;Ljava/lang/Throwable;)V", False), ("(ILjava/lang/String;Ljava/lang/Throwable;Landroid/os/Bundle;)V", False)]
    getRequestSurfacePackageErrorCode = JavaMethod("()I")
    getExtraErrorInformation = JavaMethod("()Landroid/os/Bundle;")