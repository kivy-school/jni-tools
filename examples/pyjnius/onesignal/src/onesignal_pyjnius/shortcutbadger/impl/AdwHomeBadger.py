from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdwHomeBadger"]

class AdwHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/shortcutbadger/impl/AdwHomeBadger"
    __javaconstructor__ = [("()V", False)]
    INTENT_UPDATE_COUNTER = JavaStaticField("Ljava/lang/String;")
    PACKAGENAME = JavaStaticField("Ljava/lang/String;")
    CLASSNAME = JavaStaticField("Ljava/lang/String;")
    COUNT = JavaStaticField("Ljava/lang/String;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")