from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SuggestionRangeSpan"]

class SuggestionRangeSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/SuggestionRangeSpan"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getSpanTypeId = JavaMethod("()I")
    setBackgroundColor = JavaMethod("(I)V")
    getBackgroundColor = JavaMethod("()I")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")