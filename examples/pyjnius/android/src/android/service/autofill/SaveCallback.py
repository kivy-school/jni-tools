from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SaveCallback"]

class SaveCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/SaveCallback"
    onFailure = JavaMethod("(Ljava/lang/CharSequence;)V")
    onSuccess = JavaMultipleMethod([("(Landroid/content/IntentSender;)V", False, False), ("()V", False, False)])