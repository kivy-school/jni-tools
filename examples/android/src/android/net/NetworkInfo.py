from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkInfo"]

class NetworkInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/NetworkInfo"
    __javaconstructor__ = [("(IILjava/lang/String;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getType = JavaMethod("()I")
    getSubtype = JavaMethod("()I")
    getTypeName = JavaMethod("()Ljava/lang/String;")
    getSubtypeName = JavaMethod("()Ljava/lang/String;")
    isConnectedOrConnecting = JavaMethod("()Z")
    isConnected = JavaMethod("()Z")
    isAvailable = JavaMethod("()Z")
    isFailover = JavaMethod("()Z")
    isRoaming = JavaMethod("()Z")
    getState = JavaMethod("()Landroid/net/NetworkInfo$State;")
    getDetailedState = JavaMethod("()Landroid/net/NetworkInfo$DetailedState;")
    setDetailedState = JavaMethod("(Landroid/net/NetworkInfo$DetailedState;Ljava/lang/String;Ljava/lang/String;)V")
    getReason = JavaMethod("()Ljava/lang/String;")
    getExtraInfo = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class DetailedState(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/NetworkInfo/DetailedState"
        values = JavaStaticMethod("()[Landroid/net/NetworkInfo$DetailedState;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/net/NetworkInfo$DetailedState;")
        IDLE = JavaStaticField("Landroid/net/NetworkInfo/DetailedState;")
        SCANNING = JavaStaticField("Landroid/net/NetworkInfo/DetailedState;")
        CONNECTING = JavaStaticField("Landroid/net/NetworkInfo/DetailedState;")
        AUTHENTICATING = JavaStaticField("Landroid/net/NetworkInfo/DetailedState;")
        OBTAINING_IPADDR = JavaStaticField("Landroid/net/NetworkInfo/DetailedState;")
        CONNECTED = JavaStaticField("Landroid/net/NetworkInfo/DetailedState;")
        SUSPENDED = JavaStaticField("Landroid/net/NetworkInfo/DetailedState;")
        DISCONNECTING = JavaStaticField("Landroid/net/NetworkInfo/DetailedState;")
        DISCONNECTED = JavaStaticField("Landroid/net/NetworkInfo/DetailedState;")
        FAILED = JavaStaticField("Landroid/net/NetworkInfo/DetailedState;")
        BLOCKED = JavaStaticField("Landroid/net/NetworkInfo/DetailedState;")
        VERIFYING_POOR_LINK = JavaStaticField("Landroid/net/NetworkInfo/DetailedState;")
        CAPTIVE_PORTAL_CHECK = JavaStaticField("Landroid/net/NetworkInfo/DetailedState;")

    class State(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/NetworkInfo/State"
        values = JavaStaticMethod("()[Landroid/net/NetworkInfo$State;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/net/NetworkInfo$State;")
        CONNECTING = JavaStaticField("Landroid/net/NetworkInfo/State;")
        CONNECTED = JavaStaticField("Landroid/net/NetworkInfo/State;")
        SUSPENDED = JavaStaticField("Landroid/net/NetworkInfo/State;")
        DISCONNECTING = JavaStaticField("Landroid/net/NetworkInfo/State;")
        DISCONNECTED = JavaStaticField("Landroid/net/NetworkInfo/State;")
        UNKNOWN = JavaStaticField("Landroid/net/NetworkInfo/State;")