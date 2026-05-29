from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SdkSandboxActivityHandler"]

class SdkSandboxActivityHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/sdkprovider/SdkSandboxActivityHandler"
    onActivityCreated = JavaMethod("(Landroid/app/Activity;)V")