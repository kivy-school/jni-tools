from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppEventListener"]

class AppEventListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/admanager/AppEventListener"
    onAppEvent = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")