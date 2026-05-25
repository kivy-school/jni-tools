from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VpnProfileState"]

class VpnProfileState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/VpnProfileState"
    __javaconstructor__ = [("(ILjava/lang/String;ZZ)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STATE_CONNECTED = JavaStaticField("I")
    STATE_CONNECTING = JavaStaticField("I")
    STATE_DISCONNECTED = JavaStaticField("I")
    STATE_FAILED = JavaStaticField("I")
    getState = JavaMethod("()I")
    getSessionId = JavaMethod("()Ljava/lang/String;")
    isAlwaysOn = JavaMethod("()Z")
    isLockdownEnabled = JavaMethod("()Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")