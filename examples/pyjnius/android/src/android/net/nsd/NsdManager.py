from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    discoverServices = JavaMultipleMethod([("(Ljava/lang/String;ILandroid/net/nsd/NsdManager$DiscoveryListener;)V", False, False), ("(Ljava/lang/String;ILandroid/net/Network;Ljava/util/concurrent/Executor;Landroid/net/nsd/NsdManager$DiscoveryListener;)V", False, False), ("(Landroid/net/nsd/DiscoveryRequest;Ljava/util/concurrent/Executor;Landroid/net/nsd/NsdManager$DiscoveryListener;)V", False, False), ("(Ljava/lang/String;ILandroid/net/NetworkRequest;Ljava/util/concurrent/Executor;Landroid/net/nsd/NsdManager$DiscoveryListener;)V", False, False)])
    unregisterService = JavaMethod("(Landroid/net/nsd/NsdManager$RegistrationListener;)V")
    registerService = JavaMultipleMethod([("(Landroid/net/nsd/NsdServiceInfo;ILjava/util/concurrent/Executor;Landroid/net/nsd/NsdManager$RegistrationListener;)V", False, False), ("(Landroid/net/nsd/NsdServiceInfo;ILandroid/net/nsd/NsdManager$RegistrationListener;)V", False, False)])
    registerServiceInfoCallback = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;Ljava/util/concurrent/Executor;Landroid/net/nsd/NsdManager$ServiceInfoCallback;)V")
    stopServiceDiscovery = JavaMethod("(Landroid/net/nsd/NsdManager$DiscoveryListener;)V")
    stopServiceResolution = JavaMethod("(Landroid/net/nsd/NsdManager$ResolveListener;)V")
    unregisterServiceInfoCallback = JavaMethod("(Landroid/net/nsd/NsdManager$ServiceInfoCallback;)V")
    resolveService = JavaMultipleMethod([("(Landroid/net/nsd/NsdServiceInfo;Landroid/net/nsd/NsdManager$ResolveListener;)V", False, False), ("(Landroid/net/nsd/NsdServiceInfo;Ljava/util/concurrent/Executor;Landroid/net/nsd/NsdManager$ResolveListener;)V", False, False)])

    class ServiceInfoCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/nsd/NsdManager$ServiceInfoCallback"
        onServiceLost = JavaMethod("()V")
        onServiceUpdated = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;)V")
        onServiceInfoCallbackRegistrationFailed = JavaMethod("(I)V")
        onServiceInfoCallbackUnregistered = JavaMethod("()V")

    class ResolveListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/nsd/NsdManager$ResolveListener"
        onResolutionStopped = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;)V")
        onResolveFailed = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;I)V")
        onServiceResolved = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;)V")
        onStopResolutionFailed = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;I)V")

    class RegistrationListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/nsd/NsdManager$RegistrationListener"
        onRegistrationFailed = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;I)V")
        onServiceRegistered = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;)V")
        onServiceUnregistered = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;)V")
        onUnregistrationFailed = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;I)V")

    class DiscoveryListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/nsd/NsdManager$DiscoveryListener"
        onServiceLost = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;)V")
        onDiscoveryStopped = JavaMethod("(Ljava/lang/String;)V")
        onServiceFound = JavaMethod("(Landroid/net/nsd/NsdServiceInfo;)V")
        onStartDiscoveryFailed = JavaMethod("(Ljava/lang/String;I)V")
        onStopDiscoveryFailed = JavaMethod("(Ljava/lang/String;I)V")
        onDiscoveryStarted = JavaMethod("(Ljava/lang/String;)V")