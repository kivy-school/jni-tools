from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SystemUpdatePolicy"]

class SystemUpdatePolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/SystemUpdatePolicy"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_INSTALL_AUTOMATIC = JavaStaticField("I")
    TYPE_INSTALL_WINDOWED = JavaStaticField("I")
    TYPE_POSTPONE = JavaStaticField("I")
    createAutomaticInstallPolicy = JavaStaticMethod("()Landroid/app/admin/SystemUpdatePolicy;")
    createWindowedInstallPolicy = JavaStaticMethod("(II)Landroid/app/admin/SystemUpdatePolicy;")
    createPostponeInstallPolicy = JavaStaticMethod("()Landroid/app/admin/SystemUpdatePolicy;")
    getPolicyType = JavaMethod("()I")
    getInstallWindowStart = JavaMethod("()I")
    getInstallWindowEnd = JavaMethod("()I")
    setFreezePeriods = JavaMethod("(Ljava/util/List;)Landroid/app/admin/SystemUpdatePolicy;")
    getFreezePeriods = JavaMethod("()Ljava/util/List;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class ValidationFailedException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/admin/SystemUpdatePolicy/ValidationFailedException"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        ERROR_COMBINED_FREEZE_PERIOD_TOO_CLOSE = JavaStaticField("I")
        ERROR_COMBINED_FREEZE_PERIOD_TOO_LONG = JavaStaticField("I")
        ERROR_DUPLICATE_OR_OVERLAP = JavaStaticField("I")
        ERROR_NEW_FREEZE_PERIOD_TOO_CLOSE = JavaStaticField("I")
        ERROR_NEW_FREEZE_PERIOD_TOO_LONG = JavaStaticField("I")
        ERROR_UNKNOWN = JavaStaticField("I")
        getErrorCode = JavaMethod("()I")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")