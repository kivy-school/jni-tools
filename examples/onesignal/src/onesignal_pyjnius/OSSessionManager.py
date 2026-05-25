from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSSessionManager"]

class OSSessionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSSessionManager"
    __javaconstructor__ = [("(Lcom/onesignal/OSSessionManager$SessionListener;Lcom/onesignal/influence/data/OSTrackerFactory;Lcom/onesignal/OSLogger;)V", False)]
    trackerFactory = JavaField("Lcom/onesignal/influence/data/OSTrackerFactory;")

    class SessionListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OSSessionManager/SessionListener"
        onSessionEnding = JavaMethod("(Ljava/util/List;)V")