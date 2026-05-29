from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RangingMeasurement"]

class RangingMeasurement(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/RangingMeasurement"
    CONFIDENCE_HIGH = JavaStaticField("I")
    CONFIDENCE_LOW = JavaStaticField("I")
    CONFIDENCE_MEDIUM = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getConfidence = JavaMethod("()I")
    getMeasurement = JavaMethod("()D")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")