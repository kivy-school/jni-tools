from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ForegroundColorSpan"]

class ForegroundColorSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/ForegroundColorSpan"
    __javaconstructor__ = [("(I)V", False), ("(Landroid/os/Parcel;)V", False)]
    getSpanTypeId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getForegroundColor = JavaMethod("()I")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    toString = JavaMethod("()Ljava/lang/String;")