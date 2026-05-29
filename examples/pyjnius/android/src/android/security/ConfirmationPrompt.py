from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConfirmationPrompt"]

class ConfirmationPrompt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/ConfirmationPrompt"
    cancelPrompt = JavaMethod("()V")
    presentPrompt = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/security/ConfirmationCallback;)V")
    isSupported = JavaStaticMethod("(Landroid/content/Context;)Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/ConfirmationPrompt$Builder"
        __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
        setPromptText = JavaMethod("(Ljava/lang/CharSequence;)Landroid/security/ConfirmationPrompt$Builder;")
        setExtraData = JavaMethod("([B)Landroid/security/ConfirmationPrompt$Builder;")
        build = JavaMethod("()Landroid/security/ConfirmationPrompt;")