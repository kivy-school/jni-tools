from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrustedPresentationThresholds"]

class TrustedPresentationThresholds(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/window/TrustedPresentationThresholds"
    __javaconstructor__ = [("(FFI)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getMinAlpha = JavaMethod("()F")
    getMinFractionRendered = JavaMethod("()F")
    getStabilityRequirementMillis = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")