from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInAppMessageLifecycleHandler"]

class OSInAppMessageLifecycleHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSInAppMessageLifecycleHandler"
    __javaconstructor__ = [("()V", False)]
    onWillDisplayInAppMessage = JavaMethod("(Lcom/onesignal/OSInAppMessage;)V")
    onDidDisplayInAppMessage = JavaMethod("(Lcom/onesignal/OSInAppMessage;)V")
    onWillDismissInAppMessage = JavaMethod("(Lcom/onesignal/OSInAppMessage;)V")
    onDidDismissInAppMessage = JavaMethod("(Lcom/onesignal/OSInAppMessage;)V")