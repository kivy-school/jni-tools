from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TopicsManager"]

class TopicsManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/topics/TopicsManager"
    getTopics = JavaMethod("(Landroid/adservices/topics/GetTopicsRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    get = JavaStaticMethod("(Landroid/content/Context;)Landroid/adservices/topics/TopicsManager;")