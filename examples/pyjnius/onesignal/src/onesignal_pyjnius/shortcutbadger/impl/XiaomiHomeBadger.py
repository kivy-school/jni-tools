from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XiaomiHomeBadger"]

class XiaomiHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/shortcutbadger/impl/XiaomiHomeBadger"
    __javaconstructor__ = [("()V", False)]
    INTENT_ACTION = JavaStaticField("Ljava/lang/String;")
    EXTRA_UPDATE_APP_COMPONENT_NAME = JavaStaticField("Ljava/lang/String;")
    EXTRA_UPDATE_APP_MSG_TEXT = JavaStaticField("Ljava/lang/String;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")