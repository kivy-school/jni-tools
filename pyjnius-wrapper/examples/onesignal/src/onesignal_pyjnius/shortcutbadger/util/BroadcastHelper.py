from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BroadcastHelper"]

class BroadcastHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/shortcutbadger/util/BroadcastHelper"
    __javaconstructor__ = [("()V", False)]
    canResolveBroadcast = JavaStaticMethod("(Landroid/content/Context;Landroid/content/Intent;)Z")
    resolveBroadcast = JavaStaticMethod("(Landroid/content/Context;Landroid/content/Intent;)Ljava/util/List;")
    sendIntentExplicitly = JavaStaticMethod("(Landroid/content/Context;Landroid/content/Intent;)V")