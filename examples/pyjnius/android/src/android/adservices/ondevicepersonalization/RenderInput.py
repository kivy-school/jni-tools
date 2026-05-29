from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RenderInput"]

class RenderInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/RenderInput"
    getWidth = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    getRenderingConfig = JavaMethod("()Landroid/adservices/ondevicepersonalization/RenderingConfig;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")