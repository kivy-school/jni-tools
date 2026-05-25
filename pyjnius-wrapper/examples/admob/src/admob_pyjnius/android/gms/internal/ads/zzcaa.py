from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcaa"]

class zzcaa(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzcaa"
    __javaconstructor__ = [("(Landroid/os/IBinder;Landroid/os/IBinder;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("Landroid/view/View;")
    zzb = JavaField("Ljava/util/Map;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")