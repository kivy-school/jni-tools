from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DevicePresenceEvent"]

class DevicePresenceEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/DevicePresenceEvent"
    __javaconstructor__ = [("(IILandroid/os/ParcelUuid;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EVENT_BLE_APPEARED = JavaStaticField("I")
    EVENT_BLE_DISAPPEARED = JavaStaticField("I")
    EVENT_BT_CONNECTED = JavaStaticField("I")
    EVENT_BT_DISCONNECTED = JavaStaticField("I")
    EVENT_SELF_MANAGED_APPEARED = JavaStaticField("I")
    EVENT_SELF_MANAGED_DISAPPEARED = JavaStaticField("I")
    NO_ASSOCIATION = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getEvent = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getUuid = JavaMethod("()Landroid/os/ParcelUuid;")
    getAssociationId = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")