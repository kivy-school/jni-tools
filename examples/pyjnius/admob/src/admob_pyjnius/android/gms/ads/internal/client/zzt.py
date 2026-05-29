from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzt"]

class zzt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzt"
    __javaconstructor__ = [("(IILjava/lang/String;J)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("I")
    zzb = JavaField("I")
    zzc = JavaField("Ljava/lang/String;")
    zzd = JavaField("J")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    zza = JavaStaticMethod("(Lorg/json/JSONObject;)Lcom/google/android/gms/ads/internal/client/zzt;")