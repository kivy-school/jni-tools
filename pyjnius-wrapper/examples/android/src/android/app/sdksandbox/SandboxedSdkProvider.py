from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SandboxedSdkProvider"]

class SandboxedSdkProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/SandboxedSdkProvider"
    __javaconstructor__ = [("()V", False)]
    attachContext = JavaMethod("(Landroid/content/Context;)V")
    getContext = JavaMethod("()Landroid/content/Context;")
    onLoadSdk = JavaMethod("(Landroid/os/Bundle;)Landroid/app/sdksandbox/SandboxedSdk;")
    beforeUnloadSdk = JavaMethod("()V")
    getView = JavaMethod("(Landroid/content/Context;Landroid/os/Bundle;II)Landroid/view/View;")