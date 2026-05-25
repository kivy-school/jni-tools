from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Badger"]

class Badger(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/shortcutbadger/Badger"
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")