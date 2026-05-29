from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PendingJobReasonsInfo"]

class PendingJobReasonsInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/job/PendingJobReasonsInfo"
    __javaconstructor__ = [("(J[I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPendingJobReasons = JavaMethod("()[I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getTimestampMillis = JavaMethod("()J")