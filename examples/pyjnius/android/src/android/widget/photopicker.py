from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class EmbeddedPhotoPickerSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/photopicker/EmbeddedPhotoPickerSession"
    close = JavaMethod("()V")
    notifyResized = JavaMethod("(II)V")
    getSurfacePackage = JavaMethod("()Landroid/view/SurfaceControlViewHost$SurfacePackage;")
    notifyConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
    notifyPhotoPickerExpanded = JavaMethod("(Z)V")
    notifyVisibilityChanged = JavaMethod("(Z)V")
    requestRevokeUriPermission = JavaMethod("(Ljava/util/List;)V")

class EmbeddedPhotoPickerClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/photopicker/EmbeddedPhotoPickerClient"
    onSelectionComplete = JavaMethod("()V")
    onUriPermissionGranted = JavaMethod("(Ljava/util/List;)V")
    onUriPermissionRevoked = JavaMethod("(Ljava/util/List;)V")
    onSessionError = JavaMethod("(Ljava/lang/Throwable;)V")
    onSessionOpened = JavaMethod("(Landroid/widget/photopicker/EmbeddedPhotoPickerSession;)V")

class EmbeddedPhotoPickerProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/photopicker/EmbeddedPhotoPickerProvider"
    openSession = JavaMethod("(Landroid/os/IBinder;IIILandroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo;Ljava/util/concurrent/Executor;Landroid/widget/photopicker/EmbeddedPhotoPickerClient;)V")

class EmbeddedPhotoPickerProviderFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/photopicker/EmbeddedPhotoPickerProviderFactory"
    create = JavaStaticMethod("(Landroid/content/Context;)Landroid/widget/photopicker/EmbeddedPhotoPickerProvider;")

class EmbeddedPhotoPickerFeatureInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/photopicker/EmbeddedPhotoPickerFeatureInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getAccentColor = JavaMethod("()J")
    getMaxSelectionLimit = JavaMethod("()I")
    getMimeTypes = JavaMethod("()Ljava/util/List;")
    getPreSelectedUris = JavaMethod("()Ljava/util/List;")
    getThemeNightMode = JavaMethod("()I")
    isOrderedSelection = JavaMethod("()Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/photopicker/EmbeddedPhotoPickerFeatureInfo$Builder"
        __javaconstructor__ = [("()V", False)]
        setMaxSelectionLimit = JavaMethod("(I)Landroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo$Builder;")
        setMimeTypes = JavaMethod("(Ljava/util/List;)Landroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo$Builder;")
        setAccentColor = JavaMethod("(J)Landroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo$Builder;")
        setOrderedSelection = JavaMethod("(Z)Landroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo$Builder;")
        setPreSelectedUris = JavaMethod("(Ljava/util/List;)Landroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo$Builder;")
        setThemeNightMode = JavaMethod("(I)Landroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo$Builder;")
        build = JavaMethod("()Landroid/widget/photopicker/EmbeddedPhotoPickerFeatureInfo;")