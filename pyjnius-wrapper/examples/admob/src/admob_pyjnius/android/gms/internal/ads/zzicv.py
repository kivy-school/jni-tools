from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzicv"]

class zzicv(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzicv"
    __javaconstructor__ = [("()V", False)]
    zzcY = JavaMethod("()Lcom/google/android/gms/internal/ads/zzify;")
    zzaM = JavaMethod("()Lcom/google/android/gms/internal/ads/zzidl;")
    zzaO = JavaMethod("(Ljava/io/OutputStream;)V")
    zzcX = JavaMethod("(Lcom/google/android/gms/internal/ads/zzidu;)V")