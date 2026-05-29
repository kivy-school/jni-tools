from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConnectivityDiagnosticsManager"]

class ConnectivityDiagnosticsManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ConnectivityDiagnosticsManager"
    registerConnectivityDiagnosticsCallback = JavaMethod("(Landroid/net/NetworkRequest;Ljava/util/concurrent/Executor;Landroid/net/ConnectivityDiagnosticsManager$ConnectivityDiagnosticsCallback;)V")
    unregisterConnectivityDiagnosticsCallback = JavaMethod("(Landroid/net/ConnectivityDiagnosticsManager$ConnectivityDiagnosticsCallback;)V")

    class DataStallReport(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ConnectivityDiagnosticsManager$DataStallReport"
        __javaconstructor__ = [("(Landroid/net/Network;JILandroid/net/LinkProperties;Landroid/net/NetworkCapabilities;Landroid/os/PersistableBundle;)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        DETECTION_METHOD_DNS_EVENTS = JavaStaticField("I")
        DETECTION_METHOD_TCP_METRICS = JavaStaticField("I")
        KEY_DNS_CONSECUTIVE_TIMEOUTS = JavaStaticField("Ljava/lang/String;")
        KEY_TCP_METRICS_COLLECTION_PERIOD_MILLIS = JavaStaticField("Ljava/lang/String;")
        KEY_TCP_PACKET_FAIL_RATE = JavaStaticField("Ljava/lang/String;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getNetworkCapabilities = JavaMethod("()Landroid/net/NetworkCapabilities;")
        getNetwork = JavaMethod("()Landroid/net/Network;")
        getLinkProperties = JavaMethod("()Landroid/net/LinkProperties;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getStallDetails = JavaMethod("()Landroid/os/PersistableBundle;")
        getReportTimestamp = JavaMethod("()J")
        getDetectionMethod = JavaMethod("()I")

    class ConnectivityReport(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ConnectivityDiagnosticsManager$ConnectivityReport"
        __javaconstructor__ = [("(Landroid/net/Network;JLandroid/net/LinkProperties;Landroid/net/NetworkCapabilities;Landroid/os/PersistableBundle;)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        KEY_NETWORK_PROBES_ATTEMPTED_BITMASK = JavaStaticField("Ljava/lang/String;")
        KEY_NETWORK_PROBES_SUCCEEDED_BITMASK = JavaStaticField("Ljava/lang/String;")
        KEY_NETWORK_VALIDATION_RESULT = JavaStaticField("Ljava/lang/String;")
        NETWORK_PROBE_DNS = JavaStaticField("I")
        NETWORK_PROBE_FALLBACK = JavaStaticField("I")
        NETWORK_PROBE_HTTP = JavaStaticField("I")
        NETWORK_PROBE_HTTPS = JavaStaticField("I")
        NETWORK_PROBE_PRIVATE_DNS = JavaStaticField("I")
        NETWORK_VALIDATION_RESULT_INVALID = JavaStaticField("I")
        NETWORK_VALIDATION_RESULT_PARTIALLY_VALID = JavaStaticField("I")
        NETWORK_VALIDATION_RESULT_SKIPPED = JavaStaticField("I")
        NETWORK_VALIDATION_RESULT_VALID = JavaStaticField("I")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getNetworkCapabilities = JavaMethod("()Landroid/net/NetworkCapabilities;")
        getNetwork = JavaMethod("()Landroid/net/Network;")
        getLinkProperties = JavaMethod("()Landroid/net/LinkProperties;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getReportTimestamp = JavaMethod("()J")
        getAdditionalInfo = JavaMethod("()Landroid/os/PersistableBundle;")

    class ConnectivityDiagnosticsCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ConnectivityDiagnosticsManager$ConnectivityDiagnosticsCallback"
        __javaconstructor__ = [("()V", False)]
        onConnectivityReportAvailable = JavaMethod("(Landroid/net/ConnectivityDiagnosticsManager$ConnectivityReport;)V")
        onDataStallSuspected = JavaMethod("(Landroid/net/ConnectivityDiagnosticsManager$DataStallReport;)V")
        onNetworkConnectivityReported = JavaMethod("(Landroid/net/Network;Z)V")