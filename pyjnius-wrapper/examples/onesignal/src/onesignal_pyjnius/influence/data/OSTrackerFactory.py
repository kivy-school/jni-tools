from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSTrackerFactory"]

class OSTrackerFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/influence/data/OSTrackerFactory"
    __javaconstructor__ = [("(Lcom/onesignal/OSSharedPreferences;Lcom/onesignal/OSLogger;Lcom/onesignal/OSTime;)V", False)]
    getInfluences = JavaMethod("()Ljava/util/List;")
    getSessionInfluences = JavaMethod("()Ljava/util/List;")
    getIAMChannelTracker = JavaMethod("()Lcom/onesignal/influence/data/OSChannelTracker;")
    getNotificationChannelTracker = JavaMethod("()Lcom/onesignal/influence/data/OSChannelTracker;")
    getChannels = JavaMethod("()Ljava/util/List;")
    initFromCache = JavaMethod("()V")
    saveInfluenceParams = JavaMethod("(Lcom/onesignal/OneSignalRemoteParams$InfluenceParams;)V")
    addSessionData = JavaMethod("(Lorg/json/JSONObject;Ljava/util/List;)V")
    getChannelByEntryAction = JavaMethod("(Lcom/onesignal/OneSignal$AppEntryAction;)Lcom/onesignal/influence/data/OSChannelTracker;")
    getChannelsToResetByEntryAction = JavaMethod("(Lcom/onesignal/OneSignal$AppEntryAction;)Ljava/util/List;")

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/influence/data/OSTrackerFactory/WhenMappings"