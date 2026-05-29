from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentObserver"]

class ContentObserver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/ContentObserver"
    __javaconstructor__ = [("(Landroid/os/Handler;)V", False)]
    dispatchChange = JavaMultipleMethod([("(ZLandroid/net/Uri;I)V", False, False), ("(ZLandroid/net/Uri;)V", False, False), ("(Z)V", False, False), ("(ZLjava/util/Collection;I)V", False, False)])
    onChange = JavaMultipleMethod([("(Z)V", False, False), ("(ZLandroid/net/Uri;)V", False, False), ("(ZLandroid/net/Uri;I)V", False, False), ("(ZLjava/util/Collection;I)V", False, False)])
    deliverSelfNotifications = JavaMethod("()Z")