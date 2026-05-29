from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GnssMeasurementRequest"]

class GnssMeasurementRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/GnssMeasurementRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PASSIVE_INTERVAL = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getIntervalMillis = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    isFullTracking = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssMeasurementRequest$Builder"
        __javaconstructor__ = [("(Landroid/location/GnssMeasurementRequest;)V", False), ("()V", False)]
        setFullTracking = JavaMethod("(Z)Landroid/location/GnssMeasurementRequest$Builder;")
        setIntervalMillis = JavaMethod("(I)Landroid/location/GnssMeasurementRequest$Builder;")
        build = JavaMethod("()Landroid/location/GnssMeasurementRequest;")