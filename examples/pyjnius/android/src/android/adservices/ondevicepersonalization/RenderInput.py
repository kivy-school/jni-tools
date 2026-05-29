from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RenderInput"]

class RenderInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/RenderInput"
    __javaconstructor__ = [("(IILandroid/adservices/ondevicepersonalization/RenderingConfig;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getRenderingConfig = JavaMethod("()Landroid/adservices/ondevicepersonalization/RenderingConfig;")
    getHeight = JavaMethod("()I")
    getWidth = JavaMethod("()I")