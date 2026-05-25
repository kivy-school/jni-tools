from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentObserver"]

class ContentObserver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/ContentObserver"
    __javaconstructor__ = [("(Landroid/os/Handler;)V", False)]
    deliverSelfNotifications = JavaMethod("()Z")
    onChange = JavaMultipleMethod([("(Z)V", False, False), ("(ZLandroid/net/Uri;)V", False, False), ("(ZLandroid/net/Uri;I)V", False, False), ("(ZLjava/util/Collection;I)V", False, False)])
    dispatchChange = JavaMultipleMethod([("(Z)V", False, False), ("(ZLandroid/net/Uri;)V", False, False), ("(ZLandroid/net/Uri;I)V", False, False), ("(ZLjava/util/Collection;I)V", False, False)])