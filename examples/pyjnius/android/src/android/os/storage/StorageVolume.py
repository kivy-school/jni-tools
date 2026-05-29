from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StorageVolume"]

class StorageVolume(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/storage/StorageVolume"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTRA_STORAGE_VOLUME = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isPrimary = JavaMethod("()Z")
    isRemovable = JavaMethod("()Z")
    getDirectory = JavaMethod("()Ljava/io/File;")
    createAccessIntent = JavaMethod("(Ljava/lang/String;)Landroid/content/Intent;")
    isEmulated = JavaMethod("()Z")
    getStorageUuid = JavaMethod("()Ljava/util/UUID;")
    createOpenDocumentTreeIntent = JavaMethod("()Landroid/content/Intent;")
    getMediaStoreVolumeName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getState = JavaMethod("()Ljava/lang/String;")
    getUuid = JavaMethod("()Ljava/lang/String;")
    getDescription = JavaMethod("(Landroid/content/Context;)Ljava/lang/String;")
    getOwner = JavaMethod("()Landroid/os/UserHandle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")