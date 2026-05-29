from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PushRegistratorADM"]

class PushRegistratorADM(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/PushRegistratorADM"
    __javaconstructor__ = [("()V", False)]
    registerForPush = JavaMethod("(Landroid/content/Context;Ljava/lang/String;Lcom/onesignal/PushRegistrator$RegisteredHandler;)V")
    fireCallback = JavaStaticMethod("(Ljava/lang/String;)V")