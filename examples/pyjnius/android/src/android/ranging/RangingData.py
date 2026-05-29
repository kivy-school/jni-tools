from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RangingData"]

class RangingData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/RangingData"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getElevation = JavaMethod("()Landroid/ranging/RangingMeasurement;")
    getAzimuth = JavaMethod("()Landroid/ranging/RangingMeasurement;")
    getRssi = JavaMethod("()I")
    hasRssi = JavaMethod("()Z")
    getRangingTechnology = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getTimestampMillis = JavaMethod("()J")
    getDistance = JavaMethod("()Landroid/ranging/RangingMeasurement;")