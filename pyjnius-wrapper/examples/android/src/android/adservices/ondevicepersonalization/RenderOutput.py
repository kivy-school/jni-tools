from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RenderOutput"]

class RenderOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/RenderOutput"
    getContent = JavaMethod("()Ljava/lang/String;")
    getTemplateId = JavaMethod("()Ljava/lang/String;")
    getTemplateParams = JavaMethod("()Landroid/os/PersistableBundle;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/RenderOutput/Builder"
        __javaconstructor__ = [("()V", False)]
        setContent = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/RenderOutput$Builder;")
        setTemplateId = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/RenderOutput$Builder;")
        setTemplateParams = JavaMethod("(Landroid/os/PersistableBundle;)Landroid/adservices/ondevicepersonalization/RenderOutput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/RenderOutput;")