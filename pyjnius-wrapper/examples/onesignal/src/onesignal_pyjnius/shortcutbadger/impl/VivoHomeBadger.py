from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VivoHomeBadger"]

class VivoHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/shortcutbadger/impl/VivoHomeBadger"
    __javaconstructor__ = [("()V", False)]
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")