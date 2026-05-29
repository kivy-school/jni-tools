from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SdkSandboxClientImportanceListener"]

class SdkSandboxClientImportanceListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/sdkprovider/SdkSandboxClientImportanceListener"
    onForegroundImportanceChanged = JavaMethod("(Z)V")