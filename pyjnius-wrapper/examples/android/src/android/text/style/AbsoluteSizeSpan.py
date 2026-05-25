from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbsoluteSizeSpan"]

class AbsoluteSizeSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/AbsoluteSizeSpan"
    __javaconstructor__ = [("(I)V", False), ("(IZ)V", False), ("(Landroid/os/Parcel;)V", False)]
    getSpanTypeId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getSize = JavaMethod("()I")
    getDip = JavaMethod("()Z")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    updateMeasureState = JavaMethod("(Landroid/text/TextPaint;)V")
    toString = JavaMethod("()Ljava/lang/String;")