from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PhysicalChannelConfig"]

class PhysicalChannelConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/PhysicalChannelConfig"
    BAND_UNKNOWN = JavaStaticField("I")
    CELL_BANDWIDTH_UNKNOWN = JavaStaticField("I")
    CHANNEL_NUMBER_UNKNOWN = JavaStaticField("I")
    CONNECTION_PRIMARY_SERVING = JavaStaticField("I")
    CONNECTION_SECONDARY_SERVING = JavaStaticField("I")
    CONNECTION_UNKNOWN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FREQUENCY_UNKNOWN = JavaStaticField("I")
    PHYSICAL_CELL_ID_MAXIMUM_VALUE = JavaStaticField("I")
    PHYSICAL_CELL_ID_UNKNOWN = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getNetworkType = JavaMethod("()I")
    getBand = JavaMethod("()I")
    getCellBandwidthDownlinkKhz = JavaMethod("()I")
    getCellBandwidthUplinkKhz = JavaMethod("()I")
    getConnectionStatus = JavaMethod("()I")
    getDownlinkChannelNumber = JavaMethod("()I")
    getDownlinkFrequencyKhz = JavaMethod("()I")
    getPhysicalCellId = JavaMethod("()I")
    getUplinkChannelNumber = JavaMethod("()I")
    getUplinkFrequencyKhz = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")