from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EapAkaInfo"]

class EapAkaInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/eap/EapAkaInfo"
    getReauthId = JavaMethod("()[B")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapAkaInfo/Builder"
        __javaconstructor__ = [("()V", False)]
        setReauthId = JavaMethod("([B)Landroid/net/eap/EapAkaInfo$Builder;")
        build = JavaMethod("()Landroid/net/eap/EapAkaInfo;")