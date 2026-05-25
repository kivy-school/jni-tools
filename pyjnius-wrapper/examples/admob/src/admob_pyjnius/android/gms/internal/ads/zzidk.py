from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzidk"]

class zzidk(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzidk"
    write = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False)])
    zza = JavaMethod("()Lcom/google/android/gms/internal/ads/zzidl;")
    zzb = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")