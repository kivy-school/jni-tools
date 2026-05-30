from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class OverlayManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/om/OverlayManager"
    getOverlayInfosForTarget = JavaMethod("(Ljava/lang/String;)Ljava/util/List;")
    commit = JavaMethod("(Landroid/content/om/OverlayManagerTransaction;)V")

class OverlayInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/om/OverlayInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTargetOverlayableName = JavaMethod("()Ljava/lang/String;")
    getTargetPackageName = JavaMethod("()Ljava/lang/String;")
    getOverlayIdentifier = JavaMethod("()Landroid/content/om/OverlayIdentifier;")
    getOverlayName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class FabricatedOverlay(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/om/FabricatedOverlay"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    setResourceValue = JavaMultipleMethod([("(Ljava/lang/String;Landroid/content/res/AssetFileDescriptor;Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;IILjava/lang/String;)V", False, False), ("(Ljava/lang/String;ILjava/lang/String;Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Landroid/os/ParcelFileDescriptor;Ljava/lang/String;)V", False, False)])
    setNinePatchResourceValue = JavaMethod("(Ljava/lang/String;Landroid/os/ParcelFileDescriptor;Ljava/lang/String;)V")
    setTargetOverlayable = JavaMethod("(Ljava/lang/String;)V")
    getIdentifier = JavaMethod("()Landroid/content/om/OverlayIdentifier;")

class OverlayManagerTransaction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/om/OverlayManagerTransaction"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    registerFabricatedOverlay = JavaMethod("(Landroid/content/om/FabricatedOverlay;)V")
    unregisterFabricatedOverlay = JavaMethod("(Landroid/content/om/OverlayIdentifier;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    newInstance = JavaStaticMethod("()Landroid/content/om/OverlayManagerTransaction;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class OverlayIdentifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/om/OverlayIdentifier"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")