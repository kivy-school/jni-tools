from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OneSignal"]

class OneSignal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OneSignal"
    __javaconstructor__ = [("()V", False)]
    sdkType = JavaStaticField("Ljava/lang/String;")
    getSdkVersionRaw = JavaStaticMethod("()Ljava/lang/String;")
    getDeviceState = JavaStaticMethod("()Lcom/onesignal/OSDeviceState;")
    unsubscribeWhenNotificationsAreDisabled = JavaStaticMethod("(Z)V")
    setAppId = JavaStaticMethod("(Ljava/lang/String;)V")
    initWithContext = JavaStaticMethod("(Landroid/content/Context;)V")
    setNotificationWillShowInForegroundHandler = JavaStaticMethod("(Lcom/onesignal/OneSignal$OSNotificationWillShowInForegroundHandler;)V")
    setInAppMessageLifecycleHandler = JavaStaticMethod("(Lcom/onesignal/OSInAppMessageLifecycleHandler;)V")
    setNotificationOpenedHandler = JavaStaticMethod("(Lcom/onesignal/OneSignal$OSNotificationOpenedHandler;)V")
    setInAppMessageClickHandler = JavaStaticMethod("(Lcom/onesignal/OneSignal$OSInAppMessageClickHandler;)V")
    userProvidedPrivacyConsent = JavaStaticMethod("()Z")
    onesignalLog = JavaStaticMethod("(Lcom/onesignal/OneSignal$LOG_LEVEL;Ljava/lang/String;)V")
    provideUserConsent = JavaStaticMethod("(Z)V")
    requiresUserPrivacyConsent = JavaStaticMethod("()Z")
    setRequiresUserPrivacyConsent = JavaStaticMethod("(Z)V")
    setLogLevel = JavaMultipleMethod([("(Lcom/onesignal/OneSignal$LOG_LEVEL;Lcom/onesignal/OneSignal$LOG_LEVEL;)V", True, False), ("(II)V", True, False)])
    setSMSNumber = JavaMultipleMethod([("(Ljava/lang/String;Lcom/onesignal/OneSignal$OSSMSUpdateHandler;)V", True, False), ("(Ljava/lang/String;)V", True, False), ("(Ljava/lang/String;Ljava/lang/String;)V", True, False), ("(Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/OneSignal$OSSMSUpdateHandler;)V", True, False)])
    logoutSMSNumber = JavaMultipleMethod([("()V", True, False), ("(Lcom/onesignal/OneSignal$OSSMSUpdateHandler;)V", True, False)])
    setEmail = JavaMultipleMethod([("(Ljava/lang/String;Lcom/onesignal/OneSignal$EmailUpdateHandler;)V", True, False), ("(Ljava/lang/String;)V", True, False), ("(Ljava/lang/String;Ljava/lang/String;)V", True, False), ("(Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/OneSignal$EmailUpdateHandler;)V", True, False)])
    logoutEmail = JavaMultipleMethod([("()V", True, False), ("(Lcom/onesignal/OneSignal$EmailUpdateHandler;)V", True, False)])
    setLanguage = JavaMultipleMethod([("(Ljava/lang/String;)V", True, False), ("(Ljava/lang/String;Lcom/onesignal/OneSignal$OSSetLanguageCompletionHandler;)V", True, False)])
    setExternalUserId = JavaMultipleMethod([("(Ljava/lang/String;)V", True, False), ("(Ljava/lang/String;Lcom/onesignal/OneSignal$OSExternalUserIdUpdateCompletionHandler;)V", True, False), ("(Ljava/lang/String;Ljava/lang/String;)V", True, False), ("(Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/OneSignal$OSExternalUserIdUpdateCompletionHandler;)V", True, False)])
    removeExternalUserId = JavaMultipleMethod([("()V", True, False), ("(Lcom/onesignal/OneSignal$OSExternalUserIdUpdateCompletionHandler;)V", True, False)])
    sendTag = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    sendTags = JavaMultipleMethod([("(Ljava/lang/String;)V", True, False), ("(Lorg/json/JSONObject;)V", True, False), ("(Lorg/json/JSONObject;Lcom/onesignal/OneSignal$ChangeTagsUpdateHandler;)V", True, False)])
    postNotification = JavaMultipleMethod([("(Ljava/lang/String;Lcom/onesignal/OneSignal$PostNotificationResponseHandler;)V", True, False), ("(Lorg/json/JSONObject;Lcom/onesignal/OneSignal$PostNotificationResponseHandler;)V", True, False)])
    getTags = JavaStaticMethod("(Lcom/onesignal/OneSignal$OSGetTagsHandler;)V")
    deleteTag = JavaMultipleMethod([("(Ljava/lang/String;)V", True, False), ("(Ljava/lang/String;Lcom/onesignal/OneSignal$ChangeTagsUpdateHandler;)V", True, False)])
    deleteTags = JavaMultipleMethod([("(Ljava/util/Collection;)V", True, False), ("(Ljava/util/Collection;Lcom/onesignal/OneSignal$ChangeTagsUpdateHandler;)V", True, False), ("(Ljava/lang/String;)V", True, False), ("(Ljava/lang/String;Lcom/onesignal/OneSignal$ChangeTagsUpdateHandler;)V", True, False), ("(Lorg/json/JSONArray;Lcom/onesignal/OneSignal$ChangeTagsUpdateHandler;)V", True, False)])
    isLocationShared = JavaStaticMethod("()Z")
    disablePush = JavaStaticMethod("(Z)V")
    disableGMSMissingPrompt = JavaStaticMethod("(Z)V")
    setLocationShared = JavaStaticMethod("(Z)V")
    promptLocation = JavaStaticMethod("()V")
    promptForPushNotifications = JavaMultipleMethod([("()V", True, False), ("(Z)V", True, False), ("(ZLcom/onesignal/OneSignal$PromptForPushNotificationPermissionResponseHandler;)V", True, False)])
    clearOneSignalNotifications = JavaStaticMethod("()V")
    removeNotification = JavaStaticMethod("(I)V")
    removeGroupedNotifications = JavaStaticMethod("(Ljava/lang/String;)V")
    addPermissionObserver = JavaStaticMethod("(Lcom/onesignal/OSPermissionObserver;)V")
    removePermissionObserver = JavaStaticMethod("(Lcom/onesignal/OSPermissionObserver;)V")
    addSubscriptionObserver = JavaStaticMethod("(Lcom/onesignal/OSSubscriptionObserver;)V")
    removeSubscriptionObserver = JavaStaticMethod("(Lcom/onesignal/OSSubscriptionObserver;)V")
    addEmailSubscriptionObserver = JavaStaticMethod("(Lcom/onesignal/OSEmailSubscriptionObserver;)V")
    removeEmailSubscriptionObserver = JavaStaticMethod("(Lcom/onesignal/OSEmailSubscriptionObserver;)V")
    addSMSSubscriptionObserver = JavaStaticMethod("(Lcom/onesignal/OSSMSSubscriptionObserver;)V")
    removeSMSSubscriptionObserver = JavaStaticMethod("(Lcom/onesignal/OSSMSSubscriptionObserver;)V")
    addTriggers = JavaStaticMethod("(Ljava/util/Map;)V")
    addTrigger = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    removeTriggersForKeys = JavaStaticMethod("(Ljava/util/Collection;)V")
    removeTriggerForKey = JavaStaticMethod("(Ljava/lang/String;)V")
    getTriggerValueForKey = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    getTriggers = JavaStaticMethod("()Ljava/util/Map;")
    pauseInAppMessages = JavaStaticMethod("(Z)V")
    isInAppMessagingPaused = JavaStaticMethod("()Z")
    sendOutcome = JavaMultipleMethod([("(Ljava/lang/String;)V", True, False), ("(Ljava/lang/String;Lcom/onesignal/OneSignal$OutcomeCallback;)V", True, False)])
    sendUniqueOutcome = JavaMultipleMethod([("(Ljava/lang/String;)V", True, False), ("(Ljava/lang/String;Lcom/onesignal/OneSignal$OutcomeCallback;)V", True, False)])
    sendOutcomeWithValue = JavaMultipleMethod([("(Ljava/lang/String;F)V", True, False), ("(Ljava/lang/String;FLcom/onesignal/OneSignal$OutcomeCallback;)V", True, False)])

    class AppEntryAction(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/AppEntryAction"
        values = JavaStaticMethod("()[Lcom/onesignal/OneSignal$AppEntryAction;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/OneSignal$AppEntryAction;")
        isNotificationClick = JavaMethod("()Z")
        isAppOpen = JavaMethod("()Z")
        isAppClose = JavaMethod("()Z")
        NOTIFICATION_CLICK = JavaStaticField("Lcom/onesignal/OneSignal/AppEntryAction;")
        APP_OPEN = JavaStaticField("Lcom/onesignal/OneSignal/AppEntryAction;")
        APP_CLOSE = JavaStaticField("Lcom/onesignal/OneSignal/AppEntryAction;")

    class ChangeTagsUpdateHandler(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/ChangeTagsUpdateHandler"
        onSuccess = JavaMethod("(Lorg/json/JSONObject;)V")
        onFailure = JavaMethod("(Lcom/onesignal/OneSignal$SendTagsError;)V")

    class EmailErrorType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/EmailErrorType"
        values = JavaStaticMethod("()[Lcom/onesignal/OneSignal$EmailErrorType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/OneSignal$EmailErrorType;")
        VALIDATION = JavaStaticField("Lcom/onesignal/OneSignal/EmailErrorType;")
        REQUIRES_EMAIL_AUTH = JavaStaticField("Lcom/onesignal/OneSignal/EmailErrorType;")
        INVALID_OPERATION = JavaStaticField("Lcom/onesignal/OneSignal/EmailErrorType;")
        NETWORK = JavaStaticField("Lcom/onesignal/OneSignal/EmailErrorType;")

    class EmailUpdateError(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/EmailUpdateError"
        getType = JavaMethod("()Lcom/onesignal/OneSignal$EmailErrorType;")
        getMessage = JavaMethod("()Ljava/lang/String;")

    class EmailUpdateHandler(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/EmailUpdateHandler"
        onSuccess = JavaMethod("()V")
        onFailure = JavaMethod("(Lcom/onesignal/OneSignal$EmailUpdateError;)V")

    class ExternalIdError(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/ExternalIdError"
        getType = JavaMethod("()Lcom/onesignal/OneSignal$ExternalIdErrorType;")
        getMessage = JavaMethod("()Ljava/lang/String;")

    class ExternalIdErrorType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/ExternalIdErrorType"
        values = JavaStaticMethod("()[Lcom/onesignal/OneSignal$ExternalIdErrorType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/OneSignal$ExternalIdErrorType;")
        REQUIRES_EXTERNAL_ID_AUTH = JavaStaticField("Lcom/onesignal/OneSignal/ExternalIdErrorType;")
        INVALID_OPERATION = JavaStaticField("Lcom/onesignal/OneSignal/ExternalIdErrorType;")
        NETWORK = JavaStaticField("Lcom/onesignal/OneSignal/ExternalIdErrorType;")

    class LOG_LEVEL(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/LOG_LEVEL"
        values = JavaStaticMethod("()[Lcom/onesignal/OneSignal$LOG_LEVEL;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/OneSignal$LOG_LEVEL;")
        NONE = JavaStaticField("Lcom/onesignal/OneSignal/LOG_LEVEL;")
        FATAL = JavaStaticField("Lcom/onesignal/OneSignal/LOG_LEVEL;")
        ERROR = JavaStaticField("Lcom/onesignal/OneSignal/LOG_LEVEL;")
        WARN = JavaStaticField("Lcom/onesignal/OneSignal/LOG_LEVEL;")
        INFO = JavaStaticField("Lcom/onesignal/OneSignal/LOG_LEVEL;")
        DEBUG = JavaStaticField("Lcom/onesignal/OneSignal/LOG_LEVEL;")
        VERBOSE = JavaStaticField("Lcom/onesignal/OneSignal/LOG_LEVEL;")

    class OSExternalUserIdUpdateCompletionHandler(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/OSExternalUserIdUpdateCompletionHandler"
        onSuccess = JavaMethod("(Lorg/json/JSONObject;)V")
        onFailure = JavaMethod("(Lcom/onesignal/OneSignal$ExternalIdError;)V")

    class OSGetTagsHandler(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/OSGetTagsHandler"
        tagsAvailable = JavaMethod("(Lorg/json/JSONObject;)V")

    class OSInAppMessageClickHandler(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/OSInAppMessageClickHandler"
        inAppMessageClicked = JavaMethod("(Lcom/onesignal/OSInAppMessageAction;)V")

    class OSLanguageError(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/OSLanguageError"
        getCode = JavaMethod("()I")
        getMessage = JavaMethod("()Ljava/lang/String;")

    class OSNotificationOpenedHandler(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/OSNotificationOpenedHandler"
        notificationOpened = JavaMethod("(Lcom/onesignal/OSNotificationOpenedResult;)V")

    class OSNotificationWillShowInForegroundHandler(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/OSNotificationWillShowInForegroundHandler"
        notificationWillShowInForeground = JavaMethod("(Lcom/onesignal/OSNotificationReceivedEvent;)V")

    class OSRemoteNotificationReceivedHandler(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/OSRemoteNotificationReceivedHandler"
        remoteNotificationReceived = JavaMethod("(Landroid/content/Context;Lcom/onesignal/OSNotificationReceivedEvent;)V")

    class OSSMSUpdateError(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/OSSMSUpdateError"
        getType = JavaMethod("()Lcom/onesignal/OneSignal$SMSErrorType;")
        getMessage = JavaMethod("()Ljava/lang/String;")

    class OSSMSUpdateHandler(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/OSSMSUpdateHandler"
        onSuccess = JavaMethod("(Lorg/json/JSONObject;)V")
        onFailure = JavaMethod("(Lcom/onesignal/OneSignal$OSSMSUpdateError;)V")

    class OSSetLanguageCompletionHandler(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/OSSetLanguageCompletionHandler"
        onSuccess = JavaMethod("(Ljava/lang/String;)V")
        onFailure = JavaMethod("(Lcom/onesignal/OneSignal$OSLanguageError;)V")

    class OutcomeCallback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/OutcomeCallback"
        onSuccess = JavaMethod("(Lcom/onesignal/OSOutcomeEvent;)V")

    class PostNotificationResponseHandler(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/PostNotificationResponseHandler"
        onSuccess = JavaMethod("(Lorg/json/JSONObject;)V")
        onFailure = JavaMethod("(Lorg/json/JSONObject;)V")

    class PromptForPushNotificationPermissionResponseHandler(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/PromptForPushNotificationPermissionResponseHandler"
        response = JavaMethod("(Z)V")

    class SMSErrorType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/SMSErrorType"
        values = JavaStaticMethod("()[Lcom/onesignal/OneSignal$SMSErrorType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/OneSignal$SMSErrorType;")
        VALIDATION = JavaStaticField("Lcom/onesignal/OneSignal/SMSErrorType;")
        REQUIRES_SMS_AUTH = JavaStaticField("Lcom/onesignal/OneSignal/SMSErrorType;")
        INVALID_OPERATION = JavaStaticField("Lcom/onesignal/OneSignal/SMSErrorType;")
        NETWORK = JavaStaticField("Lcom/onesignal/OneSignal/SMSErrorType;")

    class SendTagsError(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OneSignal/SendTagsError"
        getCode = JavaMethod("()I")
        getMessage = JavaMethod("()Ljava/lang/String;")