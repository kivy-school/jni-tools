from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcci"]

class zzcci(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzcci"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("Ljava/lang/String;")
    zzb = JavaField("I")
    zza = JavaStaticMethod("(Lorg/json/JSONArray;)Lcom/google/android/gms/internal/ads/zzcci;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")