from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StorageVolume"]

class StorageVolume(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/storage/StorageVolume"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTRA_STORAGE_VOLUME = JavaStaticField("Ljava/lang/String;")
    getDirectory = JavaMethod("()Ljava/io/File;")
    getDescription = JavaMethod("(Landroid/content/Context;)Ljava/lang/String;")
    isPrimary = JavaMethod("()Z")
    isRemovable = JavaMethod("()Z")
    isEmulated = JavaMethod("()Z")
    getOwner = JavaMethod("()Landroid/os/UserHandle;")
    getStorageUuid = JavaMethod("()Ljava/util/UUID;")
    getUuid = JavaMethod("()Ljava/lang/String;")
    getMediaStoreVolumeName = JavaMethod("()Ljava/lang/String;")
    getState = JavaMethod("()Ljava/lang/String;")
    createAccessIntent = JavaMethod("(Ljava/lang/String;)Landroid/content/Intent;")
    createOpenDocumentTreeIntent = JavaMethod("()Landroid/content/Intent;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")