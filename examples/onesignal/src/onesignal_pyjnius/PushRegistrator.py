from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PushRegistrator"]

class PushRegistrator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/PushRegistrator"
    registerForPush = JavaMethod("(Landroid/content/Context;Ljava/lang/String;Lcom/onesignal/PushRegistrator$RegisteredHandler;)V")

    class RegisteredHandler(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/PushRegistrator/RegisteredHandler"
        complete = JavaMethod("(Ljava/lang/String;I)V")