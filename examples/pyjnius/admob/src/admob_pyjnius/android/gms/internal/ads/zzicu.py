from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzicu"]

class zzicu(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzicu"
    __javaconstructor__ = [("()V", False)]
    zzq = JavaField("I")
    zzaM = JavaMethod("()Lcom/google/android/gms/internal/ads/zzidl;")
    zzaN = JavaMethod("()[B")
    zzaO = JavaMethod("(Ljava/io/OutputStream;)V")
    zzaP = JavaMethod("(Ljava/io/OutputStream;)V")
    zzaS = JavaMethod("()Lcom/google/android/gms/internal/ads/zzige;")
    zzaV = JavaStaticMethod("(Lcom/google/android/gms/internal/ads/zzidl;)V")
    zzaW = JavaStaticMethod("(Ljava/lang/Iterable;Ljava/util/List;)V")