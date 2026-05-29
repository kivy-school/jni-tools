from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NewHtcHomeBadger"]

class NewHtcHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/shortcutbadger/impl/NewHtcHomeBadger"
    __javaconstructor__ = [("()V", False)]
    INTENT_UPDATE_SHORTCUT = JavaStaticField("Ljava/lang/String;")
    INTENT_SET_NOTIFICATION = JavaStaticField("Ljava/lang/String;")
    PACKAGENAME = JavaStaticField("Ljava/lang/String;")
    COUNT = JavaStaticField("Ljava/lang/String;")
    EXTRA_COMPONENT = JavaStaticField("Ljava/lang/String;")
    EXTRA_COUNT = JavaStaticField("Ljava/lang/String;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")