from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallAudioState"]

class CallAudioState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/CallAudioState"
    __javaconstructor__ = [("(ZII)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    ROUTE_BLUETOOTH = JavaStaticField("I")
    ROUTE_EARPIECE = JavaStaticField("I")
    ROUTE_SPEAKER = JavaStaticField("I")
    ROUTE_STREAMING = JavaStaticField("I")
    ROUTE_WIRED_HEADSET = JavaStaticField("I")
    ROUTE_WIRED_OR_EARPIECE = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getRoute = JavaMethod("()I")
    audioRouteToString = JavaStaticMethod("(I)Ljava/lang/String;")
    getActiveBluetoothDevice = JavaMethod("()Landroid/bluetooth/BluetoothDevice;")
    getSupportedBluetoothDevices = JavaMethod("()Ljava/util/Collection;")
    getSupportedRouteMask = JavaMethod("()I")
    isMuted = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")