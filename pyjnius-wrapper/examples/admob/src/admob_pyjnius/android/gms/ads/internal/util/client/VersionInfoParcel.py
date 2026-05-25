from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VersionInfoParcel"]

class VersionInfoParcel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/util/client/VersionInfoParcel"
    __javaconstructor__ = [("(IIZ)V", False), ("(IIZZ)V", False), ("(IIZZZ)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    afmaVersion = JavaField("Ljava/lang/String;")
    buddyApkVersion = JavaField("I")
    clientJarVersion = JavaField("I")
    isClientJar = JavaField("Z")
    isLiteSdk = JavaField("Z")
    forPackage = JavaStaticMethod("()Lcom/google/android/gms/ads/internal/util/client/VersionInfoParcel;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")