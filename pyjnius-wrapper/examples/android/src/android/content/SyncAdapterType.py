from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncAdapterType"]

class SyncAdapterType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/SyncAdapterType"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;ZZ)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    accountType = JavaField("Ljava/lang/String;")
    authority = JavaField("Ljava/lang/String;")
    isKey = JavaField("Z")
    supportsUploading = JavaMethod("()Z")
    isUserVisible = JavaMethod("()Z")
    allowParallelSyncs = JavaMethod("()Z")
    isAlwaysSyncable = JavaMethod("()Z")
    getSettingsActivity = JavaMethod("()Ljava/lang/String;")
    newKey = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/content/SyncAdapterType;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")