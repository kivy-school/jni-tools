from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcdd"]

class zzcdd(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzcdd"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/rewarded/ServerSideVerificationOptions;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("Ljava/lang/String;")
    zzb = JavaField("Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")