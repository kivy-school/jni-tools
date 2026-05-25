from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzben"]

class zzben(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzben"
    zza = JavaStaticMethod("(Landroid/os/Parcel;)Z")
    zzb = JavaStaticMethod("(Landroid/os/Parcel;Landroid/os/Parcelable$Creator;)Landroid/os/Parcelable;")
    zzc = JavaStaticMethod("(Landroid/os/Parcel;Landroid/os/Parcelable;)V")
    zzd = JavaStaticMethod("(Landroid/os/Parcel;Landroid/os/Parcelable;)V")
    zze = JavaStaticMethod("(Landroid/os/Parcel;Landroid/os/IInterface;)V")
    zzf = JavaStaticMethod("(Landroid/os/Parcel;)Ljava/util/ArrayList;")
    zzg = JavaStaticMethod("(Landroid/os/Parcel;)Ljava/util/HashMap;")
    zzh = JavaStaticMethod("(Landroid/os/Parcel;)V")