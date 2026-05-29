from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VpnProfileState"]

class VpnProfileState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/VpnProfileState"
    __javaconstructor__ = [("(ILjava/lang/String;ZZ)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STATE_CONNECTED = JavaStaticField("I")
    STATE_CONNECTING = JavaStaticField("I")
    STATE_DISCONNECTED = JavaStaticField("I")
    STATE_FAILED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isAlwaysOn = JavaMethod("()Z")
    isLockdownEnabled = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getState = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSessionId = JavaMethod("()Ljava/lang/String;")