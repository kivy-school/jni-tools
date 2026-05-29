from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyStoreParameter"]

class KeyStoreParameter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/KeyStoreParameter"
    isEncryptionRequired = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/KeyStoreParameter$Builder"
        __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
        setEncryptionRequired = JavaMethod("(Z)Landroid/security/KeyStoreParameter$Builder;")
        build = JavaMethod("()Landroid/security/KeyStoreParameter;")