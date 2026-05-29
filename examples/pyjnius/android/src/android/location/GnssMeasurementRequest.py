from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GnssMeasurementRequest"]

class GnssMeasurementRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/GnssMeasurementRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PASSIVE_INTERVAL = JavaStaticField("I")
    isFullTracking = JavaMethod("()Z")
    getIntervalMillis = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssMeasurementRequest/Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/location/GnssMeasurementRequest;)V", False)]
        setFullTracking = JavaMethod("(Z)Landroid/location/GnssMeasurementRequest$Builder;")
        setIntervalMillis = JavaMethod("(I)Landroid/location/GnssMeasurementRequest$Builder;")
        build = JavaMethod("()Landroid/location/GnssMeasurementRequest;")