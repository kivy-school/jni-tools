from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NsdManager"]

class NsdManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/nsd/NsdManager"
    ACTION_NSD_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    EXTRA_NSD_STATE = JavaStaticField("Ljava/lang/String;")
    FAILURE_ALREADY_ACTIVE = JavaStaticField("I")
    FAILURE_BAD_PARAMETERS = JavaStaticField("I")
    FAILURE_INTERNAL_ERROR = JavaStaticField("I")
    FAILURE_MAX_LIMIT = JavaStaticField("I")
    FAILURE_OPERATION_NOT_RUNNING = JavaStaticField("I")
    NSD_STATE_DISABLED = JavaStaticField("I")
    NSD_STATE_ENABLED = JavaStaticField("I")
    PROTOCOL_DNS_SD = JavaStaticField("I")
    registerService = JavaMultipleMethod([("(Landroid/net/nsd/NsdServiceInfo;ILandroid/net/nsd/NsdManager$RegistrationListener;)V", False, False), ("(Landroid/net/nsd/NsdServiceInfo;ILjava/util/concurrent/Executor;Landroid/net/nsd/NsdManager$RegistrationListener;)V", False, False)])
    unregisterService = JavaMethod("(Landroid/net/nsd/NsdManager$RegistrationListener;)V")
    discoverServices = JavaMultipleMethod([("(Ljava/lang/String;ILandroid/net/nsd/NsdManager$DiscoveryListener;)V", False, False), ("(Ljava/lang/String;ILandroid/net/Network;Ljava/util/concurrent/Executor;Landroid/net/nsd/NsdManager$DiscoveryListener;)V", False, False), ("(Landroid/net/nsd/DiscoveryRequest;Ljava/util/concurrent/Executor;Landroid/net/nsd/NsdManager$DiscoveryListener;)V", False, False), ("(Ljava/lang/String;ILandroid/net/NetworkRequest;Ljava/util/concurrent/Executor;Landroid/net/nsd/NsdManager$DiscoveryListener;)V", False, False)])
    stopServiceDiscovery = JavaMethod("(Landroid/net/nsd/NsdManager$DiscoveryListener;)V")
    resolveService = JavaMultipleMethod([("(Landroid/net/nsd/NsdServiceInfo;Landroid/net/nsd/NsdManager$ResolveListener;)V", False, False), ("(Landroid/net/nsd/NsdServiceInfo;Ljava/util/concurrent/Executor;Landroid/net/nsd/NsdManager$ResolveListener;)V", False, False)])
    stopServiceResolution = JavaMethod("(Landroid/net/nsd/NsdManager$ResolveListener;)V")
    registerServiceInfoCallback = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;Ljava/util/concurrent/Executor;Landroid/net/nsd/NsdManager$ServiceInfoCallback;)V")
    unregisterServiceInfoCallback = JavaMethod("(Landroid/net/nsd/NsdManager$ServiceInfoCallback;)V")

    class DiscoveryListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/nsd/NsdManager/DiscoveryListener"
        onStartDiscoveryFailed = JavaMethod("(Ljava/lang/String;I)V")
        onStopDiscoveryFailed = JavaMethod("(Ljava/lang/String;I)V")
        onDiscoveryStarted = JavaMethod("(Ljava/lang/String;)V")
        onDiscoveryStopped = JavaMethod("(Ljava/lang/String;)V")
        onServiceFound = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;)V")
        onServiceLost = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;)V")

    class RegistrationListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/nsd/NsdManager/RegistrationListener"
        onRegistrationFailed = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;I)V")
        onUnregistrationFailed = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;I)V")
        onServiceRegistered = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;)V")
        onServiceUnregistered = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;)V")

    class ResolveListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/nsd/NsdManager/ResolveListener"
        onResolveFailed = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;I)V")
        onServiceResolved = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;)V")
        onResolutionStopped = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;)V")
        onStopResolutionFailed = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;I)V")

    class ServiceInfoCallback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/nsd/NsdManager/ServiceInfoCallback"
        onServiceInfoCallbackRegistrationFailed = JavaMethod("(I)V")
        onServiceUpdated = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;)V")
        onServiceLost = JavaMethod("()V")
        onServiceInfoCallbackUnregistered = JavaMethod("()V")