from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncAdapterType"]

class SyncAdapterType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/SyncAdapterType"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False), ("(Ljava/lang/String;Ljava/lang/String;ZZ)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    accountType = JavaField("Ljava/lang/String;")
    authority = JavaField("Ljava/lang/String;")
    isKey = JavaField("Z")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    allowParallelSyncs = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    supportsUploading = JavaMethod("()Z")
    isAlwaysSyncable = JavaMethod("()Z")
    getSettingsActivity = JavaMethod("()Ljava/lang/String;")
    isUserVisible = JavaMethod("()Z")
    newKey = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/content/SyncAdapterType;")