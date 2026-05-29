from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentObservable"]

class ContentObservable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/ContentObservable"
    __javaconstructor__ = [("()V", False)]
    registerObserver = JavaMethod("(Landroid/database/ContentObserver;)V")
    dispatchChange = JavaMultipleMethod([("(Z)V", False, False), ("(ZLandroid/net/Uri;)V", False, False)])
    notifyChange = JavaMethod("(Z)V")