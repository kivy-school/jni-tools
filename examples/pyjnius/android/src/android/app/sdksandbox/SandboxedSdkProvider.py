from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SandboxedSdkProvider"]

class SandboxedSdkProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/SandboxedSdkProvider"
    __javaconstructor__ = [("()V", False)]
    beforeUnloadSdk = JavaMethod("()V")
    attachContext = JavaMethod("(Landroid/content/Context;)V")
    onLoadSdk = JavaMethod("(Landroid/os/Bundle;)Landroid/app/sdksandbox/SandboxedSdk;")
    getContext = JavaMethod("()Landroid/content/Context;")
    getView = JavaMethod("(Landroid/content/Context;Landroid/os/Bundle;II)Landroid/view/View;")