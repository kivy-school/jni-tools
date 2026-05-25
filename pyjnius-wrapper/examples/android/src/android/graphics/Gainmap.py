from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Gainmap"]

class Gainmap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Gainmap"
    __javaconstructor__ = [("(Landroid/graphics/Bitmap;)V", False), ("(Landroid/graphics/Gainmap;Landroid/graphics/Bitmap;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getGainmapContents = JavaMethod("()Landroid/graphics/Bitmap;")
    setGainmapContents = JavaMethod("(Landroid/graphics/Bitmap;)V")
    setRatioMin = JavaMethod("(FFF)V")
    getRatioMin = JavaMethod("()[F")
    setRatioMax = JavaMethod("(FFF)V")
    getRatioMax = JavaMethod("()[F")
    setGamma = JavaMethod("(FFF)V")
    getGamma = JavaMethod("()[F")
    setEpsilonSdr = JavaMethod("(FFF)V")
    getEpsilonSdr = JavaMethod("()[F")
    setEpsilonHdr = JavaMethod("(FFF)V")
    getEpsilonHdr = JavaMethod("()[F")
    setDisplayRatioForFullHdr = JavaMethod("(F)V")
    getDisplayRatioForFullHdr = JavaMethod("()F")
    setMinDisplayRatioForHdrTransition = JavaMethod("(F)V")
    getMinDisplayRatioForHdrTransition = JavaMethod("()F")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")