from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SdkSandboxActivityHandler"]

class SdkSandboxActivityHandler(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/sdkprovider/SdkSandboxActivityHandler"
    onActivityCreated = JavaMethod("(Landroid/app/Activity;)V")