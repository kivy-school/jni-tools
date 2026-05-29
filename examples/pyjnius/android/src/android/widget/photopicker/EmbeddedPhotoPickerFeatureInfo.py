from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EmbeddedPhotoPickerFeatureInfo"]

class EmbeddedPhotoPickerFeatureInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/photopicker/EmbeddedPhotoPickerFeatureInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getPreSelectedUris = JavaMethod("()Ljava/util/List;")
    getAccentColor = JavaMethod("()J")
    getMimeTypes = JavaMethod("()Ljava/util/List;")
    getThemeNightMode = JavaMethod("()I")
    isOrderedSelection = JavaMethod("()Z")
    getMaxSelectionLimit = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/photopicker/EmbeddedPhotoPickerFeatureInfo$Builder"
        __javaconstructor__ = [("()V", False)]
        setAccentColor = JavaMethod("(J)Landroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo$Builder;")
        setMaxSelectionLimit = JavaMethod("(I)Landroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo$Builder;")
        setMimeTypes = JavaMethod("(Ljava/util/List;)Landroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo$Builder;")
        setOrderedSelection = JavaMethod("(Z)Landroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo$Builder;")
        setPreSelectedUris = JavaMethod("(Ljava/util/List;)Landroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo$Builder;")
        setThemeNightMode = JavaMethod("(I)Landroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo$Builder;")
        build = JavaMethod("()Landroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo;")