from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VersionInfo"]

class VersionInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/VersionInfo"
    __javaconstructor__ = [("(III)V", False)]
    zza = JavaField("I")
    zzb = JavaField("I")
    zzc = JavaField("I")
    getMajorVersion = JavaMethod("()I")
    getMinorVersion = JavaMethod("()I")
    getMicroVersion = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")