from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SensorFusionParams"]

class SensorFusionParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/SensorFusionParams"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    isSensorFusionEnabled = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/SensorFusionParams$Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/ranging/SensorFusionParams;")
        setSensorFusionEnabled = JavaMethod("(Z)Landroid/ranging/SensorFusionParams$Builder;")