from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PeriodicAdvertisingParameters"]

class PeriodicAdvertisingParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/PeriodicAdvertisingParameters"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getInterval = JavaMethod("()I")
    getIncludeTxPower = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/bluetooth/le/PeriodicAdvertisingParameters$Builder"
        __javaconstructor__ = [("()V", False)]
        setInterval = JavaMethod("(I)Landroid/bluetooth/le/PeriodicAdvertisingParameters$Builder;")
        setIncludeTxPower = JavaMethod("(Z)Landroid/bluetooth/le/PeriodicAdvertisingParameters$Builder;")
        build = JavaMethod("()Landroid/bluetooth/le/PeriodicAdvertisingParameters;")