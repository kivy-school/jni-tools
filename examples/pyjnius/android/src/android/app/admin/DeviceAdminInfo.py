from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeviceAdminInfo"]

class DeviceAdminInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/DeviceAdminInfo"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/content/pm/ResolveInfo;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    HEADLESS_DEVICE_OWNER_MODE_AFFILIATED = JavaStaticField("I")
    HEADLESS_DEVICE_OWNER_MODE_SINGLE_USER = JavaStaticField("I")
    HEADLESS_DEVICE_OWNER_MODE_UNSUPPORTED = JavaStaticField("I")
    USES_ENCRYPTED_STORAGE = JavaStaticField("I")
    USES_POLICY_DISABLE_CAMERA = JavaStaticField("I")
    USES_POLICY_DISABLE_KEYGUARD_FEATURES = JavaStaticField("I")
    USES_POLICY_EXPIRE_PASSWORD = JavaStaticField("I")
    USES_POLICY_FORCE_LOCK = JavaStaticField("I")
    USES_POLICY_LIMIT_PASSWORD = JavaStaticField("I")
    USES_POLICY_RESET_PASSWORD = JavaStaticField("I")
    USES_POLICY_WATCH_LOGIN = JavaStaticField("I")
    USES_POLICY_WIPE_DATA = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTagForPolicy = JavaMethod("(I)Ljava/lang/String;")
    getReceiverName = JavaMethod("()Ljava/lang/String;")
    getHeadlessDeviceOwnerMode = JavaMethod("()I")
    supportsTransferOwnership = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    loadIcon = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/graphics/drawable/Drawable;")
    loadLabel = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    isVisible = JavaMethod("()Z")
    usesPolicy = JavaMethod("(I)Z")
    loadDescription = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    getActivityInfo = JavaMethod("()Landroid/content/pm/ActivityInfo;")
    getComponent = JavaMethod("()Landroid/content/ComponentName;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")