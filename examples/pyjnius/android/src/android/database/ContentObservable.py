from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentObservable"]

class ContentObservable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/ContentObservable"
    __javaconstructor__ = [("()V", False)]
    dispatchChange = JavaMultipleMethod([("(ZLandroid/net/Uri;)V", False, False), ("(Z)V", False, False)])
    registerObserver = JavaMultipleMethod([("(Landroid/database/ContentObserver;)V", False, False), ("(Ljava/lang/Object;)V", False, False)])
    notifyChange = JavaMethod("(Z)V")