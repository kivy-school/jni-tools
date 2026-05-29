from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallbackThreadManager"]

class CallbackThreadManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/CallbackThreadManager"
    __javaconstructor__ = [("()V", False)]
    Companion = JavaStaticField("Lcom/onesignal/CallbackThreadManager$Companion;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/CallbackThreadManager/Companion"
        getPreference = JavaMethod("()Lcom/onesignal/CallbackThreadManager$UseThread;")
        setPreference = JavaMethod("(Lcom/onesignal/CallbackThreadManager$UseThread;)V")
        runOnPreferred = JavaMethod("(Ljava/lang/Runnable;)V")

        class WhenMappings(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "com/onesignal/CallbackThreadManager/Companion/WhenMappings"

    class UseThread(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/CallbackThreadManager/UseThread"
        values = JavaStaticMethod("()[Lcom/onesignal/CallbackThreadManager$UseThread;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/CallbackThreadManager$UseThread;")
        MainUI = JavaStaticField("Lcom/onesignal/CallbackThreadManager/UseThread;")
        Background = JavaStaticField("Lcom/onesignal/CallbackThreadManager/UseThread;")