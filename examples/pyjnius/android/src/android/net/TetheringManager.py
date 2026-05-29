from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TetheringManager"]

class TetheringManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/TetheringManager"
    CONNECTIVITY_SCOPE_GLOBAL = JavaStaticField("I")
    TETHERING_WIFI = JavaStaticField("I")
    TETHER_ERROR_DHCPSERVER_ERROR = JavaStaticField("I")
    TETHER_ERROR_DISABLE_FORWARDING_ERROR = JavaStaticField("I")
    TETHER_ERROR_DUPLICATE_REQUEST = JavaStaticField("I")
    TETHER_ERROR_ENABLE_FORWARDING_ERROR = JavaStaticField("I")
    TETHER_ERROR_ENTITLEMENT_UNKNOWN = JavaStaticField("I")
    TETHER_ERROR_IFACE_CFG_ERROR = JavaStaticField("I")
    TETHER_ERROR_INTERNAL_ERROR = JavaStaticField("I")
    TETHER_ERROR_NO_ACCESS_TETHERING_PERMISSION = JavaStaticField("I")
    TETHER_ERROR_NO_CHANGE_TETHERING_PERMISSION = JavaStaticField("I")
    TETHER_ERROR_NO_ERROR = JavaStaticField("I")
    TETHER_ERROR_PROVISIONING_FAILED = JavaStaticField("I")
    TETHER_ERROR_SERVICE_UNAVAIL = JavaStaticField("I")
    TETHER_ERROR_TETHER_IFACE_ERROR = JavaStaticField("I")
    TETHER_ERROR_UNAVAIL_IFACE = JavaStaticField("I")
    TETHER_ERROR_UNKNOWN_IFACE = JavaStaticField("I")
    TETHER_ERROR_UNKNOWN_REQUEST = JavaStaticField("I")
    TETHER_ERROR_UNKNOWN_TYPE = JavaStaticField("I")
    TETHER_ERROR_UNSUPPORTED = JavaStaticField("I")
    TETHER_ERROR_UNTETHER_IFACE_ERROR = JavaStaticField("I")
    startTethering = JavaMethod("(Landroid/net/TetheringManager$TetheringRequest;Ljava/util/concurrent/Executor;Landroid/net/TetheringManager$StartTetheringCallback;)V")
    stopTethering = JavaMethod("(Landroid/net/TetheringManager$TetheringRequest;Ljava/util/concurrent/Executor;Landroid/net/TetheringManager$StopTetheringCallback;)V")
    registerTetheringEventCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/net/TetheringManager$TetheringEventCallback;)V")
    unregisterTetheringEventCallback = JavaMethod("(Landroid/net/TetheringManager$TetheringEventCallback;)V")

    class TetheringRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/TetheringManager$TetheringRequest"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        getSoftApConfiguration = JavaMethod("()Landroid/net/wifi/SoftApConfiguration;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/net/TetheringManager$TetheringRequest$Builder"
            __javaconstructor__ = [("(I)V", False)]
            setSoftApConfiguration = JavaMethod("(Landroid/net/wifi/SoftApConfiguration;)Landroid/net/TetheringManager$TetheringRequest$Builder;")
            build = JavaMethod("()Landroid/net/TetheringManager$TetheringRequest;")

    class TetheringEventCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/TetheringManager$TetheringEventCallback"
        onTetheredInterfacesChanged = JavaMethod("(Ljava/util/Set;)V")

    class StopTetheringCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/TetheringManager$StopTetheringCallback"
        onStopTetheringFailed = JavaMethod("(I)V")
        onStopTetheringSucceeded = JavaMethod("()V")

    class StartTetheringCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/TetheringManager$StartTetheringCallback"
        onTetheringFailed = JavaMethod("(I)V")
        onTetheringStarted = JavaMethod("()V")