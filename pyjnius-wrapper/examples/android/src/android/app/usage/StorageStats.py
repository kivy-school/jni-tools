from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StorageStats"]

class StorageStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/StorageStats"
    APP_DATA_TYPE_FILE_TYPE_APK = JavaStaticField("I")
    APP_DATA_TYPE_FILE_TYPE_CURRENT_PROFILE = JavaStaticField("I")
    APP_DATA_TYPE_FILE_TYPE_DEXOPT_ARTIFACT = JavaStaticField("I")
    APP_DATA_TYPE_FILE_TYPE_DM = JavaStaticField("I")
    APP_DATA_TYPE_FILE_TYPE_REFERENCE_PROFILE = JavaStaticField("I")
    APP_DATA_TYPE_LIB = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getAppBytes = JavaMethod("()J")
    getAppBytesByDataType = JavaMethod("(I)J")
    getDataBytes = JavaMethod("()J")
    getCacheBytes = JavaMethod("()J")
    getExternalCacheBytes = JavaMethod("()J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")