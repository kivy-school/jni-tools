from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LensIntrinsicsSample"]

class LensIntrinsicsSample(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/LensIntrinsicsSample"
    __javaconstructor__ = [("(J[F)V", False)]
    getLensIntrinsics = JavaMethod("()[F")
    getTimestampNanos = JavaMethod("()J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")