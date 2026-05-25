from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LensIntrinsicsSample"]

class LensIntrinsicsSample(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/LensIntrinsicsSample"
    __javaconstructor__ = [("(J[F)V", False)]
    getTimestampNanos = JavaMethod("()J")
    getLensIntrinsics = JavaMethod("()[F")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")