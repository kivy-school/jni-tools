from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CompanionDeviceManager"]

class CompanionDeviceManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/CompanionDeviceManager"
    EXTRA_ASSOCIATION = JavaStaticField("Ljava/lang/String;")
    EXTRA_DEVICE = JavaStaticField("Ljava/lang/String;")
    FLAG_CALL_METADATA = JavaStaticField("I")
    RESULT_CANCELED = JavaStaticField("I")
    RESULT_DISCOVERY_TIMEOUT = JavaStaticField("I")
    RESULT_INTERNAL_ERROR = JavaStaticField("I")
    RESULT_OK = JavaStaticField("I")
    RESULT_SECURITY_ERROR = JavaStaticField("I")
    RESULT_USER_REJECTED = JavaStaticField("I")
    getAssociations = JavaMethod("()Ljava/util/List;")
    getMyAssociations = JavaMethod("()Ljava/util/List;")
    removeBond = JavaMethod("(I)Z")
    associate = JavaMultipleMethod([("(Landroid/companion/AssociationRequest;Landroid/companion/CompanionDeviceManager$Callback;Landroid/os/Handler;)V", False, False), ("(Landroid/companion/AssociationRequest;Ljava/util/concurrent/Executor;Landroid/companion/CompanionDeviceManager$Callback;)V", False, False)])
    attachSystemDataTransport = JavaMethod("(ILjava/io/InputStream;Ljava/io/OutputStream;)V")
    disassociate = JavaMultipleMethod([("(I)V", False, False), ("(Ljava/lang/String;)V", False, False)])
    buildAssociationCancellationIntent = JavaMethod("()Landroid/content/IntentSender;")
    buildPermissionTransferUserConsentIntent = JavaMethod("(I)Landroid/content/IntentSender;")
    detachSystemDataTransport = JavaMethod("(I)V")
    disableSystemDataSyncForTypes = JavaMethod("(II)V")
    enableSystemDataSyncForTypes = JavaMethod("(II)V")
    hasNotificationAccess = JavaMethod("(Landroid/content/ComponentName;)Z")
    isPermissionTransferUserConsented = JavaMethod("(I)Z")
    requestNotificationAccess = JavaMethod("(Landroid/content/ComponentName;)V")
    startObservingDevicePresence = JavaMultipleMethod([("(Landroid/companion/ObservingDevicePresenceRequest;)V", False, False), ("(Ljava/lang/String;)V", False, False)])
    startSystemDataTransfer = JavaMethod("(ILjava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    stopObservingDevicePresence = JavaMultipleMethod([("(Landroid/companion/ObservingDevicePresenceRequest;)V", False, False), ("(Ljava/lang/String;)V", False, False)])
    setDeviceId = JavaMethod("(ILandroid/companion/DeviceId;)V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/companion/CompanionDeviceManager$Callback"
        __javaconstructor__ = [("()V", False)]
        onFailure = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(ILjava/lang/CharSequence;)V", False, False)])
        onDeviceFound = JavaMethod("(Landroid/content/IntentSender;)V")
        onAssociationCreated = JavaMethod("(Landroid/companion/AssociationInfo;)V")
        onAssociationPending = JavaMethod("(Landroid/content/IntentSender;)V")