from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProfilingResult"]

class ProfilingResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/ProfilingResult"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    ERROR_FAILED_EXECUTING = JavaStaticField("I")
    ERROR_FAILED_INVALID_REQUEST = JavaStaticField("I")
    ERROR_FAILED_NO_DISK_SPACE = JavaStaticField("I")
    ERROR_FAILED_POST_PROCESSING = JavaStaticField("I")
    ERROR_FAILED_PROFILING_IN_PROGRESS = JavaStaticField("I")
    ERROR_FAILED_RATE_LIMIT_PROCESS = JavaStaticField("I")
    ERROR_FAILED_RATE_LIMIT_SYSTEM = JavaStaticField("I")
    ERROR_NONE = JavaStaticField("I")
    ERROR_UNKNOWN = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getErrorMessage = JavaMethod("()Ljava/lang/String;")
    getResultFilePath = JavaMethod("()Ljava/lang/String;")
    getTriggerType = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getTag = JavaMethod("()Ljava/lang/String;")
    getErrorCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")