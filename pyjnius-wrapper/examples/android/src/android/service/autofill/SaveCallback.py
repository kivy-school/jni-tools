from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SaveCallback"]

class SaveCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/SaveCallback"
    onSuccess = JavaMultipleMethod([("()V", False, False), ("(Landroid/content/IntentSender;)V", False, False)])
    onFailure = JavaMethod("(Ljava/lang/CharSequence;)V")