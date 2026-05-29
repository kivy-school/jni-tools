from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    isMuted = JavaMethod("()Z")
    getRoute = JavaMethod("()I")
    getSupportedRouteMask = JavaMethod("()I")
    getActiveBluetoothDevice = JavaMethod("()Landroid/bluetooth/BluetoothDevice;")
    getSupportedBluetoothDevices = JavaMethod("()Ljava/util/Collection;")
    audioRouteToString = JavaStaticMethod("(I)Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")