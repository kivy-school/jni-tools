from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExecuteInIsolatedServiceResponse"]

class ExecuteInIsolatedServiceResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteInIsolatedServiceResponse"
    __javaconstructor__ = [("(Landroid/adservices/ondevicepersonalization/SurfacePackageToken;I)V", False)]
    DEFAULT_BEST_VALUE = JavaStaticField("I")
    getSurfacePackageToken = JavaMethod("()Landroid/adservices/ondevicepersonalization/SurfacePackageToken;")
    getBestValue = JavaMethod("()I")