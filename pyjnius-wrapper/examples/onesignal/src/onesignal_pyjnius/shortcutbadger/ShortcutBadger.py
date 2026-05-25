from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ShortcutBadger"]

class ShortcutBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/shortcutbadger/ShortcutBadger"
    applyCount = JavaStaticMethod("(Landroid/content/Context;I)Z")
    applyCountOrThrow = JavaStaticMethod("(Landroid/content/Context;I)V")
    removeCount = JavaStaticMethod("(Landroid/content/Context;)Z")
    removeCountOrThrow = JavaStaticMethod("(Landroid/content/Context;)V")
    isBadgeCounterSupported = JavaStaticMethod("(Landroid/content/Context;)Z")
    applyNotification = JavaStaticMethod("(Landroid/content/Context;Landroid/app/Notification;I)V")