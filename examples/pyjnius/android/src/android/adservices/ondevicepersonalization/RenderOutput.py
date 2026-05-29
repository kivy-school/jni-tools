from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RenderOutput"]

class RenderOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/RenderOutput"
    getTemplateParams = JavaMethod("()Landroid/os/PersistableBundle;")
    getTemplateId = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getContent = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/RenderOutput$Builder"
        __javaconstructor__ = [("()V", False)]
        setTemplateParams = JavaMethod("(Landroid/os/PersistableBundle;)Landroid/adservices/ondevicepersonalization/RenderOutput$Builder;")
        setTemplateId = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/RenderOutput$Builder;")
        setContent = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/RenderOutput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/RenderOutput;")