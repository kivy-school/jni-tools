from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppSetIdManager"]

class AppSetIdManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/appsetid/AppSetIdManager"
    get = JavaStaticMethod("(Landroid/content/Context;)Landroid/adservices/appsetid/AppSetIdManager;")
    getAppSetId = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")