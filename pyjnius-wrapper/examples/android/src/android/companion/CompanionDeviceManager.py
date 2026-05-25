from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    RESULT_USER_REJECTED = JavaStaticField("I")
    associate = JavaMultipleMethod([("(Landroid/companion/AssociationRequest;Landroid/companion/CompanionDeviceManager$Callback;Landroid/os/Handler;)V", False, False), ("(Landroid/companion/AssociationRequest;Ljava/util/concurrent/Executor;Landroid/companion/CompanionDeviceManager$Callback;)V", False, False)])
    buildAssociationCancellationIntent = JavaMethod("()Landroid/content/IntentSender;")
    enableSystemDataSyncForTypes = JavaMethod("(II)V")
    disableSystemDataSyncForTypes = JavaMethod("(II)V")
    getAssociations = JavaMethod("()Ljava/util/List;")
    getMyAssociations = JavaMethod("()Ljava/util/List;")
    disassociate = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(I)V", False, False)])
    requestNotificationAccess = JavaMethod("(Landroid/content/ComponentName;)V")
    hasNotificationAccess = JavaMethod("(Landroid/content/ComponentName;)Z")
    startObservingDevicePresence = JavaMethod("(Ljava/lang/String;)V")
    stopObservingDevicePresence = JavaMethod("(Ljava/lang/String;)V")
    attachSystemDataTransport = JavaMethod("(ILjava/io/InputStream;Ljava/io/OutputStream;)V")
    detachSystemDataTransport = JavaMethod("(I)V")
    buildPermissionTransferUserConsentIntent = JavaMethod("(I)Landroid/content/IntentSender;")
    isPermissionTransferUserConsented = JavaMethod("(I)Z")
    startSystemDataTransfer = JavaMethod("(ILjava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/companion/CompanionDeviceManager/Callback"
        __javaconstructor__ = [("()V", False)]
        onDeviceFound = JavaMethod("(Landroid/content/IntentSender;)V")
        onAssociationPending = JavaMethod("(Landroid/content/IntentSender;)V")
        onAssociationCreated = JavaMethod("(Landroid/companion/AssociationInfo;)V")
        onFailure = JavaMethod("(Ljava/lang/CharSequence;)V")